from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


def init_server(lib, opts, args):
    app.run(debug=True)
subsonic_cmd = Subcommand('subsonic', help='Run Subsonic server')
subsonic_cmd.func = init_server


class SubsonicServer(BeetsPlugin):
    def commands(self):
        return [subsonic_cmd]
