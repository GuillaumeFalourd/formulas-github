#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GIT_TOKEN")
owner = os.environ.get("RIT_REPO_OWNER")
repository = os.environ.get("RIT_GIT_REPO")
branch = os.environ.get("RIT_REPO_BRANCH")
version = os.environ.get("RIT_REPO_VERSION")
description = os.environ.get("RIT_RELEASE_DESCRIPTION")

formula.run(token, owner, repository, branch, version, description)
