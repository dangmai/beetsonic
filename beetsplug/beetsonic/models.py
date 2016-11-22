# -*- coding: utf-8 -*-
"""
Model to get music information from beets.
"""
import random

import enum
import six
from beets.ui import decargs
from beetsplug.lyrics import LyricsPlugin

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
        id_type = BeetIdType(value_parts[0])
        if id_type is BeetIdType.album or id_type is BeetIdType.item:
            id_value = int(value_parts[1])
        else:
            id_value = value_parts[1]

        return id_type, id_value

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
        item_id = BeetIdType.get_item_id(item.id)
        album_id = None
        if item.album_id:
            album_id = BeetIdType.get_album_id(item.album_id)
        path = item.path
        if isinstance(path, six.string_types):
            path = item.path.decode('utf-8')
        return utils.create_song(
            item_id, item.title, album=item.album, artist=item.artist,
            year=item.year, genre=item.genre, coverArt=album_id,
            path=path, parent=album_id,
        )

    @staticmethod
    def _create_album(album):
        """
        Create a Child object from beets' Album.
        :param album: The beet's Album object.
        :return: The Child object.
        """
        art_path = None
        if album['artpath']:
            art_path = BeetIdType.get_album_id(album[u'id'])
        return utils.create_album(
            BeetIdType.get_album_id(album['id']), album['album'],
            artist=album['albumartist'], year=album['year'],
            genre=album['genre'], coverArt=art_path,
            parent=BeetIdType.get_artist_id(album['albumartist'])
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

    def _get_albums_from_artist(self, artist_name, columns):
        """
        Get the Album objects from an artist.
        :param artist_name: Name of the artist.
        :param columns: The columns to fetch from the table.
        :return: A list of Album objects.
        """
        with self.lib.transaction() as tx:
            query = 'SELECT {} FROM albums WHERE albumartist=?'.format(
                ', '.join(columns)
            )
            rows = tx.query(query, (artist_name,))
        albums = [dict(zip(columns, row)) for row in rows]
        return albums

    def get_music_directory(self, object_id):
        beet_id = BeetIdType.get_type(object_id)
        children = []
        if beet_id[0] is BeetIdType.album:
            album = self.lib.get_album(beet_id[1])
            name = album.album
            children = [self._create_song(item) for item in album.items()]
        elif beet_id[0] is BeetIdType.artist:
            name = beet_id[1]
            columns = ['id', 'album', 'albumartist', 'year', 'genre', 'artpath']
            albums = self._get_albums_from_artist(beet_id[1], columns)
            for album in albums:
                children.append(self._create_album(album))
        else:
            # It is the Item here
            item = self.lib.get_item(beet_id[1])
            name = item.title
        return utils.create_directory(object_id, name, children,
                                      parent=beet_id[1])

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

    @staticmethod
    def get_user(username):
        return utils.create_user(
            username=username,
            scrobbling_enabled=False,
            admin_role=True,
            settings_role=False,
            download_role=True,
            upload_role=False,
            playlist_role=True,
            cover_art_role=True,
            comment_role=False,
            podcast_role=False,
            stream_role=True,
            jukebox_role=False,
            share_role=False,
            video_conversion_role=False,
            folder_ids=[BEET_MUSIC_FOLDER_ID]
        )

    def get_cover_art(self, object_id):
        """
        Return the cover art location for an Item, Album or Artist.
        :param object_id: The Id of the object.
        :return: The path to the cover art file.
        """
        beet_id = BeetIdType.get_type(object_id)
        location = None
        if beet_id[0] is BeetIdType.album:
            album = self.lib.get_album(beet_id[1])
            if album:
                location = album.artpath or None
        elif beet_id[0] is BeetIdType.artist:
            columns = ['artpath']
            albums = self._get_albums_from_artist(beet_id[1], columns)
            albums = [album for album in albums if album[u'artpath']]
            if len(albums) > 0:
                location = str(albums[0][u'artpath'])
        elif beet_id[0] is BeetIdType.item:
            item = self.lib.get_item(beet_id[1])
            if item:
                album = item.get_album()
                if album and album.artpath:
                    location = album.artpath

        return location

    @staticmethod
    def get_lyrics(artist, title):
        # For now let's return an empty lyrics if either artist or lyrics is
        # not passed in
        empty_lyrics = utils.create_lyrics('', artist=artist, title=title)
        if not artist or not title:
            return empty_lyrics
        lyrics_plugin = LyricsPlugin()
        lyrics = lyrics_plugin.get_lyrics(artist, title)
        if not lyrics:
            return empty_lyrics
        return utils.create_lyrics(lyrics, artist=artist, title=title)

    def get_genres(self):
        album_query = 'SELECT genre, count(genre) FROM albums GROUP BY genre'
        item_query = 'SELECT genre, count(genre) FROM items GROUP BY genre'
        with self.lib.transaction() as tx:
            distinct_album_genres = tx.query(album_query)
            distinct_item_genres = tx.query(item_query)
        album_genre_map = {row[0]: int(row[1]) for row in distinct_album_genres}
        item_genre_map = {row[0]: int(row[1]) for row in distinct_item_genres}
        all_genres = set(album_genre_map.keys()).union(
            set(item_genre_map.keys())
        )
        genre_objs = [
            utils.create_genre(
                genre,
                album_genre_map[genre] if album_genre_map.has_key(genre) else 0,
                item_genre_map[genre] if item_genre_map.has_key(genre) else 0)
            for genre in all_genres]
        return utils.create_genres(genre_objs)
