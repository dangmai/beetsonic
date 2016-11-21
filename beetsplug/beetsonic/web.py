import hashlib
import json
from functools import wraps

import pyxb.utils.domutils
from flask import Blueprint
from flask import Flask
from flask import Response
from flask import abort
from flask import request
from flask import send_file
from flask.views import View
from flask_cors import CORS
from xmljson import yahoo

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
        content = self.response.toxml('utf-8')
        if return_format in ['json', 'jsonp']:
            # We'll turn the XML content into JSON content here
            obj = yahoo.data(utils.strip_xml_namespaces(content))
            if return_format == 'json':
                content = json.dumps(obj, indent=2)
                mimetype = 'application/json'
            else:
                content = json.dumps(obj)
                callback = request.args.get(u'callback', 'callback')
                content = callback + '(' + content + ')'
                mimetype = 'application/javascript'
        else:
            mimetype = 'text/xml'
        return Response(content, mimetype=mimetype)


class BinaryView(View):
    """
    Used for responses that contain binary data
    """

    def __init__(self, location_fn):
        self.location_fn = location_fn
        self.error_response = utils.create_subsonic_response(
            SUBSONIC_API_VERSION,
            bindings.ResponseStatus.failed
        )

    def dispatch_request(self, *args, **kwargs):
        location = self.location_fn(self.error_response)
        if isinstance(location, bindings.Response):
            # This is a convention we use to denote that there is an error
            content = location.toxml('utf-8')
            mimetype = 'text/xml'
            return Response(content, mimetype=mimetype)
        else:
            return send_file(location, as_attachment=True)


