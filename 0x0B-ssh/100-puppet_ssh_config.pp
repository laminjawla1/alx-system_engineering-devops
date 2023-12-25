#!/usr/bin/env bash
# This file creates an ssh configuration file using puppet
file {'ssh_config':
  mode    => '0744',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => 'Host * PasswordAuthentication no IdentifyFile ~/.ssh/school'
}
