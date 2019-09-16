# Imports
from workshop import app
from flask import render_template, redirect, url_for

# Views
# Creating a route always requires a "/". You can assign more then one route to certain template
# Assign request method to routes to control if users can post, delete, get etc.
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def index():
    # Render template renders webpage with data creating the dynamic webpage
    return render_template('index.html')

# python array containg any data a developer would like
array = ['Hello', 'World', "Dev Club", "Lowell!", "Free food!", "CODE", "PYTHON IS SUPERIOR"]

@app.route("/advanced", methods=['GET'])
def advanced():
    # Using Jinja and flasks ability to create dynamic webpages we pass in the array in to the Jinja template to use the data in the array on the webpage
    return render_template('advanced.html', array=array)

# Error Handelers
# You can create custom error pages for any html error codes
# 404 error handler returns 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
