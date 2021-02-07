#!/usr/bin/python3
import requests
import re

def run(token, username, repository):

    repository = urlify(repository)

    url = f'https://api.github.com/repos/{username}/{repository}'

    authorization = f'token {token}'
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r = requests.delete(
        url=url,
        headers=headers
        )

    if r.status_code == 204:
        message = "Repository https://github.com/%s/%s successfully deleted!" % (username, repository)
        print(message)

    else:
        print("Couldn't delete repository https://github.com/%s/%s" % (username, repository))
        print (r.status_code, r.reason)

def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s\-]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s
