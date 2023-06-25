#!/bin/sh
set -e

cd ./server
python3.9 manage.py runserver 0.0.0.0:8080 #--noreload

echo "INFO: Command Mode ..."
echo "$@"