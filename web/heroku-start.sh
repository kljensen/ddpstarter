#!/bin/sh
mkdir -p static_cache
python manage.py collectstatic --noinput
gunicorn rerentweb.wsgi  --log-file -
