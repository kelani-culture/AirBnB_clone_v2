#!/usr/bin/env bash
# install nginx
sudo apt-get -y update && sudo apt-get -y install nginx


if [ ! -d '/data/' ]; then
    mkdir '/data/'
fi

if [ ! -d '/data/web_static/' ]; then
    mkdir '/data/web_static'
fi

if [ ! -d '/data/web_static/releases/' ]; then
    mkdir '/data/web_static/releases/'
fi

if [ ! -d '/data/web_static/shared/' ]; then
    mkdir '/data/web_static/shared'
fi

if [ ! -d '/data/web_static/releases/test/' ]; then
    mkdir '/data/web_static/releases/test/'
fi

if [ ! -f '/data/web_static/releases/test/index.html' ]; then
    touch '/data/web_static/releases/test/index.html'
    html="""
    <html>
      <head>
      </head>
      <body>
	   Holberton School
      </body>
     </html>
    """
    echo "$html" > '/data/web_static/releases/test/index.html'
fi

#!/bin/bash

# Create directories if they don't exist
mkdir -p /data/web_static/shared

# Create a symbolic link /data/web_static/current
# If the symbolic link already exists, delete and recreate it
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
# This should be recursive; everything inside should be created/owned by this user/group
chown -R ubuntu:ubuntu /data/


# update nginx configuration to serve the content of /data/web_static/current
configure="""
server {
	listen 80 default_server;
	server_name _;

	location / {
		root /var/www/html;
	}
	location = /hbnb_static/ {
		alias /data/web_static/current/index.html;
        index index.html;
	}
}
"""

echo "$configure" > /etc/nginx/sites-available/default
sudo service nginx restart

