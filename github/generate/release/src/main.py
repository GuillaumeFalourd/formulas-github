#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GIT_TOKEN")
username = os.environ.get("RIT_GIT_USER")
repository = os.environ.get("RIT_GIT_REPO")
branch = os.environ.get("RIT_REPO_BRANCH")
version = os.environ.get("RIT_REPO_VERSION")

formula.run(token, username, repository, branch, version)
