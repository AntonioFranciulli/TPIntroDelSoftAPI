#!/bin/bash

sudo apt update
sudo apt install python3-pip
pip install pipenv
mkdir .venv
pipenv install flask
pipenv install flask_sqlalchemy
pipenv install requests
pipenv install mysql-connector-python
pipenv install Flask-Cors
export HOST="127.0.0.1"
export FLASK_RUN_PORT=5050
export FLASK_DEBUG=1
pipenv run flask run
