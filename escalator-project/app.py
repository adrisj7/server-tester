#!/usr/bin/python

import sys
import datetime
import json

from flask import Flask, render_template, redirect, request

from flask_cors import CORS
#, g, render_template, redirect, request

# 5000 seems a bit... basic. Feel free to change later to something more
#      interesting.

SITE_PORT = 5000

# If testing on localhost, set to True
# Otherwise if running on server, set to False
SERVER_LOCAL = True

# Init app
app = Flask(__name__)

CORS(app)

# MAIN ESCALATOR STATES
isMoving1 = 0
isMoving2 = 0

lastUpdate = "never"

@app.route("/")
def route_default():
    return redirect("/home")

@app.route("/home")
def route_home():
    return render_template("home.html")

@app.route("/update", methods=["POST", "GET"])
def route_update():
    global isMoving1, isMoving2, lastUpdate
    
    data = request.form
    isMoving1 = data["state1"]
    isMoving2 = data["state2"]
    
    time = datetime.datetime.today()
    
    lastUpdate = "%s/%s/%s %s:%s:%s:%s" % (\
            time.month,
            time.day,
            time.year,
            time.hour,
            time.minute,
            time.second,
            time.microsecond)
    return "1"

@app.route("/getData")
def route_get_data():
    return json.dumps({"state1" : isMoving1, "state2" : isMoving2, "lastUpdate" : lastUpdate})


if __name__ == "__main__":
    if SERVER_LOCAL:
        host = "127.0.0.1"
    else:
        host = "0.0.0.0"
 

    app.run(host = host,
            port = SITE_PORT,
            debug = True
            )

