#!/usr/bin/python3
import os

from formula import formula

username = os.environ.get("RIT_GITHUB_USER")
name = os.environ.get("RIT_NAME")
job = os.environ.get("RIT_JOB")
company = os.environ.get("RIT_COMPANY")
linkedin_url = os.environ.get("RIT_LINKEDIN_URL")
twitter_url = os.environ.get("RIT_TWITTER_URL")
medium_url = os.environ.get("RIT_MEDIUM_URL")

formula.Run(username, name, job, company, linkedin_url, twitter_url, medium_url)
