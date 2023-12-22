# This script kills the program 'killmenow'
exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
