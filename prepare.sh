#!/bin/bash -e

pip install -r requirements.txt
./manage.py makesuperuser
./manage.py makemigrations simple_app
./manage.py migrate
./manage.py runserver
