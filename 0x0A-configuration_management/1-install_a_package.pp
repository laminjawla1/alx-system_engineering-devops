# This script install flask from pip3
exec {'Flask':
  command  => '/usr/bin/pip3 install Flask==2.1.0',
}
