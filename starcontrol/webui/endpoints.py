from flask import render_template
from .. import app

@app.route("/")
def home():
    return render_template("layout.html")

@app.route("/starmap/")
def starmap():
    return render_template("starmap.html")
