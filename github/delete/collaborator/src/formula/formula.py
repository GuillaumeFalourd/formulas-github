#!/usr/bin/python3
import requests
import json

def run(token, username, repository, collaborator):

    url = f"https://api.github.com/repos/{username}/{repository}/collaborators/{collaborator}"

    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r1 = requests.get(
        url=url,
        headers=headers
        )

    if r1.status_code == 204:

        r2 = requests.delete(
            url=url,
            headers=headers
            )

        if r2.status_code == 204:
            print(f"✅ Collaborator \033[36m{collaborator}\033[0m successfully removed from {username}'s \033[36m{repository}\033[0m repository")

        else:
            print("❌ Couldn't delete the collaborator from the repository")
            print (r2.status_code, r2.reason)

    else:
        print(f"⚠️ Username \033[36m{collaborator}\033[0m isn't a \033[36m{repository}\033[0m repository collaborator")
