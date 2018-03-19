#!/bin/bash

echo "This script installs a virtual environment and nginx. You may be prompted for your password."
virtualenv ve
./ve/bin/pip install gunicorn gevent flask uwsgi
sudo apt-get install nginx
