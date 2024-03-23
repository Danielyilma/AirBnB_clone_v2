#!/usr/bin/python3
'''displaying hbnb content'''
from flask import Flask, render_template
from models import storage, state, amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filter():
    states = storage.all(state.State)
    amenities = storage.all(amenity.Amenity)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
