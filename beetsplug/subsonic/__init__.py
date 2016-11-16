from functools import wraps

import pyxb.utils.domutils
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from flask import Blueprint
from flask import Flask
from flask import Response

from generated import api

pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(api.Namespace)


class SubsonicResponse(Response):
    def __init__(self, content=None, *args, **kwargs):
        if isinstance(content, api.Response):
            kwargs['mimetype'] = 'application/xml'
            content = content.toxml('utf-8')
        super(Response, self).__init__(content, *args, **kwargs)

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, api.Response):
            return cls(response)
        return super(Response, cls).force_type(response, environ)


def subsonic(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        response = api.subsonic_response()
        response.version = api.Version('1.14.0')
        response.status = api.ResponseStatus.ok
        return func(response, *args, **kwargs)

    return decorated_function


rest_api = Blueprint('rest_api', __name__)


@rest_api.route("/ping.view")
@subsonic
def ping(response):
    return response


app = Flask(__name__)
app.response_class = SubsonicResponse
app.register_blueprint(rest_api, url_prefix='/rest')


def init_server(lib, opts, args):
    app.run(debug=True)


subsonic_cmd = Subcommand('subsonic', help='Run Subsonic server')
subsonic_cmd.func = init_server


class SubsonicServer(BeetsPlugin):
    def commands(self):
        return [subsonic_cmd]
