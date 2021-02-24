#!/usr/bin/python3
import requests
import json

def run(token, owner, repository, branch, version, description):

    url = f'https://api.github.com/repos/{owner}/{repository}/releases'

    data = {}
    data['body'] = description
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
        message = "✅ Release %s successfully generated for %s's %s repository" % (version, owner, repository)
        print(message)

    else:
        print("❌ Couldn't generate repository release")
        print (r.status_code, r.reason)