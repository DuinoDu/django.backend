#!/bin/bash

python manage.py makemigrations simple_app
python manage.py migrate simple_app
