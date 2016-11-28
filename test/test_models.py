#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the models module"""

from __future__ import (
    division,
    absolute_import,
    print_function,
    unicode_literals,
)

from datetime import datetime

import beets
import unittest2 as unittest
from beets.library import Item

from beetsplug.beetsonic.models import BeetsModel, BeetIdType

# Dummy item creation.
_item_ident = 0


def item(lib=None):
    global _item_ident
    _item_ident += 1
    i = beets.library.Item(
        title=u'the title',
        artist=u'the artist',
        albumartist=u'the album artist',
        album=u'the album',
        genre=u'the genre',
        composer=u'the composer',
        grouping=u'the grouping',
        year=1,
        month=2,
        day=3,
        track=4,
        tracktotal=5,
        disc=6,
        disctotal=7,
        lyrics=u'the lyrics',
        comments=u'the comments',
        bpm=8,
        comp=True,
        path='somepath{0}'.format(_item_ident),
        length=60.0,
        bitrate=128000,
        format='FLAC',
        mb_trackid='someID-1',
        mb_albumid='someID-2',
        mb_artistid='someID-3',
        mb_albumartistid='someID-4',
        album_id=None,
    )
    if lib:
        lib.add(i)
    return i


_album_ident = 0


def album(lib=None):
    global _item_ident
    _item_ident += 1
    i = beets.library.Album(
        artpath=None,
        albumartist=u'some album artist',
        albumartist_sort=u'some sort album artist',
        albumartist_credit=u'some album artist credit',
        album=u'the album',
        genre=u'the genre',
        year=2014,
        month=2,
        day=5,
        tracktotal=0,
        disctotal=1,
        comp=False,
        mb_albumid='someID-1',
        mb_albumartistid='someID-1'
    )
    if lib:
        lib.add(i)
    return i


class BeetsModelTest(unittest.TestCase):
    """A test case that includes an in-memory library object (`lib`) and
    an item added to the library (`i`).
    """

    def setUp(self):
        super(BeetsModelTest, self).setUp()
        self.lib = beets.library.Library(':memory:')
        self.a = album(self.lib)
        self.i = item()
        self.i.album_id = self.a.id
        self.lib.add(self.i)

        self.model = BeetsModel(self.lib)

    def tearDown(self):
        self.lib._connection().close()
        super(BeetsModelTest, self).tearDown()

    def test_get_album(self):
        # Add another item to the album
        another = item()
        another.album_id = self.a.id
        self.lib.add(another)

        album_id = 'album:{}'.format(self.a.id)
        album = self.model.get_album(album_id)
        self.assertEqual(self.a.album, album.name)
        self.assertEqual(album_id, album.id)
        self.assertEqual(2, album.songCount)
        self.assertEqual(120, album.duration)
        self.assertEqual(datetime.fromtimestamp(self.a.added), album.created)
        self.assertEqual(self.a.albumartist, album.artist)
        self.assertEqual(BeetIdType.get_artist_id(self.a.albumartist),
                         album.artistId)
        self.assertEqual(BeetIdType.get_album_id(self.a.id), album.coverArt)
        self.assertEqual(self.a.genre, album.genre)

    def test_get_artist_with_albums(self):
        # Create another album for the same artist
        another = album()
        another.album = 'album 2'
        another.artpath = 'artpath'
        self.lib.add(another)

        artist_id = BeetIdType.get_artist_id(another.albumartist)
        artist = self.model.get_artist_with_albums(artist_id)

        self.assertEqual(artist_id, artist.id)
        self.assertEqual(another.albumartist, artist.name)
        self.assertEqual(artist_id, artist.coverArt)
        self.assertEqual(2, len(artist.orderedContent()))
