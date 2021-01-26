#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GIT_USER")
key = os.environ.get("RIT_GIT_TOKEN")
login = os.environ.get("RIT_USER_LOGIN")

formula.run(user, key, login)
