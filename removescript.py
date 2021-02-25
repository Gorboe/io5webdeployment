import subprocess
import time

if __name__ == '__main__':
    # Source .openstack file
    # subprocess.run('source ~/.openstack', shell=True)

    # Remove the puppet files linked with this deployment
    subprocess.run('rm /etc/puppetlabs/code/environments/production/manifests/users.pp', shell=True)

    # Remove the agent certificates
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean web1-apache2-prod', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean web2-apache2-prod', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean web3-node-prod', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean db1-mysql-prod', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean db2-mysql-prod', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean memcached1-prod', shell=True)
    subprocess.run('/opt/puppetlabs/puppet/bin/puppet cert clean lb1-pound-prod', shell=True)

    # Remove the vm's from openstack
    print('#--------------------------------DELETE STEP 1/7--------------------------------#')
    subprocess.run('nova delete web1-apache2-prod.io5assignment3-web1', shell=True)
    time.sleep(2)
    print('#--------------------------------DELETE STEP 2/7--------------------------------#')
    subprocess.run('nova delete web2-apache2-prod.io5assignment3-web2', shell=True)
    time.sleep(2)
    print('#--------------------------------DELETE STEP 3/7--------------------------------#')
    subprocess.run('nova delete web3-node-prod.io5assignment3-web3', shell=True)
    time.sleep(2)
    print('#--------------------------------DELETE STEP 4/7--------------------------------#')
    subprocess.run('nova delete db1-mysql-prod.io5assignment3-db1', shell=True)
    time.sleep(2)
    print('#--------------------------------DELETE STEP 5/7--------------------------------#')
    subprocess.run('nova delete db2-mysql-prod.io5assignment3-db2', shell=True)
    time.sleep(2)
    print('#--------------------------------DELETE STEP 6/7--------------------------------#')
    subprocess.run('nova delete memcached1-prod.io5assignment3-memcached1', shell=True)
    time.sleep(2)
    print('#--------------------------------DELETE STEP 7/7--------------------------------#')
    subprocess.run('nova delete lb1-pound-prod.io5assignment3-lb1', shell=True)
    time.sleep(2)

    # Delete from foreman page
    print('#--------------------------------DELETE SCRIPT FINISHED--------------------------------#')
    print('NB: You still need to manually remove the machines from foreman.')
