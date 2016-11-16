import pyxb.utils.domutils
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from flask import Blueprint
from flask import Flask

from generated import api

pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(api.Namespace)

rest_api = Blueprint('rest_api', __name__)


@rest_api.route("/ping.view")
def ping():
    response = api.subsonic_response()
    response.version = api.Version('1.14.0')
    response.status = api.ResponseStatus.ok
    return response.toxml('utf-8'), 200, {'Content-Type': 'application/xml; charset=utf-8'}


app = Flask(__name__)
app.register_blueprint(rest_api, url_prefix='/rest')

def init_server(lib, opts, args):
    app.run(debug=True)
subsonic_cmd = Subcommand('subsonic', help='Run Subsonic server')
subsonic_cmd.func = init_server


class SubsonicServer(BeetsPlugin):
    def commands(self):
        return [subsonic_cmd]
