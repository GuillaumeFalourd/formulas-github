#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GITHUB_TOKEN")
owner = os.environ.get("RIT_REPO_OWNER")
repository = os.environ.get("RIT_GITHUB_REPO")
branch = os.environ.get("RIT_REPO_BRANCH")
default = os.environ.get("RIT_BRANCH_DEFAULT")

formula.run(token, owner, repository, branch, default)
