"""
Utilities module
"""
from beetsplug.beetsonic import bindings


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
    # TODO implement ignoredArticles functionality
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
    lyrics = bindings.Lyrics(content, **kwargs)
    return lyrics
