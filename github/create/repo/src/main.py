#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GIT_TOKEN")
username = os.environ.get("RIT_GIT_USER")
repository = os.environ.get("RIT_GIT_REPO")
private = os.environ.get("RIT_REPO_PRIVACY")

formula.run(token, username, repository, private)