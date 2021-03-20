#!/usr/bin/python3
import requests
import json
import re
import os

def run(token, username, repository, private, clone):

    repository = urlify(repository)

    url = f"https://api.github.com/user/repos"

    data = {}
    data["name"] = repository
    data["description"] = "Project created with Ritchie CLI"
    data["homepage"] = "https://ritchiecli.io"
    data["auto_init"] = True
    if private == "No":
        data["private"] = False
    else:
        data["private"] = True

    json_data = json.dumps(data)

    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r = requests.post(
        url=url,
        data=json_data,
        headers=headers
        )

    if r.status_code == 201:
        print(f"✅ Repository successfully created on \033[36mhttps://github.com/{username}/{repository}\033[0m!")

        if clone == "Yes":
            os.system(f"git clone -q https://github.com/{username}/{repository}.git")
            print(f"✅ Repository successfully cloned on the \033[36mcurrent directory\033[0m!")

    else:
        print(f"❌ Couldn't create {username}'s new repository")
        print (r.status_code, r.reason)

def urlify(s):
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s\-]", '', s)
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)
    return s