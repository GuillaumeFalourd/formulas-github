#!/usr/bin/python3
import requests
import json
import re
import inquirer

def run(token, owner, repository, branch):
    url = f'https://api.github.com/repos/{owner}/{repository}/git/refs'
    
    authorization = f'token {token}'
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r1 = requests.get(
        url=url+"/heads",
        headers=headers
    )
    
    datas = r1.json()
    repo_branches = []
    repo_shas = [] 
    
    for d in datas:
        branch_name = re.search("(?<=refs\/heads\/).*", d["ref"]).group()
        repo_branches.append(branch_name)
        repo_shas.append(branch_name+"|"+d["object"]["sha"])
    
    questions = [
        inquirer.List('reference',
                message = "What is the reference branch?",
                choices = repo_branches,
            ),
    ]
    answers = inquirer.prompt(questions)
    reference = answers["reference"]
    
    for bs in repo_shas:
        match = re.search(".+?(?=\|)", bs).group()
        if reference == match:
            sha = re.search("(?<=\|).*", bs).group()
    
    data = {}
    data['ref'] = 'refs/heads/%s' % branch
    data['sha'] = sha
    
    json_data = json.dumps(data)
    
    r2 = requests.post(
        url=url,
        data=json_data,
        headers=headers
    )
        
    if r2.status_code == 201:
        message = "✅ Branch %s successfully created on %s's %s repository" % (branch, owner, repository)
        print(message)

    else:
        print("❌ Couldn't create the branch on the repository")
        print (r2.status_code, r2.reason)
        

