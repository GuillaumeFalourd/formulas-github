#!/usr/bin/python3
import os

from formula import formula

username = os.environ.get("GITHUB_USERNAME")
name = os.environ.get("RIT_NAME")
job = os.environ.get("RIT_JOB")
company = os.environ.get("RIT_COMPANY")

formula.Run(username, name, job, company)
