#!/usr/bin/python3
'''flask application'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route('/<name>', strict_slashes=False)
def hello(name=None):
    '''root route handle'''
    return f'HBNB' if name else f'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
