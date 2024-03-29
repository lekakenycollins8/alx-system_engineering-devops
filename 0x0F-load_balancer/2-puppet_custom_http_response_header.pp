# automate the task of creating a custom HTTP header

exec { 'apt-update':
  command => ''/usr/bin/apt-get update'',
  before  => Package['nginx'],
}

package { 'nginx':
  ensure  => 'present',
  require => Exec['apt-update'],
}

file_line { 'http_header':
  ensure  => present,
  line    => 'add_header X-Served-By "${hostname}";',
  match   => '^http {',
  path    => '/etc/nginx/nginx.conf',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File_line['http_header'],
}
