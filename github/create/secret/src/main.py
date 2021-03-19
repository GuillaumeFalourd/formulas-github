#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GIT_TOKEN")
owner = os.environ.get("RIT_REPO_OWNER")
repository = os.environ.get("RIT_GIT_REPO")
secret_name = os.environ.get("RIT_SECRET_NAME")
secret_value = os.environ.get("RIT_SECRET_VALUE")

formula.run(token, owner, repository, secret_name, secret_value)