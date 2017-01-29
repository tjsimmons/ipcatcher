#!/bin/bash

python /usr/src/app/manage.py collectstatic --noinput
/usr/local/bin/gunicorn -w 2 -b :8000 ipcatcher.wsgi
