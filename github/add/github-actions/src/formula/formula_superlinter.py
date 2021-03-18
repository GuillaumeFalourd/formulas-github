#!/usr/bin/python3

github_token = "${{ secrets.GITHUB_TOKEN }}"
super_linter=f"""
name: Super-Linter Code Base

#
# Documentation:
# https://help.github.com/en/articles/workflow-syntax-for-github-actions
#

on:
  [push, pull_request]

jobs:
  build:
    name: Lint Code Base
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
        with:
          fetch-depth: 0

      - name: Lint Code Base
        uses: github/super-linter@v3
        env:
          VALIDATE_ALL_CODEBASE: false
          GITHUB_TOKEN: {github_token}
"""

def run():
    print("🔎 Adding SuperLinter workflow...")
    f = open("super_linter.yml", "w")
    f.write(super_linter)
    f.close()
