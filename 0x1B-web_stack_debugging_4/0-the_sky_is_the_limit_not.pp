#!/usr/bin/pup
# In this web stack debugging task, we are testing how well
our web server setup featuring Nginx is doing under pressure
and it turns out it’s not doing well:
we are getting a huge amount of failed requests.

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
