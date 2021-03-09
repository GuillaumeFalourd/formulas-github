#!/usr/bin/python3
import requests
import json
import re
import inquirer
import os

def run(token, owner, repository, branch, default):
    url = f"https://api.github.com/repos/{owner}/{repository}/git/refs"
    
    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r1 = requests.get(
        url=url+"/heads",
        headers=headers
        )
    
    datas = r1.json()
    shas = {}
    
    for d in datas:
        branch_name = re.search("(?<=refs\/heads\/).*", d["ref"]).group()
        shas[branch_name] = d["object"]["sha"]
    
    questions = [
        inquirer.List("reference",
                message = "\033[1mReference branch\033[0m",
                choices = shas.keys(),
            ),
    ]
    answers = inquirer.prompt(questions)
    reference = answers["reference"]
    print("⚙️ Creating new branch...")
    
    data = {}
    data["ref"] = f"refs/heads/{branch}"
    data["sha"] = shas[reference]
        
    json_data = json.dumps(data)
    
    r2 = requests.post(
        url=url,
        data=json_data,
        headers=headers
        )
        
    if r2.status_code == 201:
        print(f"✅ Branch \033[36m{branch}\033[0m successfully created on {owner}'s \033[36m{repository}\033[0m repository")
        
        if default == "yes":
            print("⚙️  Updating default branch...")
            input_flag_cmd = f"rit github update branch default --rit_repo_owner={owner} --rit_git_repo={repository} --rit_repo_branch={branch}"
            os.system(f"{input_flag_cmd}")

    else:
        print("❌ Couldn't create the branch on the repository")
        print (r2.status_code, r2.reason)
