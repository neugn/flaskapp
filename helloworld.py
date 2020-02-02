#!/usr/bin/env python3

import sys
from flask import Flask

## init flask app
app = Flask(__name__)

@app.route("/")
def greetings(msg="hello world!"):
  return ">> %s <<" % msg

@app.route("/caps")
def allcaps(msg="hello world!"):
  return ">> %s <<" % msg.capitalize()

