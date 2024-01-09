#!/usr/bin/env pup
# Adds a custom HTTP header via puppet
exec { 'script':
  script 	=> 'apt-get update -y;
  apt-get install nginx -y;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider	=> shell,
}
