#!/usr/bin/python3
'''state list end point'''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    '''states list end point'''
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    '''states list end point'''
    state = None
    for s_obj in storage.all(State).values():
        if s_obj.id == id:
            state = s_obj
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown_storage(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
