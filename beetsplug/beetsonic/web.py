import json

import pyxb.utils.domutils
from flask import Blueprint
from flask import Flask
from flask import Response
from flask import request
from flask.views import View

import bindings

SUBSONIC_API_VERSION = '1.14.0'


class ResponseView(View):
    def __init__(self, generate_response_func=None):
        self.generate_response_func = generate_response_func
        self.response = bindings.subsonic_response()
        self.response.version = bindings.Version(SUBSONIC_API_VERSION)
        self.response.status = bindings.ResponseStatus.ok

    def dispatch_request(self):
        if self.generate_response_func:
            self.generate_response_func(self.response)
        return_format = request.args.get('f', 'xml')
        if return_format == 'json':
            content = json.dumps(self.response)
            mimetype = 'application/json'
        else:
            content = self.response.toxml('utf-8')
            mimetype = 'application/xml'
        return Response(content, mimetype=mimetype)


def create_blueprint(model):
    rest_api = Blueprint('rest_api', __name__)

    def ping(_):
        pass

    def get_licenses(response):
        response.license = bindings.License(valid=True)

    def get_music_folders(response):
        response.musicFolders = bindings.MusicFolders()
        response.musicFolders.append(
            bindings.MusicFolder(id=1, name='beets library'))

    def get_indexes(response):
        response.indexes = bindings.Indexes()
        response.indexes.ignoredArticles = 'The El La Los Las Le Les'
        response.indexes.lastModified = 0
        print(model.get_indexes())

    def route(end_point, generate_response_func):
        rest_api.add_url_rule(
            end_point,
            view_func=ResponseView.as_view(
                generate_response_func.__name__,
                generate_response_func=generate_response_func
            )
        )

    route('/ping.view', ping)
    route('/getLicenses.view', get_licenses)
    route('/getMusicFolders.view', get_music_folders)
    route('/getIndexes.view', get_indexes)

    return rest_api


class SubsonicServer(Flask):
    def __init__(self, model=None, *args, **kwargs):
        super(SubsonicServer, self).__init__(*args, **kwargs)

        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(
            bindings.Namespace)

        self.register_blueprint(create_blueprint(model), url_prefix='/rest')
