import sys

import gevent.monkey
from gevent.pywsgi import WSGIServer

gevent.monkey.patch_all()

from flask import Flask


application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    gevent_server = WSGIServer(("0.0.0.0", int(sys.argv[2])), application)
    gevent_server.serve_forever()
