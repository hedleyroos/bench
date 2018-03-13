import sys

from flask import Flask

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=int(sys.argv[2]), threaded=True)
