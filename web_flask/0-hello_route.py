#!/usr/bin/python3
""" scripts start a web app to listen on 0.0.0.0 port 5000. """i

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ returns 'Hello HBNB!' to the output"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
