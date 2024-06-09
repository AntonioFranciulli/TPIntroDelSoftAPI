#!/bin/bash

sudo apt update
sudo apt install python3-pip
pip install pipenv
mkdir .venv
pipenv install flask
pipenv install flask_sqlalchemy
pipenv install mysql-connector-python
export FLASK_DEBUG=1
pipenv run flask run
