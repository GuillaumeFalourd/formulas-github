#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth

def run(user, key, login):

    github_user = requests.get(
        ('https://api.github.com/users/%s' % (login)), auth=HTTPBasicAuth(user, key),
    ).json()

    if "message" in github_user and github_user["message"] == "Not Found":
        print ("Github User does not exist.")

    else:
        email = github_user["email"]
        name = github_user["name"]

        if email is None or name is None:

            events = requests.get(
                ('https://api.github.com/users/%s/events?per_page=100' % (login)), auth=HTTPBasicAuth(user, key),
            ).json()

            if name is None:
                name = get_name(events, login)

            if email is None:
                email = get_email(events, login, name)


        print("------------------------------------------------------------------------------------------------")
        print(f'{"Github User":^20} {"Name":^35} {"Email":^40}')
        print("------------------------------------------------------------------------------------------------")
        print(
            f'{login:^20} {name:^35} {email:^40}'
        )

def get_name(events, login):
    name = "-"
    found_name = False
    for event in events:
        if not found_name and event["type"] == "PushEvent" and event["actor"] is not None and event["payload"] is not None:
            actor = event["actor"]
            if actor["login"] == login:
                payload = event["payload"]
                if len(payload["commits"]) == 1:
                    for commit in payload["commits"]:
                        if not found_name and commit["author"] is not None:
                            author = commit["author"]
                            if not found_name and author["email"] is not None and "github" not in author["email"]:
                                    name = author["name"]
                                    found_name = True
    return name

def get_email(events, login, name):
    email = "-"
    found_email = False
    for event in events:
        if not found_email and event["type"] == "PushEvent" and event["payload"] is not None:
            payload = event["payload"]
            for commit in payload["commits"]:
                if not found_email and commit["author"] is not None:
                    author = commit["author"]
                    if not found_email and author["name"] in login and "github" not in author["email"]:
                        email = author["email"]
                        found_email = True
                    if not found_email and author["name"] in name and "github" not in author["email"]:
                        email = author["email"]
                        found_email = True
                    if not found_email and name.split()[0].lower() in author["name"] and "github" not in author["email"]:
                        email = author["email"] + " *" # The * represents an email that is related but not necessary from this user account.
    return email
