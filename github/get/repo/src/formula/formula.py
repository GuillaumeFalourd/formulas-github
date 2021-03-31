#!/usr/bin/env python3

import os
import re

from urllib.parse import urljoin

import requests
from requests import get
from requests.auth import HTTPBasicAuth

import json

regex_pattern = r"(?<=\+)(.*)"

def run(user, key, repo_url, contribution):

    user_repo = re.sub("https://github.com/","", repo_url)
    datas = user_repo.split(sep ='/', maxsplit=2)
    repo_owner = datas[0]
    repo_name = datas[1]

    authorization = f"token {key}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    insights = []
    contributors = []
    repo_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

    print(f"🐙 Getting insights for {repo_owner}'s {repo_name} repository:")
    traffic = requests.get(
        url = repo_url + "/traffic/views",
        headers = headers,
    ).json()

    clones = requests.get(
        url = repo_url + "/traffic/clones",
        headers = headers,
    ).json()

    contributors = requests.get(
        url = repo_url + "/contributors",
        headers = headers,
    ).json()

    repo_stats = requests.get(
        url = repo_url,
        headers = headers,
    ).json()

    try:
        clones = clones["count"]
    except (IndexError, KeyError) :
        clones = "-"

    try:
        forks = repo_stats["forks_count"]
    except (IndexError, KeyError):
        forks = "-"

    try:
        stars = repo_stats["stargazers_count"]
    except (IndexError, KeyError):
        stars = "-"

    try:
        watchers = repo_stats["subscribers_count"]
    except (IndexError, KeyError):
        watchers = "-"

    try:
        views = traffic["count"]
    except (IndexError, KeyError):
        views = "-"

    try:
        uniques = traffic["uniques"]
    except (IndexError, KeyError):
        uniques = "-"

    insights.append(
        {
            "repo": repo_name,
            "views": views,
            "uniques": uniques,
            "clones": clones,
            "contributors": len(contributors),
            "contributors_list": contributors,
            "forks": forks,
            "stars": stars,
            "watchers": watchers,
        }
    )

    print("\n-------------------------------------------------------------------------------------------------------")
    print(f'{"Repository":25} {"Views":^10} {"Uniques":^10} {"Clones":^10} {"Contributors":^10} {"Forks":^10} {"Stars":^10} {"Watchers":^10}')
    print("-------------------------------------------------------------------------------------------------------")
    for insight in insights:
        print(
            f'{insight["repo"]:25} {insight["views"]:^10} {insight["uniques"]:^10} {insight["clones"]:^10} {insight["contributors"]:^12} {insight["forks"]:^10} {insight["stars"]:^10} {insight["watchers"]:^10}'
        )
    if contribution == "yes" :
        print_contribution(insights, user, key)

def print_contribution(insights, user, key):
    for insight in insights:
            print(f"\nRepository: https://github.com/ZupIT/" + insight["repo"] + "/")
            print("----------------------------------------------------------------------------------------------------------------------------")
            print(f'{"Github ID":10} {"Username":^20} {"Name":^35} {"Email":^40} {"Contributions":^10}')
            print("----------------------------------------------------------------------------------------------------------------------------")

            try:
                for contributor in insight["contributors_list"]:
                    get_contributor_details(user, key, contributor)

                    print(
                        f'{contributor["id"]:^10} {contributor["login"]:^20} {contributor["name"]:^35} {contributor["email"]:^40} {contributor["contributions"]:^10}'
                    )

            except(TypeError):
                print("🚫 Sorry: We could't retrieve the contributors list for this repository...\n")

def get_contributor_details(user, key, contributor):
    github_user = requests.get(
        ("https://api.github.com/users/%s" % (contributor["login"])), auth=HTTPBasicAuth(user, key),
    ).json()

    if "message" in github_user and github_user["message"] == "Not Found":
        print ("Github User does not exist.")

    else:
        contributor["email"] = github_user["email"]
        contributor["name"] = github_user["name"]

        if contributor["email"] is None or contributor["name"] is None:

            events = requests.get(
                ("https://api.github.com/users/%s/events?per_page=100" % (contributor["login"])), auth=HTTPBasicAuth(user, key),
            ).json()

            if contributor["name"] is None:
                contributor["name"] = get_name(events, contributor["login"])

            if contributor["email"] is None:
                contributor["email"] = get_email(events, contributor["login"], contributor["name"])

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

def get_name(events, login):
    name = "-"
    found_name = False
    for event in events:
        if not found_name and event["type"] == "PushEvent" and event["actor"]is not None and event["payload"] is not None:
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
