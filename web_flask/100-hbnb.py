#!/usr/bin/python3
'''displaying web content'''
from flask import Flask, render_template
from models import storage, amenity, state, place


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(state.State)
    amenities = storage.all(amenity.Amenity)
    places = storage.all(place.Place)
    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
