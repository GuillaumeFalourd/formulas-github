#!/usr/bin/python3
import requests
import json

def run(token, username, repository, branch, version):

    url = f'https://api.github.com/repos/{username}/{repository}/releases'

    data = {}
    data['body'] = 'Release generated automatically using Ritchie CLI'
    data['target_commitish'] = branch
    data['tag_name'] = version
    data['name'] = version
    json_data = json.dumps(data)

    authorization = f'token {token}'
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
        message = "Release %s successfully generated for %s repository" % (version, repository)
        print(message)

    else:
        print("Couldn't generate repository release")
        print (r.status_code, r.reason)