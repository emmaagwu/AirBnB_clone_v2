#!/usr/bin/python3
""" start a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    use the strict_slashes=False option
"""
from flask import Flask

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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python(text="is cool"):
    """ returns 'Python' followed by the content of the text
    Replaces any underscore in <text> with space
    """
    text_space = text.replace("_", " ")
    return "Python {}".format(text_space)


@app.route("/number/<int:n>", strict_slashes=False)
def show_n(n):
    """
        displays '<n> is a number' only if n is an integer
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
