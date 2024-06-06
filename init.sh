#!/bin/bash

sudo apt update
sudo apt install python3-pip
pip install pipenv
mkdir .venv
pipenv install flask
export FLASK_DEBUG=1
pipenv run flask run
