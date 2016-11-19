"""
Model to get music information from beets.
"""
import random

import enum
from beets.ui import decargs

from beetsplug.beetsonic import utils

BEET_MUSIC_FOLDER_ID = 1


@enum.unique
class BeetIdType(enum.Enum):
    album = 'album'
    item = 'item'
    artist = 'artist'

    @staticmethod
    def get_type(value):
        """
        Return the BeetIdType for an Id value.
        :param value: the Id value.
        :return: the BeetIdType Enum.
        """
        value_parts = value.split(':')
        if len(value_parts) <= 1:
            raise ValueError(u'Invalid Id: {}'.format(value))
        return BeetIdType(value_parts[0]), value_parts[1]

    @staticmethod
    def get_artist_id(name):
        """
        Return the Subsonic id for an artist.
        :param name: The name of the artist.
        :return: The Subsonic Id for that artist.
        """
        return BeetIdType.artist.value + ':' + name

    @staticmethod
    def get_album_id(album_id):
        """
        Return the Subsonic id for an album
        :param album_id: The beets internal Id for an album.
        :return: The Subsonic Id for that album.
        """
        return BeetIdType.album.value + ':' + str(album_id)

    @staticmethod
    def get_item_id(item_id):
        """
        Return the Subsonic id for a item
        :param item_id: The beets internal Id for an Item.
        :return: The Subsonic Id for that Item.
        """
        return BeetIdType.item.value + ':' + str(item_id)


class BeetModel(object):
    def __init__(self, lib):
        self.lib = lib

    @staticmethod
    def _create_artist(name, **kwargs):
        # Since beets doesn't track artist ids, we'll make the id the name
        # of the artist, prefixed with the string 'artist:', in order to
        # differentiate between Artist and other metadata types.
        return utils.create_artist(BeetIdType.get_artist_id(name), name,
                                   **kwargs)

    @staticmethod
    def _create_song(item):
        """
        Create a Child object from beets' Item.
        :param item: The beet's Item object.
        :return: The Child object.
        """
        return utils.create_song(
            BeetIdType.get_item_id(item.id), item.title, album=item.album,
            artist=item.artist, year=item.year, genre=item.genre)

    @staticmethod
    def _create_album(album):
        """
        Create a Child object from beets' Album.
        :param album: The beet's Album object.
        :return: The Child object.
        """
        return utils.create_album(
            BeetIdType.get_album_id(album['id']), album['album'],
            artist=album['albumartist'], year=album['year'],
            genre=album['genre']
        )

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
                                      name=u'beets music folder')
        ])

    def get_music_directory(self, id):
        original_id = id
        id = BeetIdType.get_type(id)
        children = []
        if id[0] is BeetIdType.album:
            album = self.lib.get_album(int(id[1]))
            name = album.album
            children = [self._create_song(item) for item in album.items()]
        elif id[0] is BeetIdType.artist:
            with self.lib.transaction() as tx:
                keys = ['id', 'album', 'albumartist', 'year', 'genre']
                query = 'SELECT {} FROM albums WHERE albumartist=?'.format(
                    ', '.join(keys)
                )
                rows = tx.query(
                    query,
                    (id[1],)
                )
            name = id[1]
            for row in rows:
                album = dict(zip(keys, row))
                children.append(self._create_album(album))
        else:
            raise ValueError(u'Invalid Id type {}'.format(id[0]))
        return utils.create_directory(original_id, name, children)

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
        id = BeetIdType.get_type(id)[1]
        item = self.lib.get_item(id)
        if not item:
            raise ValueError(u'Song with id {} not found'.format(id))
        return item.path
