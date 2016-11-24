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
import unittest
from collections import namedtuple

from enum import Enum
from mock import MagicMock
from six.moves.urllib.parse import urlencode

from beetsplug.beetsonic import bindings
from beetsplug.beetsonic import errors
from beetsplug.beetsonic import web


class ResponseType(Enum):
    xml = 'xml',
    json = 'json',
    jsonp = 'jsonp'


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

    @staticmethod
    def _get_content(response, response_type=ResponseType.xml):
        """Return the Response a Python object that has similar-ish structure
        even though the response types differ."""
        if response_type is ResponseType.xml:
            return bindings.CreateFromDocument(response)
        elif response_type is ResponseType.json:
            return json.loads(
                response,
                object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    def _get_response(self, end_point='/rest/ping.view', params={},
                      response_type=ResponseType.xml):
        """Helper to get a response with some sensible defaults"""
        default_params = {
            'v': web.SUBSONIC_API_VERSION,
            'f': ResponseType.xml.name,
            'c': 'TestApp',
            'u': self.configs['username'],
            'p': self.configs['password'],
        }
        default_params.update(params)
        # If the value in a dict is None, let's delete that item, since it
        # doesn't make sense to urlencode that item anyway.
        default_params = {
            key: value
            for key, value in default_params.iteritems()
            if value is not None
            }

        url = '{}?{}'.format(end_point, urlencode(default_params))
        return self._get_content(self.app.get(url).data, response_type)

    def test_authentication_missing_username(self):
        response = self._get_response(params={'u': None})
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_MSG,
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

    def test_ping(self):
        response = self._get_response('/rest/ping.view')
        self.assertEqual(bindings.ResponseStatus.ok,
                         response.status)

    def test_get_indexes(self):
        response = self._get_response('/rest/getIndexes.view')


if __name__ == '__main__':
    unittest.main()
