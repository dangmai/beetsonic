"""
Utilities module
"""

import io
import json
import os
import time
from datetime import datetime

import pyxb

from beetsplug.beetsonic import bindings


def element_to_obj(element, use_name=True):
    """
    Convert a bound element to a Python object that can be serialized.
    :param pyxb.binding.basis.complexTypeDefinition element: The bound element.
    :param use_name: Whether to use element name as the key or not.
    :return: The converted Object.
    """
    if isinstance(element, pyxb.binding.content._PluralBinding):
        child_elements = [element_to_obj(el, False) for el in element]
        element_name = element._PluralBinding__elementBinding.name().localName()
        return {element_name: child_elements}
    elif isinstance(element, pyxb.binding.basis.complexTypeDefinition):
        attributes = [attr.localName() for attr in element._AttributeMap.keys()]
        attr_map = {attr: getattr(element, attr)
                    for attr in attributes
                    if getattr(element, attr) is not None}

        child_elements = [el.localName()
                          for el in element._ElementMap.keys()
                          if getattr(element, el.localName()) is not None]
        for child_element in child_elements:
            attr_map.update(
                element_to_obj(getattr(element, child_element), True))

        if use_name:
            attr_map = {element._element().name().localName(): attr_map}
        return attr_map
    else:
        return element


def create_subsonic_response(version, status=bindings.ResponseStatus.ok,
                             **kwargs):
    response = bindings.subsonic_response(
        version=version,
        status=status,
        **kwargs
    )
    return response


def create_artist(id, name, **kwargs):
    """
    Helper method to create an Artist object.
    :param name: Name of the artist
    :return: The Artist object
    """
    return bindings.Artist(
        id=id,
        name=name,
        **kwargs
    )


def create_artist_with_albums_id3(id, name, album_count, albums=[], **kwargs):
    """
    Create a ArtistWithAlbumsID3 object.
    :param id: Id of the artist.
    :param name: Name of the artist.
    :param album_count: Number of the albums belonging to the artist.
    :param bindings.AlbumID3 albums: A list of AlbumID3 objects that belongs to
    the artist.
    :return: The ArtistWithAlbumsID3 object.
    """
    artist = bindings.ArtistWithAlbumsID3(
        id=id,
        name=name,
        albumCount=album_count,
        **kwargs
    )
    for album in albums:
        artist.append(album)
    return artist


def create_song(id, title, **kwargs):
    """
    Helper method to create a Child object, representing a Song.
    :param id: Id of the song.
    :param title: Title of the song
    :param kwargs: The other properties of the song.
    :return: The Child object
    """
    return bindings.Child(
        id=id,
        title=title,
        isDir=False,
        **kwargs
    )


def create_album(id, title, **kwargs):
    """
    Helper method to create a Child object, representing an Album.
    :param id: The id of the album.
    :param title: The title of the album.
    :param kwargs: The other properties of the album.
    :return: The Child object.
    """
    return bindings.Child(
        id=id,
        title=title,
        album=title,
        isDir=True,
        **kwargs
    )


def create_directory(id, name, children=[], **kwargs):
    """
    Helper method to create a Directory object.
    :param id: The id of the Directory.
    :param name: The name of the Directory.
    :param children: The Children objects to append to the Directory.
    :param kwargs: The other properties of the Directory.
    :return: The Directory object
    """
    directory = bindings.Directory(
        id=id,
        name=name,
        **kwargs
    )
    for child in children:
        directory.append(child)
    return directory


def create_album_id3(id, name, song_count, duration, created, **kwargs):
    """
    Helper method to create an AlbumID3 object.
    :param id: The id of the album.
    :param name: The name of the album.
    :param song_count: The number of songs in the album.
    :param duration: The duration of the album.
    :param created: When the album was created.
    :param kwargs: Other properties of the album.
    :return: The AlbumID3 object.
    """
    album = bindings.AlbumID3(
        id=id,
        name=name,
        songCount=song_count,
        duration=duration,
        created=created,
        **kwargs
    )
    return album


def create_album_with_songs_id3(id, name, song_count, duration, created,
                                children=[], **kwargs):
    """
    Helper method to create a AlbumWithSongsID3 object.
    :param id: The id of the Album.
    :param name: The name of the Album.
    :param song_count: The number of songs in the album.
    :param duration: The duration of the album.
    :param created: When the album was created.
    :param children: The Children objects to append to the album.
    :param kwargs: Other properties of the album.
    :return: The AlbumWithSongsID3 object.
    """
    album = bindings.AlbumWithSongsID3(
        id=id,
        name=name,
        songCount=song_count,
        duration=duration,
        created=created,
        **kwargs
    )
    for child in children:
        album.append(child)
    return album


def create_user(username, scrobbling_enabled, admin_role, settings_role,
                download_role, upload_role, playlist_role, cover_art_role,
                comment_role, podcast_role, stream_role, jukebox_role,
                share_role, video_conversion_role, folder_ids, **kwargs):
    user = bindings.User(
        username=username,
        scrobblingEnabled=scrobbling_enabled,
        adminRole=admin_role,
        settingsRole=settings_role,
        downloadRole=download_role,
        uploadRole=upload_role,
        playlistRole=playlist_role,
        coverArtRole=cover_art_role,
        commentRole=comment_role,
        podcastRole=podcast_role,
        streamRole=stream_role,
        jukeboxRole=jukebox_role,
        shareRole=share_role,
        videoConversionRole=video_conversion_role,
        **kwargs
    )
    for folder_id in folder_ids:
        user.append(folder_id)
    return user


