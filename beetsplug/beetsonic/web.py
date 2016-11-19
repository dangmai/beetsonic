import hashlib
import json

import pyxb.utils.domutils
from flask import Blueprint
from flask import Flask
from flask import Response
from flask import abort
from flask import request
from flask import send_file
from flask.views import View

import bindings
from beetsplug.beetsonic import errors
from beetsplug.beetsonic import utils

SUBSONIC_API_VERSION = u'1.14.0'


class ResponseView(View):
    """
    Used for common responses that contain the API results
    """
    def __init__(self, generate_response_func=None):
        self.generate_response_func = generate_response_func
        self.response = utils.create_subsonic_response(SUBSONIC_API_VERSION)

    def dispatch_request(self, *args, **kwargs):
        if self.generate_response_func:
            self.generate_response_func(self.response)
        return_format = request.args.get('f', 'xml')
        if return_format == 'json':
            content = json.dumps(self.response)
            mimetype = 'application/json'
        else:
            content = self.response.toxml('utf-8')
            mimetype = 'text/xml'
        return Response(content, mimetype=mimetype)


class BinaryView(View):
    """
    Used for responses that contain binary data
    """

    def __init__(self, location_fn):
        self.location_fn = location_fn

    def dispatch_request(self, *args, **kwargs):
        location = self.location_fn()
        print(location)
        if isinstance(location, bindings.Response):
            # This is a convention we use to denote that there is an error
            content = location.toxml('utf-8')
            mimetype = 'text/xml'
            return Response(content, mimetype=mimetype)
        else:
            return send_file(location)


class ApiBlueprint(Blueprint):
    def route(self, rule, **options):
        """
        Custom route decorator for the API Blueprint
        :param rule: The URL rule for this route
        :param options: The options kwargs
        :return: The decorated function
        """
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

    def route_binary(self, rule, **options):
        """
        Custom route_binary decorator for the API Blueprint
        :param rule: The URL rule for this route
        :param options: The options kwargs
        :return: The decorated function
        """

        def decorator(location_fn):
            self.add_url_rule(
                rule,
                view_func=BinaryView.as_view(
                    location_fn.__name__,
                    location_fn=location_fn
                )
            )
            return location_fn

        return decorator

    def error(self, code):
        """
        Custom error decorator for the API Blueprint
        :param code: The HTTP error code to handle
        :return: The decorated function
        """
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

    def add_common_errors(self, rule_map, generate_response_func):
        """
        There are endpoints that we won't implement, because beets doesn't
        have the tool to handle them. For those endpoints, we use this method
        to make sure they return correct the correct error response.
        :param rule_map: Map of the URL rule to the function name used by Flask
        :param generate_response_func: Function used to generate the response
        :return: None
        """
        for rule, route_fn in rule_map.iteritems():
            self.add_url_rule(
                rule,
                view_func=ResponseView.as_view(
                    route_fn,
                    generate_response_func=generate_response_func
                )
            )


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

        def client_upgrade(response):
            create_error_response(
                response,
                errors.CLIENT_UPGRADE_ERROR_CODE,
                errors.CLIENT_UPGRADE_ERROR_MSG
            )

        def server_upgrade(response):
            create_error_response(
                response,
                errors.SERVER_UPGRADE_ERROR_CODE,
                errors.SERVER_UPGRADE_ERROR_MSG
            )

        def create_error_response(response, code, message):
            response.status = bindings.ResponseStatus.failed
            response.error = bindings.Error(code=code, message=message)

        @api.route('/ping.view')
        def ping(_):
            pass

        @api.route('/getLicense.view')
        def get_licenses(response):
            response.license = bindings.License(valid=True)

        @api.route('/getMusicFolders.view')
        def get_music_folders(response):
            response.musicFolders = model.get_music_folders()

        @api.route('/getIndexes.view')
        def get_indexes(response):
            if_modified_since = request.args.get('ifModifiedSince', 0)
            last_modified = model.get_last_modified()
            if last_modified <= if_modified_since:
                return

            album_artists = model.get_album_artists()
            indexes = utils.create_indexes(album_artists,
                                           configs['ignoredArticles'])
            indexes.lastModified = last_modified

            # Get items without albums
            children = model.get_singletons()
            for child in children:
                indexes.append(child)
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

        @api.route('/getRandomSongs.view')
        def get_random_songs(response):
            size = request.args.get('size', 10)
            if size < 0:
                size = 0
            elif size > 500:
                size = 500
            genre = request.args.get('genre', None)
            from_year = request.args.get('fromYear', None)
            to_year = request.args.get('toYear', None)
            music_folder_id = request.args.get('musicFolderId', None)
            response.randomSongs = model.get_random_songs(size, genre,
                                                          from_year, to_year,
                                                          music_folder_id)

        @api.route_binary('/stream.view')
        def stream():
            error_response = utils.create_subsonic_response(
                SUBSONIC_API_VERSION,
                bindings.ResponseStatus.failed
            )

            if 'id' not in request.args:
                required_parameter_missing(error_response)
                return error_response
            id = request.args.get('id')
            try:
                return model.get_song_location(id)
            except ValueError:
                data_not_found(error_response)
                return error_response

        api.add_common_errors({
            '/createUser.view': 'create_user',
            '/updateUser.view': 'update_user',
            '/deleteUser.view': 'delete_user',
            '/changePassword.view': 'change_password',
            '/createPlaylist.view': 'create_playlist',
            '/updatePlaylist.view': 'update_playlist',
            '/deletePlaylist.view': 'delete_playlist',
            '/star.view': 'star',
            '/unstar.view': 'unstar',
            '/setRating.view': 'set_rating',
            '/scrobble.view': 'scrobble',
            '/createShare.view': 'create_share',
            '/updateShare.view': 'update_share',
            '/deleteShare.view': 'delete_share',
            '/refreshPodcasts.view': 'refresh_podcasts',
            '/createPodcastChannel.view': 'create_podcast_channel',
            '/deletePodcastChannel.view': 'delete_podcast_channel',
            '/deletePodcastEpisode.view': 'delete_podcast_episode',
            '/downloadPodcastEpisode.view': 'download_podcast_episode',
            '/jukeboxControl.view': 'jukebox_control',
            '/addChatMessage.view': 'add_chat_message',
            '/createBookmark.view': 'create_bookmark',
            '/deleteBookmark.view': 'delete_bookmark',
        }, forbidden)

        @api.before_request
        def check_version():
            if 'v' not in request.args:
                abort(403)
            client_version = request.args.get('v')
            client_version_parts = map(int, client_version.split('.'))
            server_version_parts = map(int, SUBSONIC_API_VERSION.split('.'))
            if client_version_parts[0] > server_version_parts[0]:
                return ResponseView(server_upgrade).dispatch_request()
            elif client_version_parts[0] < server_version_parts[0]:
                return ResponseView(client_upgrade).dispatch_request()
            elif client_version_parts[1] > server_version_parts[1]:
                return ResponseView(server_upgrade).dispatch_request()

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
                if received_token != expected_token:
                    abort(403)
            else:
                abort(403)

        self.register_blueprint(
            api,
            url_prefix='/rest'
        )
