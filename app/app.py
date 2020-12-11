""" Sample Chalice "hello world" application """
import json
from chalice import Chalice

with open(".chalice/config.json") as config_file:
    CONFIG = json.load(config_file)
    print(json.dumps(CONFIG))

if "app_name" not in CONFIG:
    raise KeyError("No 'app_name' configured in app/.chalice/config.json")

APP_NAME = CONFIG.get("app_name")

# Chalice currently requires app.py to have 'app' (lowercase) available
app = Chalice(app_name=APP_NAME)


@app.route("/")
def index():
    """ Index page for the hello world api """
    return {"hello": "world"}


@app.route("/hello/{name}")
def hello_name(name):
    """ Sample route for returning names """
    return {"hello": name}


# See https://aws.github.io/chalice/index.html for more examples
