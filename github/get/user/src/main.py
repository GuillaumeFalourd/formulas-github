#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GIT_USER")
key = os.environ.get("RIT_GIT_TOKEN")
username = os.environ.get("GITHUB_USERNAME")
repo_details = os.environ.get("REPO_DETAILS")
keep_file = os.environ.get("KEEP_FILE")

formula.Run(username, repo_details, keep_file, user, key)
