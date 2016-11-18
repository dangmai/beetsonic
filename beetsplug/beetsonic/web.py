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


class ApiBlueprint(Blueprint):
    def route(self, rule, **options):
        def decorator(generate_response_func):
            self.add_url_rule(
                rule,
                view_func=ResponseView.as_view(
                    generate_response_func.__name__,
                    generate_response_func=generate_response_func
                )
            )
            return generate_response_func

        return decorator

    def error(self, code):
        def decorator(generate_response_func):
            self.register_error_handler(
                code,
                ResponseView.as_view(
                    generate_response_func.__name__,
                    generate_response_func=generate_response_func
                )
            )
            return generate_response_func

        return decorator


class SubsonicServer(Flask):
    def __init__(self, model, configs, *args, **kwargs):
        super(SubsonicServer, self).__init__(*args, **kwargs)

        pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(
            bindings.Namespace)

        api = ApiBlueprint('api', __name__)

        @api.error(403)
        def unauthenticated(response):
            create_error_response(
                response,
                errors.AUTHENTICATION_ERROR_CODE,
                errors.AUTHENTICATION_ERROR_MSG
            )

        def forbidden(response):
            create_error_response(
                response,
                errors.USER_NOT_AUTHORIZED_ERROR_CODE,
                errors.USER_NOT_AUTHORIZED_ERROR_MSG
            )

        @api.error(404)
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

        @api.route('/ping.view')
        def ping(_):
            pass

        @api.route('/getLicenses.view')
        def get_licenses(response):
            response.license = bindings.License(valid=True)

        @api.route('/getMusicFolders.view')
        def get_music_folders(response):
            response.musicFolders = bindings.MusicFolders()
            response.musicFolders.append(
                bindings.MusicFolder(id=1, name='beets library'))

        @api.route('/getIndexes.view')
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

            # Map the uppercased character to a list of album artists whose
            # names start with that character
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

        def _get_user():
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
            return user

        @api.route('/getUser.view')
        def get_user(response):
            if u'username' not in request.args:
                required_parameter_missing(response)
            elif request.args.get(u'username') != configs[u'username']:
                abort(404)
            else:
                response.user = _get_user()

        @api.route('/getUsers.view')
        def get_users(response):
            response.users = bindings.Users()
            response.users.append(_get_user())

        @api.route('/createUser.view')
        def create_user(response):
            forbidden(response)

        @api.route('/updateUser.view')
        def update_user(response):
            forbidden(response)

        @api.route('/deleteUser.view')
        def delete_user(response):
            forbidden(response)

        @api.route('/changePassword.view')
        def change_password(response):
            forbidden(response)

        @api.before_request
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

        self.register_blueprint(
            api,
            url_prefix='/rest'
        )
