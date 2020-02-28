# Fix number of files opened in Nginx
include stdlib

file_line { 'u limit nginx':
  ensure => present,
  path   => '/etc/default/nginx',
  line   => 'ULIMIT="-n 4096"',
  match  => 'ULIMIT="-n 15"',
}
-> exec {'restart nginx':
  command => 'service nginx restart',
}
