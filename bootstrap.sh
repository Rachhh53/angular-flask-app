#!/bin/bash
export FLASK_APP=./main.py
# source $(pipenv --venv)/Scripts/activate
source ./env/Scripts/activate
flask run -h 0.0.0.0
### to run ###
# make script executable
# chmod u+x bootstrap.sh
# execute script in the background
#./bootstrap.sh &
### also do this at some point ###
# py -m pip install -r requirements.txt