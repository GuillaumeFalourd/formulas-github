#!/usr/bin/python3
import json
import requests
from requests.auth import HTTPBasicAuth
import os

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json', 'User-Agent': 'Python Student', 'Accept': 'application/vnd.github.v3+json'}

def Run(username, repo_details, keep_file, user, key):
    # Print User details
    try:
        user_details = get_user_details(username) # It's a binary string
    except Exception as error:
        print(error)
        exit(0)

    # Open file for writing
    file_name = username + ".txt"
    user_file = open(file_name, "w+")

    if user_details is not None:

        # convert it to utf-8 encoded json string
        user_in_json = user_details.decode('utf-8')

        # Load the JSON to a Python list & dump it back out as formatted JSON
        user_detail_dict = json.loads(user_in_json)

        if user_detail_dict['email'] is None or user_detail_dict['name'] is None:

            events = requests.get(
                ('https://api.github.com/users/%s/events?per_page=100' % (username)), auth=HTTPBasicAuth(user, key),
            ).json()

            if user_detail_dict['name'] is None:
                user_detail_dict['name'] = get_name(events, username)

            if user_detail_dict['email'] is None:
                user_detail_dict['email'] = get_email(events, username, user_detail_dict['name'])

        user_file.write("\n" + "="*10 + " User details of username: " + username + " " + "="*10 + "\n" )
        user_file.write("🔅 User Name: {}".format(user_detail_dict['name']) + "\n")
        user_file.write("📔 Bio: {}".format(user_detail_dict['bio']) + "\n")
        user_file.write("📇 Company: {}".format(user_detail_dict['company']) + "\n")
        user_file.write("📧 Email: {}".format(user_detail_dict['email']) + "\n")
        user_file.write("🛰  Location: {}".format(user_detail_dict['location'])+ "\n")
        user_file.write("👀 Following: {}".format(user_detail_dict['following']) + "\n")
        user_file.write("👥 Followers: {}".format(user_detail_dict['followers']) + "\n")
        user_file.write("🔢 Public Repo count: {}".format(user_detail_dict['public_repos']) + "\n")
        user_file.write("🆙 Account created at: {}".format(user_detail_dict['created_at']) + "\n")
    else:
        print('No User Found')

    if  repo_details == "yes":
        # Print Repo list details
        repo_list = get_repos(username) # It's a binary string

        if repo_list is not None:
            repo_in_json = repo_list.decode('utf-8') # convert it to utf-8 encoded json string

            # Load the JSON to a Python list & dump it back out as formatted JSON
            repo_list = json.loads(repo_in_json)
            user_file.write("\n" + "="*10 + " Repo details of username: " + username + " " + "="*10 + "\n")

            for repo_dict in repo_list:
                user_file.write("*"*10 + " Repo Name: {}".format(repo_dict['name']) + " " + "*"*10 + "\n")
                user_file.write("📄 Description: {}".format(repo_dict['description']) + "\n")
                user_file.write("🌐 Repo url: {}".format(repo_dict['clone_url']) + "\n")
                user_file.write("🔀 Is it forked one : {}".format(repo_dict['fork']) + "\n")
                user_file.write("🆕 Created at: {}".format(repo_dict['created_at']) + "\n")
                user_file.write("🔄 Updated at: {}".format(repo_dict['updated_at']) + "\n")
                user_file.write("🗣  Language: {}".format(repo_dict['language']) + "\n")
                user_file.write("🧮 Fork Count: {}".format(repo_dict['forks_count']) + "\n")
                user_file.write("\n")
        else:
            print('No Repo List Found')

    user_file.close()

    f = open(file_name, 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

    if keep_file == "no":
        os.system(f'rm -rf {file_name}')

def get_user_details(username):
    user_url = '{}users/{}'.format(api_url_base, username)
    response = requests.get(user_url, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url_base))
        return None

def get_repos(username):
    repo_url = '{}users/{}/repos'.format(api_url_base, username)
    response = requests.get(repo_url, headers=headers)

    if response.status_code == 200:
        return (response.content)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, api_url_base))
        return None

def get_name(events, username):
    name = "-"
    found_name = False
    for event in events:
        if not found_name and event["type"] == "PushEvent" and event["actor"] is not None and event["payload"] is not None:
            actor = event["actor"]
            if actor["login"] == username:
                payload = event["payload"]
                if len(payload["commits"]) == 1:
                    for commit in payload["commits"]:
                        if not found_name and commit["author"] is not None:
                            author = commit["author"]
                            if not found_name and author["email"] is not None and "github" not in author["email"]:
                                    name = author["name"]
                                    found_name = True
    return name

def get_email(events, username, name):
    email = "-"
    found_email = False
    for event in events:
        if not found_email and event["type"] == "PushEvent" and event["payload"] is not None:
            payload = event["payload"]
            for commit in payload["commits"]:
                if not found_email and commit["author"] is not None:
                    author = commit["author"]
                    if not found_email and author["name"] in username and "github" not in author["email"]:
                        email = author["email"]
                        found_email = True
                    if not found_email and author["name"] in name and "github" not in author["email"]:
                        email = author["email"]
                        found_email = True
                    if not found_email and name.split()[0].lower() in author["name"] and "github" not in author["email"]:
                        email = author["email"] + " *" # The * represents an email that is related but not necessary from this user account.
    return email
