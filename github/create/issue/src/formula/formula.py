#!/usr/bin/python3
import requests
import json
import sys
import re

def run(token, owner, repository, title, body, labels, assignees):

    url = f"https://api.github.com/repos/{owner}/{repository}/issues"

    data = {}
    data["title"] = title
    data["body"] = body
    
    if labels not in (None, ''):
        label_list = format(labels)
        data["labels"] = label_list
    
    if assignees not in (None, ''):
        assignees_list = format(assignees)
        data["assignees"] = assignees_list

    json_data = json.dumps(data)

    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }
    
    r1 = requests.get(
        url=url,
        headers=headers
        )
    
    if r1.status_code == 200:
        issues = r1.json()
        
        for issue in issues:
            if issue["title"] == title:
                print (f"👀 Issue with the same title already exists on \033[36mhttps://github.com/{owner}/{repository}\033[0m!")
                print("Please, update the ISSUE title.")
                sys.exit()   
            if issue["body"] == body:
                print (f"👀 Issue with the same description already exists on \033[36mhttps://github.com/{owner}/{repository}\033[0m!")
                print("Please, update the ISSUE description.")
                sys.exit()       

        r2 = requests.post(
            url=url,
            data=json_data,
            headers=headers
            )

        if r2.status_code == 201:
            print(f"✅ Issue successfully created on \033[36mhttps://github.com/{owner}/{repository}\033[0m!")

        else:
            print(f"❌ Couldn't create new issue on \033[36mhttps://github.com/{owner}/{repository}")
            print (r2.status_code, r2.reason, r2.content)
                    
    else:
       print(f"❌ Couldn't check issues on \033[36mhttps://github.com/{owner}/{repository}")
       print (r1.status_code, r1.reason, r1.content)

def format(value):
    return re.sub(' ', '', value).strip().split(",")
