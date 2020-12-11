""" Sample Chalice "hello world" application """
from chalice import Chalice

APP = Chalice(app_name="app")


@APP.route("/")
def index():
    """ Index page for the hello world api """
    return {"hello": "world"}


@APP.route("/hello/{name}")
def hello_name(name):
    """ Sample route for returning names """
    return {"hello": name}


# See https://aws.github.io/chalice/index.html for more examples