class ApiBlueprint(Blueprint):
    def __init__(self, model, configs, *args, **kwargs):
        super(ApiBlueprint, self).__init__(*args, **kwargs)
        self.model = model
        self.configs = configs

        self._set_up_error_handlers()
        self._set_up_routes(model, configs)

    def _set_up_error_handlers(self):
        self.register_error_handler(403, self.unauthenticated)
        self.register_error_handler(404, self.data_not_found)

    def _set_up_routes(self, model, configs):
        @self.route('/ping.view')
        def ping(_):
            pass

        @self.route('/getLicense.view')
        def get_licenses(response):
            response.license = bindings.License(valid=True)

        @self.route('/getMusicFolders.view')
        def get_music_folders(response):
            response.musicFolders = model.get_music_folders()

        @self.route('/getIndexes.view')
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
            # TODO get singletons as part of album if possible
            children = model.get_singletons()
            for child in children:
                indexes.append(child)
            response.indexes = indexes

        @self.route('/getUser.view')
        @self.require_arguments([u'username'])
        def get_user(response):
            if request.args.get(u'username') != configs[u'username']:
                abort(404)
            else:
                response.user = model.get_user(configs[u'username'])

        @self.route('/getUsers.view')
        def get_users(response):
            response.users = bindings.Users()
            response.users.append(model.get_user(configs[u'username']))

        @self.route('/getRandomSongs.view')
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

        @self.route('/getMusicDirectory.view')
        @self.require_arguments([u'id'])
        def get_music_directory(response):
            response.directory = model.get_music_directory(request.args[u'id'])

        # TODO contact MusicBrainz for artist information
        @self.route('/getArtistInfo.view')
        @self.require_arguments([u'id'])
        def get_artist_info(response):
            response.artistInfo = utils.create_artist_info()

        @self.route('/getLyrics.view')
        def get_lyrics(response):
            artist = None
            title = None
            if u'artist' in request.args:
                artist = request.args[u'artist']
            if u'title' in request.args:
                title = request.args[u'title']
            response.lyrics = model.get_lyrics(artist, title)

        @self.route('/getGenres.view')
        def get_genres(response):
            response.genres = model.get_genres()

        # TODO handle sizing request
        @self.route_binary('/getCoverArt.view')
        @self.require_arguments([u'id'])
        def get_cover_art(error_response):
            object_id = request.args.get(u'id')
            location = model.get_cover_art(object_id)
            if not location:
                self.data_not_found(error_response)
                return error_response
            return location

        # TODO transcode the music
        @self.route_binary('/stream.view')
        @self.require_arguments([u'id'])
        def stream(error_response):
            id = request.args.get(u'id')
            try:
                return model.get_song_location(id)
            except ValueError:
                self.data_not_found(error_response)
                return error_response

        @self.route_binary('/download.view')
        @self.require_arguments([u'id'])
        def download(error_response):
            id = request.args.get('id')
            try:
                return model.get_song_location(id)
            except ValueError:
                self.data_not_found(error_response)
                return error_response

        self.add_common_errors({
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
        }, self.forbidden)

        @self.before_request
        def check_version():
            if 'v' not in request.args:
                abort(403)
            client_version = request.args.get('v')
            client_version_parts = map(int, client_version.split('.'))
            server_version_parts = map(int, SUBSONIC_API_VERSION.split('.'))
            if client_version_parts[0] > server_version_parts[0]:
                return ResponseView(self.server_upgrade).dispatch_request()
            elif client_version_parts[0] < server_version_parts[0]:
                return ResponseView(self.client_upgrade).dispatch_request()
            elif client_version_parts[1] > server_version_parts[1]:
                return ResponseView(self.server_upgrade).dispatch_request()

        @self.before_request
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

    @staticmethod
    def create_error_response(response, code, message):
        response.status = bindings.ResponseStatus.failed
        response.error = bindings.Error(code=code, message=message)

    def unauthenticated(self, response):
        self.create_error_response(
            response,
            errors.AUTHENTICATION_ERROR_CODE,
            errors.AUTHENTICATION_ERROR_MSG
        )

    def forbidden(self, response):
        self.create_error_response(
            response,
            errors.USER_NOT_AUTHORIZED_ERROR_CODE,
            errors.USER_NOT_AUTHORIZED_ERROR_MSG
        )

    def data_not_found(self, response):
        self.create_error_response(
            response,
            errors.DATA_NOT_FOUND_ERROR_CODE,
            errors.DATA_NOT_FOUND_ERROR_MSG
        )

    def required_parameter_missing(self, response):
        self.create_error_response(
            response,
            errors.REQUIRED_PARAMETER_ERROR_CODE,
            errors.REQUIRED_PARAMETER_ERROR_MSG
        )

    def client_upgrade(self, response):
        self.create_error_response(
            response,
            errors.CLIENT_UPGRADE_ERROR_CODE,
            errors.CLIENT_UPGRADE_ERROR_MSG
        )

    def server_upgrade(self, response):
        self.create_error_response(
            response,
            errors.SERVER_UPGRADE_ERROR_CODE,
            errors.SERVER_UPGRADE_ERROR_MSG
        )

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

    def require_arguments(self, arguments):
        """
        Decorator to check whether the arguments required are sent from the
        client or not. Must be inside a route.
        :param arguments: The arguments required.
        :return: The decorated function.
        """

        def decorator(f):
            @wraps(f)
            def decorated_function(response, *args, **kwargs):
                for argument in arguments:
                    if argument not in request.args:
                        self.required_parameter_missing(response)
                        return response
                return f(response, *args, **kwargs)

            return decorated_function

        return decorator

    def register_error_handler(self, code_or_exception, f):
        """
        Override Blueprint method to use ResponseView.
        :param code_or_exception: Code or exception to catch.
        :param f: Function to use in ResponseView.
        :return: None
        """
        super(ApiBlueprint, self).register_error_handler(
            code_or_exception,
            ResponseView.as_view(
                f.__name__,
                generate_response_func=f
            )
        )

    def add_common_errors(self, rule_map, generate_response_func):
        """
        There are endpoints that we won't implement, because beets doesn't
        have the tools to handle them. For those endpoints, we use this method
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

        api = ApiBlueprint(model, configs, 'api', __name__)

        self.register_blueprint(api, url_prefix='/rest')
        if configs['cors']:
            CORS(self, resources={r"/*": {"origins": configs['cors']}})
