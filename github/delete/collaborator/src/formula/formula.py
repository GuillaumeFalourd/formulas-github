#!/usr/bin/python3
import requests
import json

def run(token, username, repository, collaborator):

    authorization = f'token {token}'
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    url = f'  https://api.github.com/repos/{username}/{repository}/collaborators{collaborator}'

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
                message = "Collaborator %s successfully removed from %s repository" % (collaborator, repository)
                print(message)

            else:
                print("Couldn't delete the collaborator from the repository")
                print (r2.status_code, r2.reason)

    else:
        message = "Username %s isn't a %s repository collaborator" % (collaborator, repository)
        print(message)
