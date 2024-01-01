#!/usr/bin/python3
"""C is fun!"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles requests to the root url"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Handles requests to the /hbnb url"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Handles requests to the /c/<text> url"""
    return 'C {}'.format(text.replace('_',' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)