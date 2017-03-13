#!/usr/bin/python

import sys


from flask import Flask, render_template, redirect 
#, g, render_template, redirect, request

# 5000 seems a bit... basic. Feel free to change later to something more
#      interesting.

SITE_PORT = 5000

# If testing on localhost, set to True
# Otherwise if running on server, set to False
SERVER_LOCAL = False

# Init app
app = Flask(__name__)

# MAIN ESCALATOR STATE
isMoving = False

@app.route("/")
def route_default():
    return redirect("/home")

@app.route("/home")
def route_home():
    return render_template("home.html")

@app.route("/update", methods=["POST"])
def route_update():
    data = request.form
    isMoving = data["state"]

@app.route("/getData")
def route_get_data():
    return str({"state" : isMoving})


if __name__ == "__main__":
    if SERVER_LOCAL:
        host = "127.0.0.1"
    else:
        host = "0.0.0.0"
 

    app.run(host = host,
            port = SITE_PORT,
            debug = True
            )

