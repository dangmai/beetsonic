import pyxb.utils.domutils
from flask import Blueprint
from flask import Flask
from flask import Response
from flask import g

import bindings

SUBSONIC_API_VERSION = '1.14.0'


class SubsonicHTTPResponse(Response):
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


def create_blueprint(model):
    rest_api = Blueprint('rest_api', __name__)

    @rest_api.before_request
    def init_response():
        g.response = bindings.subsonic_response()
        g.response.version = bindings.Version(SUBSONIC_API_VERSION)
        g.response.status = bindings.ResponseStatus.ok

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
        g.response.indexes.ignoredArticles = 'The El La Los Las Le Les'
        g.response.indexes.lastModified = 0
        print(model.get_indexes())
        return g.response

    return rest_api


class SubsonicServer(Flask):
    def __init__(self, model=None, *args, **kwargs):
        super(SubsonicServer, self).__init__(*args, **kwargs)

        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(
            bindings.Namespace)

        self.response_class = SubsonicHTTPResponse
        self.register_blueprint(create_blueprint(model), url_prefix='/rest')
