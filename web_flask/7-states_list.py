"""a list of all states"""
#!/usr/bin/python3
from flask import Flask, render_template
from models.__init__ import storage


app = Flask(__name__)


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