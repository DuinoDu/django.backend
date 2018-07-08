#!/bin/bash -e

pip install -r requirements.txt
./manage.py makemigrations simple_app
./manage.py migrate

echo ""
echo "------------"
echo "./manage.py createsuperuser"
echo "------------"
echo "./manage.py runserver"
echo "------------"
echo "if access by other machine, please"
echo "./manage.py runserver 0.0.0.0:8000"
