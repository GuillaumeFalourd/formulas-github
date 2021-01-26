#!/usr/bin/python3
import os

from formula import formula

user = os.environ.get("GIT_USERNAME")
key = os.environ.get("GIT_TOKEN")
contribution = os.environ.get("CONTRIBUTION")

formula.Run(user, key, contribution)
