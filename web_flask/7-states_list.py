#!/usr/bin/python3
"""List of states"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy session after each request"""
    storage.close()

@app.route('/state_list', strict_slashes=False)
def state_list():
    """Displays a list of all state objects sorted by name"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)