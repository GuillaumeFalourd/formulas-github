#!/usr/bin/python3
import requests
import json

def run(token, owner, repository, title, body):

    url = f"https://api.github.com/repos/{owner}/{repository}/issues"

    data = {}
    data["title"] = title
    data["body"] = body

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
        print(f"✅ Issue successfully created on \033[36mhttps://github.com/{owner}/{repository}\033[0m!")

    else:
        print(f"❌ Couldn't create new issue on \033[36mhttps://github.com/{owner}/{repository}")
        print (r.status_code, r.reason)
