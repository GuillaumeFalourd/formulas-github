#!/usr/bin/python3
import requests
import inquirer
import json

def run(token, owner, repository):
    url = f"https://api.github.com/repos/{owner}/{repository}/actions/secrets"
    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r = requests.get(
        url = url,
        headers = headers
    )

    if r.status_code == 200:
        datas = r.json()
        all_secrets = datas["secrets"]
        secrets_names = []

        for secret in all_secrets:
                secret_name = secret["name"]
                secrets_names.append(secret_name)

        question1 = [
                inquirer.Checkbox("secrets",
                        message = f"\033[1m\033[36m{repository}\033[0m \033[1msecrets to delete\033[0m ",
                        choices = secrets_names,
                    ),
            ]
        answer = inquirer.prompt(question1)
        secrets = answer["secrets"]

        for secret_name in secrets:
            r = requests.delete(
                url = url + f"/{secret_name}",
                headers = headers
            )

            if r.status_code == 204:
                print(f"✅ Secret \033[36m{secret_name}\033[0m successfully deleted from \033[36m{repository}\033[0m repository")

            else:
                print(f"❌ Couldn't delete the \033[36m{secret_name}\033[0m secret from the repository")
                print (r.status_code, r.reason)

    else:
        print("❌ Couldn't get the repository secrets")
        print (r.status_code, r.reason)
