import pyxb.utils.domutils
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from flask import Blueprint
from flask import Flask
from flask import Response
from flask import g

import bindings

pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(bindings.Namespace)


class SubsonicResponse(Response):
    def __init__(self, content=None, *args, **kwargs):
        if isinstance(content, bindings.Response):
            kwargs['mimetype'] = 'application/xml'
            content = content.toxml('utf-8')
        super(Response, self).__init__(content, *args, **kwargs)

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, bindings.Response):
            return cls(response)
        return super(Response, cls).force_type(response, environ)


rest_api = Blueprint('rest_api', __name__)


@rest_api.before_request
def init_response():
    g.response = bindings.subsonic_response()
    g.response.version = bindings.Version('1.14.0')
    g.response.status = bindings.ResponseStatus.ok


@rest_api.before_request
def init_lib():
    g.lib = app.config['lib']


@rest_api.route('/ping.view')
def ping():
    return g.response


@rest_api.route('/getLicense.view')
def get_license():
    g.response.license = bindings.License(valid=True)
    return g.response


@rest_api.route('/getMusicFolders.view')
def get_music_folders():
    g.response.musicFolders = bindings.MusicFolders()
    g.response.musicFolders.append(
        bindings.MusicFolder(id=1, name='beets library'))
    return g.response


@rest_api.route('/getIndexes.view')
def get_indexes():
    g.response.indexes = bindings.Indexes()

    with g.lib.transaction() as tx:
        rows = tx.query("SELECT DISTINCT albumartist FROM albums")
    all_artists = [row[0] for row in rows]

    g.response.indexes.ignoredArticles = 'The El La Los Las Le Les'
    g.response.indexes.lastModified = 0
    return g.response


app = Flask(__name__)
app.response_class = SubsonicResponse
app.register_blueprint(rest_api, url_prefix='/rest')


def init_server(lib, opts, args):
    app.config['lib'] = lib
    app.run(debug=True)


beetsonic_cmd = Subcommand('sonic',
                           help='Run Subsonic server inteface for beets')
beetsonic_cmd.func = init_server


class BeetsonicServer(BeetsPlugin):
    def commands(self):
        return [beetsonic_cmd]
