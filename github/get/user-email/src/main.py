#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GITHUB_USER")
key = os.environ.get("RIT_GITHUB_TOKEN")
login = os.environ.get("RIT_USER_LOGIN")

formula.run(user, key, login)
