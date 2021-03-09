#!/usr/bin/python3
import inquirer
import requests
import re
import os

def run(token, username, default_branch, repos):
    
    url_repos = f"https://api.github.com/user/repos?type=owner&per_page=100&sort=full_name"

    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }
    
    r1 = requests.get(
        url = url_repos,
        headers = headers
        )

    if r1.status_code == 200:
        datas = r1.json()
        all_repositories = []
    
        for d in datas:
            all_repositories.append(d["name"])

        if repos == "all":
            repos = all_repositories
            
        else: # I want to select
            question1 = [
                inquirer.Checkbox("repositories",
                        message = f"\033[1m\033[36m{username}\033[0m \033[1mrepository to delete:\033[0m ",
                        choices = all_repositories,
                    ),
            ]
            answer = inquirer.prompt(question1)
            repositories = answer["repositories"]            
        
        for repository in repositories:
            url_heads = f"https://api.github.com/repos/{username}/{repository}/git/refs/heads"

            r2 = requests.get(
                url = url_heads,
                headers = headers
                )
    
            datas = r2.json()
            branches = []
            
            for data in datas:
                branch_name = re.search("(?<=refs\/heads\/).*", data["ref"]).group()
                branches.append(branch_name)
                
            if default_branch in branches:
                print(f"\n⚙️  Updating default branch for \033[36m{repository}\033[0m...")
                input_flag_cmd = f"rit github update branch default --rit_repo_owner=\"{username}\" --rit_git_repo=\"{repository}\" --rit_repo_branch=\"{default_branch}\""
                os.system(f"{input_flag_cmd}")
            else:
                print(f"\n⚙️  Creating new branch for \033[36m{repository}\033[0m...")
                input_flag_cmd = f"rit github create branch --rit_repo_owner=\"{username}\" --rit_git_repo=\"{repository}\" --rit_repo_branch=\"{default_branch}\" --rit_branch_default=\"yes\""
                os.system(f"{input_flag_cmd}")
