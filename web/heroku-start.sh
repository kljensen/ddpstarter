#!/bin/sh
mkdir -p static_cache
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:$PORT
