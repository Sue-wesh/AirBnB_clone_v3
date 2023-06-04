#!/usr/bin/python3
"""index.py file"""

from api.v1.views import app_views


@app_views.route('/status')
def status():
    """returns JSON : "status": "OK" """
    return (jsonify({'status': 'OK'}), 200)


@app_views.route('/stats')
def stats():
    """ retrieves the number of each object by type """
    classes = {"amenities": storage.count(Amenity),
               "cities": storage.count(City),
               "places": storage.count(Place),
               "reviews": storage.count(Review),
               "states": storage.count(State),
               "users": storage.count(User)}
    return (jsonify(classes))
