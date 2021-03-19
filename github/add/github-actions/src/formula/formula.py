#!/usr/bin/python3
import os

from formula import formula_horusec
from formula import formula_superlinter
from formula import formula_dependabot

def run(project_path, workflows, new_branch, new_branch_name):
    try:
        current_pwd = os.environ.get("CURRENT_PWD")
        if project_path == "" or project_path == current_pwd:
            os.chdir(current_pwd)
        else:
            os.chdir(project_path)
        
        if new_branch == "yes":
            os.system(f"git checkout -b {new_branch_name}")
            
        createGithubFolder()
        createGithubActionsWorkflows(workflows)
        
        if new_branch == "yes":
            os.system(f"git add .")
            os.system("git commit -m \"Add Github Actions Workflows with Ritchie CLI\"")
            os.system(f"git push origin {new_branch_name}")
        
        print("✅ Github Actions workflows successfully added to the project.")
        if new_branch == "yes":
            print(f"✅ Code successfully added and committed to the {new_branch_name} branch.")
    
    except:
        print("❌ Oops, something went wrong. Check the informed inputs first.") 
        print("⚠️  If the error persists, please, open an ISSUE on the related repository.")
        
def createGithubFolder():
    print("Creating folders...") 
    if not os.path.exists(".github"):
        os.makedirs(".github")
        os.chdir('.github')
    else:
        os.chdir('.github')
    
    if not os.path.exists("workflows"):
        os.makedirs("workflows")
        os.chdir('workflows')
    else:
        os.chdir('workflows')

def createGithubActionsWorkflows(workflows):
    workflows = workflows.split("|")    
    loop = 0
    for w in workflows:
        loop = loop +1
        if w == "Horusec":
            formula_horusec.run()
        elif w == "Super-Linter":
            formula_superlinter.run()
