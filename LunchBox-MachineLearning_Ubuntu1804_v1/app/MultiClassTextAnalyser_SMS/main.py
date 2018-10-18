from flask import Flask
from flask import request

app = Flask(__name__)

from .core import app_setup


if __name__ == "__main__":
    # Only for debugging while developing
    #app.run(host='0.0.0.0', debug=False, port=8085)
    app.run()
