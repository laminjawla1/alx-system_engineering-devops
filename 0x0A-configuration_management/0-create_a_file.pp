# This puppet script creates a file 'school' in the /tmp directory
$file_name = '/tmp/school'

file {$file_name:
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
