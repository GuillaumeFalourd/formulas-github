#!/usr/bin/python3
import requests
import json

def run(token, username, repository):
    url1 = "https://api.github.com/repos/GuillaumeFalourd/GuillaumeFalourd/traffic/views"

    authorization = f"token {token}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization" : authorization,
        }

    r1 = requests.get(
        url=url1,
        headers=headers
        )

    datas = r1.json()

    try:
        views = datas["count"]
    except (IndexError, KeyError):
        views = "-"

    try:
        uniques = datas["uniques"]
    except (IndexError, KeyError):
        uniques = "-"

    print("Views:", views)
    print("Uniques:", uniques)

    url2 = "https://api.github.com/repos/GuillaumeFalourd/GuillaumeFalourd/traffic/popular/referrers"
    r2 = requests.get(
        url=url2,
        headers=headers
        )

    datas = r2.json()

    print("Referrers:", datas)

    url3 = "https://api.github.com/repos/GuillaumeFalourd/GuillaumeFalourd/traffic/clones"
    r3 = requests.get(
        url=url3,
        headers=headers
        )

    datas = r3.json()

    try:
        clones = datas["count"]
    except (IndexError, KeyError) :
        clones = "-"

    print("Clones:", clones)

    url4 = "https://api.github.com/repos/GuillaumeFalourd/GuillaumeFalourd"
    r4 = requests.get(
        url=url4,
        headers=headers
        )

    datas = r4.json()

    try:
        forks = datas["forks_count"]
    except (IndexError, KeyError):
        forks = "-"

    try:
        stars = datas["stargazers_count"]
    except (IndexError, KeyError):
        stars = "-"

    try:
        watchers = datas["subscribers_count"]
    except (IndexError, KeyError):
        watchers = "-"

    print("Forks:", forks)
    print("Stars:", stars)
    print("Watchers:", watchers)