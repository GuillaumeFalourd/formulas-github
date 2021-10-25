#!/usr/bin/python3
import requests
import json
import inquirer
import re

def Run(user, token, owner, repository, workflow_type):

    base_url = f"https://api.github.com/repos/{owner}/{repository}"
    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    if workflow_type == "repository_dispatch":
        print("Creating Repository Dispatch event")

        question1 = [
            inquirer.Text("event_type",
                    message = f"\033[1m\033[36mWhat is the event type?\033[0m"
                ),
        ]
        answer = inquirer.prompt(question1)
        event_type = answer["event_type"]

        question2 = [
            inquirer.List("client_payload",
                    message = f"\033[1mDo you want to send a client_payload?\033[0m",
                    choices=["yes", "no"]
                ),
        ]
        answer = inquirer.prompt(question2)
        client_payload = answer["client_payload"]

        if client_payload == "yes":
            question3 = [
                inquirer.Text("quantity",
                        message = f"\033[1mHow many input would you like to inform in the client payload? (from 0 to 10)\033[0m",
                    ),
            ]
            answer = inquirer.prompt(question3)
            quantity = answer["quantity"]

            inputs = {}
            if quantity != 0:
                for i in range(int(quantity)):
                    question4 = [
                        inquirer.Text("input",
                                message = f"\033[1mInform input name and value: (e.g: name::value)\033[0m",
                            ),
                        ]
                    answer = inquirer.prompt(question4)
                    input = answer["input"]
                    splitted_input = input.split("::", 2)
                    name = splitted_input[0]
                    value = splitted_input[1]
                    inputs[name] = value

        data = {}
        data["event_type"] = event_type
        if client_payload == "yes":
            data["client_payload"] = inputs
        json_data = json.dumps(data)

        url_repo_dispatch = f"{base_url}/dispatches"
        r = requests.post(
            url=url_repo_dispatch,
            data=json_data,
            headers=headers
        )

        if r.status_code == 204:
            print(f"✅ Repository dispatch event successfully triggered for {owner}'s \033[36m{repository}\033[0m repository")

        else:
            print(f"❌ Couldn't trigger repository dispatch event for {owner}'s \033[36m{repository}\033[0m repository")
            print (r.status_code, r.reason)

    if workflow_type == "workflow_dispatch":
        print("Creating Workflow Dispatch event")
        url_list_workflow_dispatch = f"{base_url}/actions/workflows?per_page=100"
        r = requests.get(
            url=url_list_workflow_dispatch,
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
                        message = f"\033[1mWhich workflow to trigger:\033[0m ",
                        choices = result,
                    ),
            ]
            answer = inquirer.prompt(question1)
            workflow_name = answer["workflow_name"][0]

            url_heads = f"https://api.github.com/repos/{owner}/{repository}/git/refs/heads"

            r = requests.get(
                url = url_heads,
                headers = headers
                )

            datas = r.json()
            branches = []

            for data in datas:
                branch_name = re.search("(?<=refs\/heads\/).*", data["ref"]).group()
                branches.append(branch_name)

            question2 = [
                inquirer.Checkbox("branch",
                        message = f"\033[1mWhich branch to trigger:\033[0m ",
                        choices = branches,
                    ),
            ]
            answer = inquirer.prompt(question2)
            branch = answer["branch"][0]

            question3 = [
                inquirer.Text("quantity",
                        message = f"\033[1mHow many input would you like to inform? (from 0 to 10)\033[0m",
                    ),
            ]
            answer = inquirer.prompt(question3)
            quantity = answer["quantity"]

            inputs = {}
            if quantity != 0:
                for i in range(int(quantity)):
                    question4 = [
                        inquirer.Text("input",
                                message = f"\033[1mInform input name and value: (e.g: name::value)\033[0m",
                            ),
                        ]
                    answer = inquirer.prompt(question4)
                    input = answer["input"]
                    splitted_input = input.split("::", 2)
                    name = splitted_input[0]
                    value = splitted_input[1]
                    inputs[name] = value

            data = {}
            data["ref"] = branch
            data["inputs"] = inputs
            json_data = json.dumps(data)

            workflow_id = workflows[workflow_name]
            url_workflow_dispatch = f"{base_url}/actions/workflows/{workflow_id}/dispatches"
            r = requests.post(
                url=url_workflow_dispatch,
                data=json_data,
                headers=headers
            )

            if r.status_code == 204:
                print(f"✅ Workflow \033[36m{workflow_name}\033[0m successfully triggered for {branch} branch on {owner}'s \033[36m{repository}\033[0m repository")

            else:
                print(f"❌ Couldn't trigger workflow \033[36m{workflow_name}\033[0m")
                print (r.status_code, r.reason)
        else:
            print(f"❌ Couldn't retrieve {owner}'s \033[36m{repository}\033[0m repository workflows.")
            print (r.status_code, r.reason)
