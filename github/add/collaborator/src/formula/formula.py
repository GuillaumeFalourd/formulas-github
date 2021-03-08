#!/usr/bin/python3
import requests
import json

def run(token, username, repository, collaborator):
    url = f"https://api.github.com/repos/{username}/{repository}/collaborators/{collaborator}"

    data = {}
    data["permission"] = "push"

    json_data = json.dumps(data)

    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r = requests.put(
        url=url,
        data=json_data,
        headers=headers
        )

    if r.status_code == 201:
        print(f"✅ Collaborator \033[36m{collaborator}\033[0m successfully added to {username}'s \033[36m{repository}\033[0m repository")

    else:
        print("❌ Couldn't add the collaborator to the repository")
        print (r.status_code, r.reason)
