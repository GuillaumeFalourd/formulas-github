#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GIT_TOKEN")
username = os.environ.get("RIT_GIT_USER")

formula.run(token, username)
