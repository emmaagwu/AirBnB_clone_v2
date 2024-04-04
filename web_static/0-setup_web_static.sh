#!/usr/bin/env bash
# This script sets up a new nginx server to deploy a static file

apt-get update -y
apt-get install nginx -y

#Create directories '/data/', '/data/web_static/' and '/data/web_static/releases'
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "ALX AirBnB clone Project" > /data/web_static/releases/test/index.html

#remove an existing symbolic link and create a new one
ln -sf /data/web_static/releases/test/ /data/web_static/current

#give ownership of /data/ to ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
