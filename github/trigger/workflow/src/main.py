#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GITHUB_USER")
key = os.environ.get("RIT_GITHUB_TOKEN")
repo_owner = os.environ.get("RIT_GITHUB_REPOSITORY_OWNER")
repo_name = os.environ.get("RIT_GITHUB_REPOSITORY_NAME")
workflow_type = os.environ.get("RIT_WORKFLOW_TYPE")

formula.Run(user, key, repo_owner, repo_name, workflow_type)
