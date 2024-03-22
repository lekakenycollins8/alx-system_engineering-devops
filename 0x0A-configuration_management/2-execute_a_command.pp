# kills a process

exec {'kill_killmenow':
  command     => 'pkill -9 -f killmenow',
  path        => '/bin:/usr/bin:/sbin:/usr/sbin',
}