def create_indexes(artists, ignored_articles_str):
    """
    Create indexes from a list of Artist objects.
    An index consists of an uppercase character, mapping to all the Artists
    whose name starts with that character.
    :param artists: List of Artist objects.
    :param ignoredArticles: List of words to ignore while building the indexes.
    :return: An Indexes object
    """
    ignored_articles = ignored_articles_str.split(' ')
    indexes = bindings.Indexes()
    indexes.ignoredArticles = ignored_articles_str

    def index_func(map, artist):
        """
        The reducer function to index the list
        """
        name_parts = artist.name.split(' ')
        while name_parts[0] in ignored_articles:
            name_parts.pop(0)
        first_char = name_parts[0][:1].upper()
        if first_char not in map:
            map[first_char] = []
        map[first_char].append(artist)
        return map

    char_map = reduce(
        index_func,
        artists,
        dict()
    )
    for char, artists in sorted(char_map.iteritems()):
        index = bindings.Index(name=char)
        for artist in artists:
            index.append(artist)
        indexes.append(index)

    return indexes


def create_music_folders(music_folders):
    """
    Create a Music Folders object from a list of Music Folder objects
    :param music_folders: List of Music Folder objects
    :return: Music Folders object
    """
    folders = bindings.MusicFolders()
    for music_folder in music_folders:
        folders.append(music_folder)
    return folders


def create_music_folder(id, **kwargs):
    """
    Create a Music Folder object
    :param id: Id of the Music Folder
    :param kwargs: The other keyword arguments
    :return: The Music Folder object
    """
    return bindings.MusicFolder(
        id=id,
        **kwargs
    )


def create_songs(child_objects):
    """
    Create a Songs object from a list of Child objects.
    :param child_objects: List of Child objects.
    :return: a Songs object.
    """
    songs = bindings.Songs()
    for child in child_objects:
        songs.append(child)
    return songs


def create_artist_info(**kwargs):
    """
    Create an ArtistInfo object.
    :param kwargs: The properties of the ArtistInfo object.
    :return: The ArtistInfo object.
    """
    return bindings.ArtistInfo(**kwargs)


def create_lyrics(content, **kwargs):
    """
    Create a Lyrics object.
    :param content: The content of the lyrics.
    :param kwargs: Other properties of the Lyrics object.
    :return: The Lyrics object.
    """
    lyrics = bindings.Lyrics(content, **kwargs)
    return lyrics


def create_genres(genre_objs):
    """
    Create a Genres object from a list of Genre objects.
    :param genre_obs: List of Genre objects.
    :return: The Genres object.
    """
    genres = bindings.Genres()
    for genre_obj in genre_objs:
        genres.append(genre_obj)
    return genres


def create_genre(name, album_count, song_count):
    """
    Create a Genre object.
    :param name: Name of the genre.
    :param song_count: The number of songs in the genre.
    :param album_count: The number of albums in the genre.
    :return: The Genre object.
    """
    return bindings.Genre(name, songCount=song_count, albumCount=album_count)


def create_playlists(playlists):
    """
    Create a Playlists object from a list of Playlist objects.
    :param playlists: List of Playlist objects.
    :param kwargs: Other properties of the Playlists.
    :return: The Playlists object.
    """
    playlists_obj = bindings.Playlists()
    for playlist in playlists:
        playlists_obj.append(playlist)
    return playlists_obj


def create_playlist(songs, allowed_users, playlist_id, name, song_count,
                    duration, created, changed, **kwargs):
    """
    Create a PlaylistWithSongs object.
    :param bindings.Child[] songs: List of Child objects.
    :param allowed_users: List of allowed users.
    :param playlist_id: Id of the playlist.
    :param name: Name of the playlist.
    :param song_count: Number of songs in the playlist.
    :param duration: Duration of the playlist.
    :param created: When the playlist was created.
    :param changed: When the playlist was last changed.
    :param kwargs: Other properties of the playlist.
    :return: The Playlist object.
    """
    playlist = bindings.PlaylistWithSongs(
        id=playlist_id,
        name=name,
        songCount=song_count,
        duration=duration,
        created=created,
        changed=changed,
        **kwargs
    )
    # print allowed_users
    for user in allowed_users:
        playlist.append(user)
    for song in songs:
        playlist.append(song)
    return playlist


def create_podcasts():
    """
    Create a Podcasts object.
    :return: A Podcasts object.
    """
    return bindings.Podcasts()


def get_music_type():
    """
    Get the bound Music Type
    :return: the MediaType for Music.
    """
    return bindings.MediaType.music


def parse_m3u(m3u_location):
    """
    Parse a m3u file.
    :param m3u_location: Location of the m3u playlist.
    :return: A list of absolute paths to the songs that are in the playlist.
    """
    with io.open(m3u_location, encoding='utf-8') as m3u:
        items = m3u.readlines()
    items = [os.path.abspath(item)
             for item in items
             if not item.startswith(u'#')]
    return items


class JsonEncoder(json.JSONEncoder):
    """JSON Encoder that handles DateTime, converting it to Unix timestamp"""

    def default(self, o):
        if isinstance(o, datetime):
            return time.mktime(o.timetuple())
        return json.JSONEncoder.default(self, o)
