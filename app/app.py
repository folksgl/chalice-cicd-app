""" Sample Chalice "hello world" application """
from chalice import Chalice

# Chalice currently requires app.py to have 'app' (lowercase) available
# The app_name should match the value found in app/.chalice/config.json
app = Chalice(app_name="app")


@app.route("/")
def index():
    """ Index page for the hello world api """
    return {"hello": "world"}


@app.route("/hello/{name}")
def hello_name(name):
    """ Sample route for returning names """
    return {"hello": name}


# See https://aws.github.io/chalice/index.html for more examples
