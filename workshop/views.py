# Imports
from workshop import app
from flask import render_template, redirect, url_for

# Views
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("advanced", methods=['GET'])
def advanced():
    return render_template('advanced.html')

# Error Handelers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')