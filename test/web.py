#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the web module"""

from __future__ import (
    division,
    absolute_import,
    print_function,
    unicode_literals,
)

import json
import shutil
import tempfile
import unittest
from collections import namedtuple

from enum import Enum
from mock import MagicMock

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

    def _assert_common(self, end_point):
        """
        Common assertions, including but not limited to:
        - Make sure authentication info is needed.
        - Make sure version rules are followed.
        - Make sure the same result is returned for different formats.
        :param end_point: The end point to test.
        :return: None
        """
        # First, call the end point without any URL parameters
        response = self.app.get(end_point)

        self.assertEqual(200, response.status_code)
        self.assertEqual('text/xml', response.mimetype)

        response = self._get_content(response.data)
        self.assertNotEqual(None, response.error)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_CODE,
                         response.error.code)
        self.assertEqual(errors.REQUIRED_PARAMETER_ERROR_MSG,
                         response.error.message)

        # Call the end point with different client versions

    def test_ping(self):
        end_point = '/rest/ping.view'
        self._assert_common(end_point)

    def test_get_indexes(self):
        end_point = '/rest/getIndexes.view'
        self._assert_common(end_point)


if __name__ == '__main__':
    unittest.main()
