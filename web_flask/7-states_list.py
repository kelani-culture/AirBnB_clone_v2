#!/usr/bin/python3
"""a list of all states"""
from flask import Flask, render_template
from models.__init__ import storage
from markupsafe import escape
import os
import subprocess

current_directory = os.getenv("PWD")
storage = None
executable_path = f"{current_directory}/dump_fix.sh"
storage_type = os.getenv("HBNB_TYPE_STORAGE")
app = Flask(__name__)
subprocess.run(['bash', 'dump_fix.sh', '7-dump.sql'])
if current_directory:
    import sys
    current_directory = current_directory.split('/')
    current_directory = current_directory[:-1]
    current_directory = '/'.join(current_directory)
    sys.path.append(current_directory)


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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


@app.route('/state_list', strict_slashes=False)
def state_list():
    states = storage.all('State')
    all_states = sorted(all_states.items(), key=lambda x: x[1].name)
    return render_template('7-states_list.html', states=all_states)


def remove_session():
    """teardown the current session"""
    storage.close()


app.teardown_appcontext(remove_session)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) 