# client configuration with puppet

file {'/root/alx-system_engineering-devops/0x0B-ssh/ssh_config':
  ensure  => present,
  content => "
		Host 18.207.207.223
		    IdentityFile ~/.ssh/school
		    PasswordAuthentication no",
  owner   =>root,
  group   => root,
  mode    => '0744',
}
