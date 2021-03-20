#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GITHUB_TOKEN")
username = os.environ.get("RIT_GITHUB_USER")
repository = os.environ.get("RIT_GITHUB_REPO")
private = os.environ.get("RIT_REPO_PRIVACY")
clone = os.environ.get("RIT_CLONE")

formula.run(token, username, repository, private, clone)