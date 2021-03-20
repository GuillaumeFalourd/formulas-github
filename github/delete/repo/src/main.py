#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GITHUB_TOKEN")
username = os.environ.get("RIT_GITHUB_USER")

formula.run(token, username)
