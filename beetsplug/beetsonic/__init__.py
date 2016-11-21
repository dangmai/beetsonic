# -*- coding: utf-8 -*-
# This file is part of beets.
# Copyright 2016, Dang Mai.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

"""Subsonic Interface for beets"""

from beets.plugins import BeetsPlugin
from beets.ui import Subcommand

from models import BeetModel
from web import SubsonicServer


class BeetsonicPlugin(BeetsPlugin):
    def __init__(self):
        super(BeetsonicPlugin, self).__init__()
        self.config.add({
            'host': u'127.0.0.1',
            'port': 5000,
            'cors': '',
            'ignoredArticles': u'The El La Los Las Le Les',
        })

    def commands(self):
        def init_server(lib, opts, args):
            model = BeetModel(lib)
            if opts.username is None:
                raise KeyError('Username is required')
            if opts.password is None:
                raise KeyError('Password is required')
            # Get all the args and opts into one variable

            configs = {
                u'host': self.config['host'].get(unicode),
                u'port': self.config['port'].get(int),
                u'cors': self.config['cors'].get(unicode),
                u'debug': opts.debug,
                u'username': opts.username,
                u'password': opts.password,
                u'ignoredArticles': self.config['ignoredArticles'].get(unicode),
            }
            app = SubsonicServer(model, configs, __name__)
            app.run(
                host=configs[u'host'],
                port=configs[u'port'],
                debug=configs[u'debug'],
            )

        cmd = Subcommand('sonic',
                         help='Run Subsonic server interface for beets')
        cmd.parser.add_option(u'-u', u'--username', action='store',
                              help=u'username')
        cmd.parser.add_option(u'-p', u'--password', action='store',
                              help=u'password')
        cmd.parser.add_option(u'-d', u'--debug', action='store_true',
                              default=False, help=u'debug mode')
        cmd.func = init_server
        return [cmd]
