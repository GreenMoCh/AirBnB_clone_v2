#!/usr/bin/python3
"""States and State"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy session after each request"""
    storage.close()

@app.route('/states', strict_slashes=False)
def states():
    """Displays a list of all state objects"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Displays a State and its cities"""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)