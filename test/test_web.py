#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the web module"""

from __future__ import (
    division,
    absolute_import,
    print_function,
    unicode_literals,
)

import binascii
import hashlib
import json
import random
import shutil
import string
import tempfile
import time
from datetime import datetime, timedelta

import unittest2 as unittest
from enum import Enum
from mock import MagicMock

from beetsplug.beetsonic import bindings
from beetsplug.beetsonic import errors
from beetsplug.beetsonic import web


class ResponseType(Enum):
    xml = 'xml',
    json = 'json',
    jsonp = 'jsonp'


class Struct:
    """
    Recursive class for building and representing object from a dictionary.
    Code from: http://stackoverflow.com/a/6573827
    """

    def __init__(self, obj):
        for k, v in obj.iteritems():
            if isinstance(v, dict):
                setattr(self, k, Struct(v))
            else:
                setattr(self, k, v)

    def __getitem__(self, val):
        return self.__dict__[val]

    def __repr__(self):
        return '{%s}' % str(', '.join('%s : %s' % (k, repr(v)) for
                                      (k, v) in self.__dict__.iteritems()))


class BeetsonicWebTestCase(unittest.TestCase):
    def setUp(self):
        self.configs = {
            'host': '127.0.0.1',
            'port': 5000,
            'cors': '',
            'playlist_dir': tempfile.mkdtemp(),
            'debug': False,
            'username': 'username',
            'password': 'password',
            'ignoredArticles': 'The La Les',
        }
        self.model = MagicMock()
        server = web.SubsonicServer(self.model, self.configs, __name__)
        self.app = server.test_client()

    def tearDown(self):
        shutil.rmtree(self.configs['playlist_dir'])

    def _get_content(self, response, response_type=ResponseType.xml,
                     callback='callback'):
        """Return the Response a Python object that has similar-ish structure
        even though the response types differ."""
        if response_type is ResponseType.xml:
            return bindings.CreateFromDocument(response)
        elif response_type is ResponseType.json:
            json_response = json.loads(response)
            self.assertIn('subsonic-response', json_response,
                          'JSON response must contain key subsonic-response')
            return Struct(json_response['subsonic-response'])
        elif response_type is ResponseType.jsonp:
            self.assertTrue(response.startswith('{}('.format(callback)))
            self.assertTrue(response.endswith(')'))
            return self._get_content(response[len(callback) + 1:-1],
                                     ResponseType.json)

    def _get_response(self, end_point='/rest/ping.view', params={},
                      response_type=ResponseType.xml):
        """Helper to get a response with some sensible defaults"""
        default_params = {
            'v': web.SUBSONIC_API_VERSION,
            'f': response_type.name,
            'c': 'TestApp',
            'u': self.configs['username'],
            'p': self.configs['password'],
            'callback': 'callback',
        }
        default_params.update(params)
        # If the value in a dict is None, let's delete that item, since it
        # doesn't make sense to urlencode that item anyway.
        default_params = {
            key: value
            for key, value in default_params.iteritems()
            if value is not None
            }

        response = self.app.get(end_point, query_string=default_params)
        return self._get_content(response.data, response_type,
                                 default_params['callback'])

    def _assert_missing_required_parameter(self, response_type, response):
        self.assertTrue(self.contains(response, 'error'))
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_MSG,
                         response.error.message)

    def test_authentication_missing_username(self):
        response = self._get_response(params={'u': None})
        self._assert_missing_required_parameter(ResponseType.xml, response)

    def test_authentication_wrong_username(self):
        response = self._get_response(
            params={'u': self.configs['username'] + 'a'})
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.AUTHENTICATION_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.AUTHENTICATION_ERROR_MSG,
                         response.error.message)

    def test_authentication_missing_password_and_token(self):
        response = self._get_response(params={'p': None})
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_MSG,
                         response.error.message)

    def test_authentication_plain_wrong_password(self):
        response = self._get_response(
            params={'p': self.configs['password'] + 'a'}
        )
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.AUTHENTICATION_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.AUTHENTICATION_ERROR_MSG,
                         response.error.message)

    def test_authentication_plain_right_password(self):
        response = self._get_response('/rest/ping.view')
        self.assertEqual(None, response.error)

    def test_authentication_hex_wrong_password(self):
        response = self._get_response(
            params={
                'p': 'enc:{}'.format(
                    binascii.hexlify(self.configs['password'] + 'a')
                )
            }
        )
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.AUTHENTICATION_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.AUTHENTICATION_ERROR_MSG,
                         response.error.message)

    def test_authentication_hex_right_password(self):
        response = self._get_response(
            params={
                'p': 'enc:{}'.format(binascii.hexlify(self.configs['password']))
            }
        )
        self.assertEqual(None, response.error)

    def test_authetication_token_wrong_token(self):
        salt = ''.join(random.choice(string.lowercase) for _ in range(6))
        token = hashlib.md5(self.configs['password'] + 'a' + salt).hexdigest()
        response = self._get_response(
            params={
                'p': None,
                's': salt,
                't': token,
            }
        )
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.AUTHENTICATION_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.AUTHENTICATION_ERROR_MSG,
                         response.error.message)

    def test_authentication_token_right_token(self):
        salt = ''.join(random.choice(string.lowercase) for _ in range(6))
        token = hashlib.md5(self.configs['password'] + salt).hexdigest()
        response = self._get_response(
            params={
                'p': None,
                's': salt,
                't': token,
            }
        )
        self.assertEqual(None, response.error)

    def test_missing_client_version(self):
        response = self._get_response(params={'v': None})
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_MSG,
                         response.error.message)

    def test_client_older_major_version(self):
        version_parts = web.SUBSONIC_API_VERSION.split('.')
        version_major = int(version_parts[0])
        client_version = '{}.{}.{}'.format(
            str(version_major - 1),
            *version_parts[1:]
        )
        response = self._get_response(params={'v': client_version})
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.CLIENT_UPGRADE_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.CLIENT_UPGRADE_ERROR_MSG,
                         response.error.message)

    def test_client_newer_major_version(self):
        version_parts = web.SUBSONIC_API_VERSION.split('.')
        version_major = int(version_parts[0])
        client_version = '{}.{}.{}'.format(
            str(version_major + 1),
            *version_parts[1:]
        )
        response = self._get_response(params={'v': client_version})
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.SERVER_UPGRADE_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.SERVER_UPGRADE_ERROR_MSG,
                         response.error.message)

    def test_client_older_minor_version(self):
        version_parts = web.SUBSONIC_API_VERSION.split('.')
        version_minor = int(version_parts[1])
        client_version = '{}.{}.{}'.format(
            version_parts[0],
            str(version_minor - 1),
            version_parts[2]
        )
        response = self._get_response(params={'v': client_version})
        self.assertEqual(None, response.error)

    def test_client_newer_minor_version(self):
        version_parts = web.SUBSONIC_API_VERSION.split('.')
        version_minor = int(version_parts[1])
        client_version = '{}.{}.{}'.format(
            version_parts[0],
            str(version_minor + 1),
            version_parts[2]
        )
        response = self._get_response(params={'v': client_version})
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.SERVER_UPGRADE_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.SERVER_UPGRADE_ERROR_MSG,
                         response.error.message)

    def response_types(self, func):
        """Decorator utility to run tests with different response types."""
        for response_type in ResponseType:
            with self.subTest(response_type=response_type):
                self.model.reset_mock()
                func(response_type)

    def test_ping(self):
        @self.response_types
        def actual_tests(response_type):
            response = self._get_response('/rest/ping.view',
                                          response_type=response_type)
            self.assertEqual(bindings.ResponseStatus.ok, response.status)

    @staticmethod
    def contains(obj, attr):
        """Helper method to check existence of key in an object."""
        if isinstance(obj, Struct):
            return hasattr(obj, attr)
        return getattr(obj, attr) is not None

    def test_get_indexes_without_modified(self):
        @self.response_types
        def actual_tests(response_type):
            now = datetime.now()
            self.model.get_last_modified.return_value = time.mktime(
                now.timetuple()
            )
            client_last_modified = time.mktime(
                (now + timedelta(0, -10)).timetuple()
            )
            response = self._get_response(
                '/rest/getIndexes.view',
                {'ifModifiedSince': client_last_modified},
                response_type
            )
            self.assertFalse(self.contains(response, 'indexes'))
            self.model.get_last_modified.assert_called_once()

    def test_get_indexes_empty_indexes(self):
        @self.response_types
        def actual_tests(response_type):
            now = time.mktime(datetime.now().timetuple())
            self.model.get_last_modified.return_value = now
            self.model.get_album_artists.return_value = []
            self.model.get_singletons.return_value = []
            response = self._get_response('/rest/getIndexes.view',
                                          response_type=response_type)
            self.model.get_album_artists.assert_called_once()
            self.model.get_singletons.assert_called_once()
            self.assertNotEqual(None, response.indexes)
            self.assertEqual(self.configs['ignoredArticles'],
                             response.indexes.ignoredArticles)
            self.assertEqual(now, response.indexes.lastModified)
            self.assertEqual(0, len(response.indexes.index))
            self.assertEqual(0, len(response.indexes.child))

    def test_get_album_without_id(self):
        @self.response_types
        def actual_tests(response_type):
            response = self._get_response('/rest/getAlbum.view',
                                          response_type=response_type)
            self._assert_missing_required_parameter(response_type, response)

    def test_get_album_with_id(self):
        @self.response_types
        def actual_tests(response_type):
            now = datetime.now()
            self.model.get_album.return_value = bindings.AlbumWithSongsID3(
                id='id',
                name='name',
                songCount=1,
                duration=60,
                created=now
            )
            response = self._get_response('/rest/getAlbum.view',
                                          {'id': 'id'},
                                          response_type)
            self.model.get_album.assert_called_once_with('id')
            self.assertTrue(self.contains(response, 'album'))
            self.assertEqual('id', response.album.id)
            self.assertEqual('name', response.album.name)
            self.assertEqual(1, response.album.songCount)
            self.assertEqual(60, response.album.duration)


if __name__ == '__main__':
    unittest.main()
