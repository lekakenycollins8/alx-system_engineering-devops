# client configuration with puppet

file_line {'Turn off password auth':
ensure => 'present',
path   => '/root/alx-system_engineering-devops/0x0B-ssh/ssh_config',
line   => '    PasswordAuthentication no',
}

file_line {'identity file':
ensure => 'present',
path   => '/root/alx-system_engineering-devops/0x0B-ssh/ssh_config',
line   => '    IdentityFile ~/.ssh/school',
}
