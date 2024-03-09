#!/usr/bin/env bash
#setting the web server for deployment

apt install nginx -y
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

printf "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html

if [ -L /data/web_static/current ]
then
    rm -r /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

printf "server {
    listen 80;

    index index.html index.htm;
    add_header X-Served-By \$hostname;
    
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm;
    }
}
" > /etc/nginx/sites-available/default
sudo rm -rf /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

service nginx restart
