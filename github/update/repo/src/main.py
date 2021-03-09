#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GIT_TOKEN")
username = os.environ.get("RIT_GIT_USER")
default_branch = os.environ.get("RIT_DEFAULT_BRANCH")
repos = os.environ.get("RIT_REPOS")

formula.run(token, username, default_branch, repos)