#!/usr/bin/python3
import os

from formula import formula

token = os.environ.get("RIT_GITHUB_TOKEN")
owner = os.environ.get("RIT_GITHUB_OWNER")
repository = os.environ.get("RIT_GITHUB_REPO")
title = os.environ.get("RIT_ISSUE_TITLE")
body = os.environ.get("RIT_ISSUE_BODY")
labels = os.environ.get("RIT_ISSUE_LABELS")
assignees = os.environ.get("RIT_ISSUE_ASSIGNEES")

formula.run(token, owner, repository, title, body, labels, assignees)