from flask import g, request
import hashlib
import uuid

from .app import app
from .decorators import json

get_hash = lambda: hashlib.md5(uuid.uuid4().bytes).hexdigest()[:12]

@app.route("/api/v1/create", methods=['POST'])
@json
def api_v1_create():
    if 'magnet' not in request.form or 'name' not in request.form:
        return {"error": "bad_request"}

    h = get_hash()
    props = {
        'magnet': request.form['magnet'],
        'name':   request.form['name']
    }
    g.db.hmset(h, props)

    return {
        'key': h
    }
