import subprocess
import time


def build_mln(file):
    print('mln build ' + file + '.mln')
    subprocess.run('mln build -f ' + file + '.mln -r', shell=True)
    print('mln start ' + file)
    subprocess.run('mln start -p ' + file, shell=True)


def check_build(hostname, file):
    build = subprocess.run('nova list --status BUILD | grep ' + hostname, shell=True)
    while build.returncode == 0:
        time.sleep(10)
        print('checking ' + hostname + ' build progress')
        build = subprocess.run('nova list --status BUILD | grep ' + hostname, shell=True)
    print(hostname + ' is done building')

    error = subprocess.run('nova list --status ERROR | grep ' + hostname, shell=True)
    if error.returncode == 0:
        print(hostname + ' had error, trying to rebuild. Please wait.')
        time.sleep(10)
        subprocess.run('nova delete ' + hostname, shell=True)
        print('Deleting ' + hostname)
        time.sleep(10)
        print('Trying to rebuild ' + file)
        build_mln(file)
        check_build(hostname, file)
    else:
        print(hostname + ' was built with no errors')


if __name__ == '__main__':
    # subprocess.run('. ./.openstack', shell=True) # Source the openstackfile, python runs /bin/shell not /bin/bash

    # Web1
    print('#--------------------------------BUILDING WEB1 STEP: 1/7--------------------------------#')
    time.sleep(2)
    build_mln('io5assignment3-web1')
    check_build('web1-apache2-prod.io5assignment3-web1', 'io5assignment3-web1')

    # Web2
    print('#--------------------------------BUILDING WEB2 STEP: 2/7--------------------------------#')
    time.sleep(2)
    build_mln('io5assignment3-web2')
    check_build('web2-apache2-prod.io5assignment3-web2', 'io5assignment3-web2')

    # Web3
    print('#--------------------------------BUILDING WEB3 STEP: 3/7--------------------------------#')
    time.sleep(2)
    build_mln('io5assignment3-web3')
    check_build('web3-node-prod.io5assignment3-web3', 'io5assignment3-web3')

    # Db1
    print('#--------------------------------BUILDING DB1 STEP: 4/7--------------------------------#')
    time.sleep(2)
    build_mln('io5assignment3-db1')
    check_build('db1-mysql-prod.io5assignment3-db1', 'io5assignment3-db1')

    # Db2
    print('#--------------------------------BUILDING DB2 STEP: 5/7--------------------------------#')
    time.sleep(2)
    build_mln('io5assignment3-db2')
    check_build('db2-mysql-prod.io5assignment3-db2', 'io5assignment3-db2')

    # lb1
    print('#--------------------------------BUILDING LB1 STEP: 6/7--------------------------------#')
    time.sleep(2)
    build_mln('io5assignment3-lb1')
    check_build('lb1-pound-prod.io5assignment3-lb1', 'io5assignment3-lb1')

    # memcached1
    print('#--------------------------------BUILDING MEMCACHED1 STEP: 7/7--------------------------------#')
    #time.sleep(2)
    #build_mln('io5assignment3-memcached1')
    #check_build('memcached1-prod.io5assignment3-memcached1', 'io5assignment3-memcached1')

    # post installation scripts?
    time.sleep(2)
    print('#--------------------------------RUN POST INSTALLATION SCRIPTS--------------------------------#')
    subprocess.run('cp users.pp /etc/puppetlabs/code/environments/production/manifests/users.pp', shell=True)
