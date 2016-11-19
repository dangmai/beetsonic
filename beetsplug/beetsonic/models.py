"""
Model to get music information from beets.
"""
import random

from beets.ui import decargs

from beetsplug.beetsonic import utils

BEET_MUSIC_FOLDER_ID = 1


class BeetModel(object):
    def __init__(self, lib):
        self.lib = lib

    @staticmethod
    def _create_artist(name, **kwargs):
        # Since beets doesn't track artist ids, we'll make the id the name
        # of the artist, prefixed with the string 'artist:', in order to
        # differentiate between Artist and other metadata types.
        return utils.create_artist('artist:' + name, name, **kwargs)

    @staticmethod
    def _create_song(item):
        # Create a Child object from beets' Item
        return utils.create_song(
            item.id, item.title, album=item.album, artist=item.artist,
            year=item.year, genre=item.genre)

    def get_album_artists(self):
        """
        Get all album artists
        :return: List of Artist objects
        """
        with self.lib.transaction() as tx:
            rows = tx.query(
                'SELECT DISTINCT albumartist FROM albums ORDER BY albumartist'
            )
        return [self._create_artist(row[0]) for row in rows]

    def get_singletons(self):
        """
        Get all the singletons in Child objects
        :return: Child objects for singletons
        """
        results = self.lib.items(u'singleton:true')
        return [self._create_song(item) for item in results]

    def get_last_modified(self):
        """
        Get the timestamp of the last modified operation
        :return: the Unix timestamp of the last modified operation
        """
        with self.lib.transaction() as tx:
            rows = tx.query('SELECT max(mtime) FROM items')
        return rows[0][0]

    @staticmethod
    def get_music_folders():
        """
        Get the Music Folders object
        :return: the Music Folders object
        """
        return utils.create_music_folders([
            utils.create_music_folder(BEET_MUSIC_FOLDER_ID,
                                      name='beets music folder')
        ])

    def get_random_songs(self, size=10, genre=None, from_year=None,
                         to_year=None, music_folder_id=None):
        """
        Get random songs wrapped in a Songs object
        :param size: Maximum number of songs to return.
        :param genre: Only returns songs belonging to this genre.
        :param from_year: Only return songs published after or in this year.
        :param to_year: Only return songs published before or in this year.
        :param music_folder_id: Only return songs in this music folder.
        :return: a Songs object.
        """
        songs = []
        if not music_folder_id or music_folder_id == str(BEET_MUSIC_FOLDER_ID):
            # Adapted from the Random plugin
            query_parts = []
            if genre:
                query_parts.append('genre:{}'.format(genre))
            if from_year or to_year:
                from_year = from_year or ''
                to_year = to_year or ''
                year_range = [from_year, to_year]
                query_parts.append('year:{}'.format('..'.join(year_range)))
            query = decargs(query_parts)
            result = list(self.lib.items(query))
            number = min(len(result), size)
            items = random.sample(result, number)
            songs = [self._create_song(item) for item in items]

        return utils.create_songs(songs)

    def get_song_location(self, id):
        item = self.lib.get_item(id)
        if not item:
            raise ValueError(u'Song with id {} not found'.format(id))
        return item.path
