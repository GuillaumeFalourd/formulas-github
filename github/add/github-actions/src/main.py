#!/usr/bin/python3
import os

from formula import formula

project_path = os.environ.get("RIT_PROJECT_PATH")
workflows = os.environ.get("RIT_GITHUB_ACTIONS_WORKFLOWS")
new_branch = os.environ.get("RIT_NEW_BRANCH")
new_branch_name = os.environ.get("RIT_NEW_BRANCH_NAME")

formula.run(project_path, workflows, new_branch, new_branch_name)
