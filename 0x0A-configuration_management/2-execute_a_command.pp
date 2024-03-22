# kills a process

exec {'kill_killmenow':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
  refreshonly => true
}
