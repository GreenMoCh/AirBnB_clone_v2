#!/usr/bin/python3
"""HBNB filters"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy session after each request"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all("State")
    aminities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states, aminities=aminities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)