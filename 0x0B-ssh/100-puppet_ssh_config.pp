#!/usr/bin/env bash
# This file creates an ssh configuration file using puppet

# No password authentcation
file_line {'No Password Auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	PasswordAuthentication no',
  replace => true
}

# Set the default identity file
file_line {'Default Identity File':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '	IdentityFile ~/.ssh/school',
  replace => true
}
