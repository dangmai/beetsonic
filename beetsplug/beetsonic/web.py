import hashlib
import json

import pyxb.utils.domutils
from flask import Blueprint
from flask import Flask
from flask import Response
from flask import abort
from flask import request
from flask.views import View

import bindings
from beetsplug.beetsonic import errors

SUBSONIC_API_VERSION = '1.14.0'


class ResponseView(View):
    def __init__(self, generate_response_func=None):
        self.generate_response_func = generate_response_func
        self.response = bindings.subsonic_response()
        self.response.version = bindings.Version(SUBSONIC_API_VERSION)
        self.response.status = bindings.ResponseStatus.ok

    def dispatch_request(self, *args, **kwargs):
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


def create_blueprint(model, configs):
    rest_api = Blueprint('rest_api', __name__)

    def unauthorized(response):
        create_error_response(
            response,
            errors.AUTHENTICATION_ERROR_CODE,
            errors.AUTHENTICATION_ERROR_MSG
        )

    def data_not_found(response):
        create_error_response(
            response,
            errors.DATA_NOT_FOUND_ERROR_CODE,
            errors.DATA_NOT_FOUND_ERROR_MSG
        )

    def required_parameter_missing(response):
        create_error_response(
            response,
            errors.REQUIRED_PARAMETER_ERROR_CODE,
            errors.REQUIRED_PARAMETER_ERROR_MSG
        )

    def create_error_response(response, code, message):
        response.status = bindings.ResponseStatus.failed
        response.error = bindings.Error(code=code, message=message)

    def ping(_):
        pass

    def get_licenses(response):
        response.license = bindings.License(valid=True)

    def get_music_folders(response):
        response.musicFolders = bindings.MusicFolders()
        response.musicFolders.append(
            bindings.MusicFolder(id=1, name='beets library'))

    def get_indexes(response):
        if_modified_since = request.args.get('ifModifiedSince', 0)
        last_modified = model.get_last_modified()
        if last_modified <= if_modified_since:
            return

        indexes = bindings.Indexes()
        # TODO implement ignoredArticles functionality
        indexes.ignoredArticles = configs['ignoredArticles']
        indexes.lastModified = last_modified
        album_artists = model.get_album_artists()

        def index_func(map, item):
            first_char = item[:1].upper()
            if first_char not in map:
                map[first_char] = []
            map[first_char].append(item)
            return map

        # Map the uppercased character to a list of album artists whose names
        # start with that character
        char_map = reduce(
            index_func,
            album_artists,
            dict()
        )
        for char, artists in sorted(char_map.iteritems()):
            index = bindings.Index(name=char)
            for artist in artists:
                index.append(bindings.Artist(id=artist, name=artist))
            indexes.append(index)

        # Get items without albums
        children = model.get_singletons()
        for child in children:
            indexes.append(
                bindings.Child(
                    isDir=False,
                    id=child.id,
                    title=child.title,
                    artist=child.artist
                )
            )
        response.indexes = indexes

    def get_user(response):
        if u'username' not in request.args:
            required_parameter_missing(response)
        elif request.args.get(u'username') != configs[u'username']:
            abort(404)
        else:
            user = bindings.User(
                username=configs[u'username'],
                scrobblingEnabled=False,
                adminRole=True,
                settingsRole=False,
                downloadRole=True,
                uploadRole=False,
                playlistRole=True,
                coverArtRole=True,
                commentRole=False,
                podcastRole=False,
                streamRole=True,
                jukeboxRole=False,
                shareRole=False,
                videoConversionRole=False,
            )
            user.append(1)  # beets music folder id
            response.user = user

    @rest_api.before_request
    def authenticate():
        if 'u' not in request.args:
            abort(403)
        username = request.args.get('u')
        if username != configs[u'username']:
            abort(403)

        if 'p' in request.args:
            password = request.args.get('p')
            if password.startswith(u'enc:'):
                # It is hex encoded
                password = bytearray.fromhex(password[4:]).decode()
            if password != configs[u'password']:
                abort(403)
        elif 't' in request.args and 's' in request.args:
            salt = request.args.get('s')
            received_token = request.args.get('t')
            message = hashlib.md5()
            message.update(configs[u'password'] + salt)
            expected_token = message.hexdigest()
            print(received_token)
            print(expected_token)
            if received_token != expected_token:
                abort(403)
        else:
            abort(403)

    def error(code, generate_response_func):
        rest_api.register_error_handler(
            code,
            ResponseView.as_view(
                generate_response_func.__name__,
                generate_response_func=generate_response_func
            )
        )

    def route(end_point, generate_response_func):
        rest_api.add_url_rule(
            end_point,
            view_func=ResponseView.as_view(
                generate_response_func.__name__,
                generate_response_func=generate_response_func
            )
        )

    error(403, unauthorized)
    error(404, data_not_found)
    route('/ping.view', ping)
    route('/getLicenses.view', get_licenses)
    route('/getMusicFolders.view', get_music_folders)
    route('/getIndexes.view', get_indexes)
    route('/getUser.view', get_user)

    return rest_api


class SubsonicServer(Flask):
    def __init__(self, model, configs, *args, **kwargs):
        super(SubsonicServer, self).__init__(*args, **kwargs)

        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(
            bindings.Namespace)

        self.register_blueprint(
            create_blueprint(model, configs),
            url_prefix='/rest'
        )
