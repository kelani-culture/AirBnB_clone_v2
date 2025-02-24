#!/usr/bin/python3
"run a simple flask app"
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    text = text.replace('_', ' ')
    return f"C {text}"


# @app.route('/python', strict_slashes=False)
# @app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text=None):
    if text:
        text = text.replace('_', ' ')
        return f"Python {text}"
    else:
        return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
