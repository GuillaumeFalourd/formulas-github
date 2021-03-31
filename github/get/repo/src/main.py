#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GITHUB_USER")
key = os.environ.get("RIT_GITHUB_TOKEN")
repo_url = os.environ.get("RIT_GITHUB_REPOSITORY_URL")
contribution = os.environ.get("CONTRIBUTION")

formula.run(user, key, repo_url, contribution)
