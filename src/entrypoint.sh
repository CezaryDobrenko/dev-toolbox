#!/bin/bash

echo "Apply database migrations"
python manage.py makemigrations

echo "Apply database migrations"
python manage.py migrate

echo "Collect static"
# rm -r static - fore static reload
python manage.py collectstatic --noinput

echo "Starting server"
gunicorn --bind 0.0.0.0:8000 --reload toolbox.wsgi
