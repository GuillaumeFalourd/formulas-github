#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GITHUB_USER")
key = os.environ.get("RIT_GITHUB_TOKEN")
repository = os.environ.get("RIT_GITHUB_REPOSITORY")
contribution = os.environ.get("CONTRIBUTION")

formula.Run(user, key, repository, contribution)

