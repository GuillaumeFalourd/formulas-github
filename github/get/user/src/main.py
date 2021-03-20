#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("RIT_GITHUB_USER")
key = os.environ.get("RIT_GITHUB_TOKEN")
username = os.environ.get("RIT_GITHUB_USERNAME")
repo_details = os.environ.get("RIT_REPO_DETAILS")
keep_file = os.environ.get("RIT_KEEP_FILE")

formula.Run(user, key, username, repo_details, keep_file)
