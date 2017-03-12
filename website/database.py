from flask import g
from redis import StrictRedis
import os

from .app import app

@app.before_request
def connect_db():
    g.db = StrictRedis.from_url(os.environ['REDIS_URL'], db=1, decode_responses=True)
