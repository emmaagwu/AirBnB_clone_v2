#!/usr/bin/python3
""" start a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
    use the strict_slashes=False option
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Returns 'Hello HBNB' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    """ returns 'C' followed by the content of the text """
    text_space = text.replace("_", " ")
    return "C {}".format(text_space)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
