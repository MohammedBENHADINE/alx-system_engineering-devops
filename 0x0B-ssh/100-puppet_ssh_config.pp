# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 34.232.53.45
    HostName 34.232.53.45
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
