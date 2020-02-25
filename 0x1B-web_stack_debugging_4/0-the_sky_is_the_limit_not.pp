include stdlib

class nginx {

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }

  file_line { 'u limit nginx':
    notify => Service['nginx'],
    ensure => present,
    path   => '/etc/default/nginx',
    line   => 'ULIMIT="-n 4096"',
    match  => 'ULIMIT="-n 15"',
  }
}

