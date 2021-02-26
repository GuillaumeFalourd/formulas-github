#!/usr/bin/python3
import requests
import json

def run(token, owner, repository, branch):
    url = f'https://api.github.com/repos/{owner}/{repository}'
    
    authorization = f'token {token}'
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    data = {}
    data['default_branch'] = branch
    
    json_data = json.dumps(data)
    
    r = requests.post(
        url=url,
        data=json_data,
        headers=headers
    )
        
    if r.status_code == 200:
        message = "✅ Branch \033[36m%s\033[0m successfully set as default on %s's \033[36m%s\033[0m repository" % (branch, owner, repository)
        print(message)

    else:
        print("❌ Couldn't set the branch as default on the repository")
        print (r.status_code, r.reason)
