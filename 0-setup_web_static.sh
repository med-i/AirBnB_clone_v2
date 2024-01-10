#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static.

sudo apt update
sudo apt install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo tee -a /data/web_static/releases/test/index.html > /dev/null <<EOT
<!DOCTYPE html>
<body>
    <h1>AirBnb Clone</h1>
</body>
</html>
EOT

sudo ln -sf /data/web_static/current /data/web_static/releases/test/

sudo -R chown ubuntu:ubuntu /data/
