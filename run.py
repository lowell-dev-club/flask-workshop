# When not using repl.it most developers use run.py to run their flasks apps or import the flask app for use by a wgsi server or other form of running a flask app
from workshop import app

# Run Flask app
app.run(
    host='0.0.0.0', # host to view from outside the network
    port=5000, # assign to port 5000
    debug=True # Have debug pages show when there is an error
)
