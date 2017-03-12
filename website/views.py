from .app import app

from flask import g, abort, render_template

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<key>")
def download(key):
    if not g.db.exists(key):
        return render_template("404.html")

    d = g.db.hgetall(key)
    return render_template("download.html", key=key, **d)
