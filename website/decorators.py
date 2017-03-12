from functools import wraps
from flask import jsonify

def json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return jsonify(f(*args, **kwargs))
    return wrapper
