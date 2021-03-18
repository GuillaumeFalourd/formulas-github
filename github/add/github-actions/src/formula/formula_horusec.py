#!/usr/bin/python3

horusec_gh = """
name: Horusec Security Check

#
# Documentation:
# https://horusec.io
#

on: [push, pull_request]

jobs:
  horusec-security:
    name: horusec-security
    runs-on: ubuntu-latest
    steps:
    - name: Check out code
      uses: actions/checkout@v2
    - name: Running Horusec Security
      run: |
        curl -fsSL https://horusec.io/bin/install.sh | bash
        horusec start -p="./" -e="true"
"""

def run():
    print("🔒 Adding Horusec workflow...")
    f = open("horusec-workflow.yml", "w")
    f.write(horusec_gh)
    f.close()
