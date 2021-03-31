#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GITHUB_TOKEN")
username = os.environ.get("RIT_GITHUB_USER")
repos = os.environ.get("RIT_REPOS")

formula.run(token, username, repos)
