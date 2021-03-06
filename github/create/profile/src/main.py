#!/usr/bin/python3
import os

from formula import formula

username = os.environ.get("RIT_GITHUB_USER")
name = os.environ.get("RIT_NAME")
job = os.environ.get("RIT_JOB")
company = os.environ.get("RIT_COMPANY")
hardskills = os.environ.get("RIT_HARD_SKILLS")
accounts = os.environ.get("RIT_ACCOUNTS")

formula.run(username, name, job, company, hardskills, accounts)
