#!/usr/bin/python3
import requests
import json
import inquirer
import re

def Run(user, token, owner, repository):

    base_url = f"https://api.github.com/repos/{owner}/{repository}"
    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    
    print("Checking workflows")
    url_list_workflow = f"{base_url}/actions/workflows?per_page=100"
    r = requests.get(
        url=url_list_workflow,
        headers=headers
    )
    if r.status_code == 200:

        result = []
        workflows = {}

        for workflow in r.json().get("workflows"):
            workflow_name = workflow.get("name")
            workflow_id = workflow.get("id")
            result.append(workflow_name)
            workflows[workflow_name] = workflow_id

        question1 = [
            inquirer.Checkbox("workflow_name",
                    message = f"\033[1mWhich workflow logs to delete:\033[0m ",
                    choices = result,
                ),
        ]
        answer = inquirer.prompt(question1)
        workflow_name = answer["workflow_name"][0]
        workflow_id = workflows[workflow_name]

        url_list_workflow_runs = f"https://api.github.com/repos/{owner}/{repository}/actions/workflows/{workflow_id}/runs"

        r = requests.get(
            url = url_list_workflow_runs,
            headers = headers
            )

        datas = r.json()
        run_ids = []

        for data in datas:
            run_id = data["id"]
            run_ids.append(run_id)
            url_workflow_delete_log = f"{base_url}/repos/{owner}/{repository}/actions/runs/{run_id}"
            r = requests.delete(
                url=url_workflow_delete_log,
                headers=headers
            )

            if r.status_code == 204:
                print(f"✅ Workflow \033[36m{workflow_name}\033[0m logs successfully cleaned for on {owner}'s \033[36m{repository}\033[0m repository")

        else:
            print(f"❌ Couldn't clean workflow logs for \033[36m{workflow_name}\033[0m")
            print (r.status_code, r.reason)
    else:
        print(f"❌ Couldn't retrieve {owner}'s \033[36m{repository}\033[0m repository workflows.")
        print (r.status_code, r.reason)
