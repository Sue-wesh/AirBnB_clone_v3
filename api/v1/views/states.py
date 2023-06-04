#!/usr/bin/python3
""" handles all default RestFul API actions """
from api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from models.state import State
from models import storage



