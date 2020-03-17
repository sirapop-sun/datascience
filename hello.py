# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:19:40 2020

@author: sirapop.kon
"""

import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/greet/<name>")
def greet(name):
    return "Hello {}!".format(name)

if __name__ == "__main__":
    app.run()