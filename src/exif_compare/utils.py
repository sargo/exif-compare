# -*- coding: utf-8 -*-
"""
Helper functions used in views.
"""

from json import dumps
from functools import wraps

from flask import Response


def jsonify(function):
    """
    Creates a response with the JSON representation of wrapped function result.
    """
    @wraps(function)
    def inner(*args, **kwargs):
        return Response(dumps(function(*args, **kwargs)),
                        mimetype='application/json')
    return inner
