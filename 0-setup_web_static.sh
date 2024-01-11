#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static.

sudo apt update
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

echo "<!DOCTYPE html>
  <head>
  </head>
  <body>
    <h1>AirBnb Clone</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/server_name _;/a \\\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\\n" /etc/nginx/sites-available/default

sudo service nginx restart
