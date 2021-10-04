#!/bin/bash
if [ -f /.dockerenv ] ; then
pip3 install -r "$(dirname "$0")"/requirements.txt --user --disable-pip-version-check >> /dev/null
fi
python3 "$(dirname "$0")"/main.py
