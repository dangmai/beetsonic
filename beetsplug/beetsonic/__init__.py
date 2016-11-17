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


def init_server(lib, opts, args):
    model = BeetModel(lib)
    app = SubsonicServer(model, __name__)
    app.run(debug=True)


beetsonic_cmd = Subcommand('sonic',
                           help='Run Subsonic server interface for beets')
beetsonic_cmd.func = init_server


class BeetsonicPlugin(BeetsPlugin):
    def commands(self):
        return [beetsonic_cmd]
