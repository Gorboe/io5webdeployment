group { 'webadmins':
    ensure => present,
}

user { 'tom':
    ensure => present,
    groups => ['sudo', 'webadmins'],
    home => '/home/tom',
    managehome => true,
    password => '$1$iSvgT7vh$SXk7J3c54RxOG6A13KqhV/',
}

user { 'brady':
    ensure => present,
    groups => ['sudo', 'webadmins'],
    managehome => true,
    home => '/home/brady',
    password => '$1$8ZWY1RD1$xWUayN/Ce.VodCQR8yVpH/',
}

user { 'janet':
    ensure => present,
    groups => ['sudo', 'webadmins'],
    managehome => true,
    password => '$1$RGQZA46h$IFLcbEC3K6dcXjBmG68Ug/',
}
