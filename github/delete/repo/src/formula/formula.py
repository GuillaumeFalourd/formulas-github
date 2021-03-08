#!/usr/bin/python3
import requests
import inquirer
import json
import re

def run(token, username):
    
    url = f"https://api.github.com/user/repos?type=owner&per_page=100&sort=full_name"

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
        datas = r1.json()
        repositories = []
    
        for d in datas:
            repositories.append(d["name"])
            
        question1 = [
            inquirer.List("repository",
                    message = f"\033[1m\033[36m{username}\033[0m \033[1mrepository to delete:\033[0m ",
                    choices = repositories,
                ),
        ]
        answer = inquirer.prompt(question1)
        repository = answer["repository"]
        
        question2 = [
            inquirer.List("confirmation",
                    message = f"\033[1mAre you sure you want to delete \033[36m{repository}\033[0m \033[1mrepo?\033[0m",
                    choices = ["Yes", "No"],
                ),
        ]
        answer = inquirer.prompt(question2)
        confirmation = answer["confirmation"]
        
        if confirmation == "Yes":
            url = f"https://api.github.com/repos/{username}/{repository}"

            r2 = requests.delete(
                url=url,
                headers=headers
                )

            if r2.status_code == 204:
                print(f"✅ Repository \033[36mhttps://github.com/{username}/{repository}\033[0m successfully deleted!")

            else:
                print(f"❌ Couldn't delete repository https://github.com/{username}/{repository}")
                print(r2.status_code, r2.reason)
    
    if r1.status_code != 200:
        print(f"❌ Couldn't get {username}'s repositories")
        print(r1.status_code, r1.reason)