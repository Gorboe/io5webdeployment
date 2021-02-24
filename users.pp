user { 'tom':
    ensure => present,
    groups => ['sudo'],
    password => '$1$iSvgT7vh$SXk7J3c54RxOG6A13KqhV/',
}

user { 'brady':
    ensure => present,
    groups => ['sudo', 'admin'],
    password => Sensitive("bradypw"),
}

user { 'janet':
    ensure => present,
    password => Sensitive("janetpw"),
}
