from fabric.api import *
from os import sys

# Server declarations.
def local():
    env.hosts = ['localhost']

# Port 22 => 2200 forwarding is set up in Vagrantfile
def vir_env():
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2200']

# Standard Ubuntu setup
def heroku_setup():
    dev_tools()
    virtualenv_setup()
    celery()

def dev_tools():
    sudo( "sudo apt-get -y install python-pip" )
    sudo( "sudo apt-get -y install python-setuptools" )
    sudo( "sudo easy_install pip" )
    sudo( "sudo pip install virtualenv" )
    sudo( "sudo pip install -vv virtualenvwrapper" )
    sudo( "sudo apt-get -y install libpq-dev python-dev" )
    sudo( "sudo gem install heroku" )

# Creating a new heroku virtual environment
#def VE_creation():
#    with settings(warn_only=True):
#        if run("grep -i \"source /usr/local/bin/virtualenvwrapper.sh\" ~/.bash_profile").failed:
#            virtualenv_setup()
#        run("mkvirtualenv --no-site-packages --unzip-setuptools heroku")

# Setup the virtual environment to have various versions of python.
# This function runs only if the grep in previous function failed.
def virtualenv_setup():
    run("echo  >> ~/.bash_profile")
    run('sed -i \'$ a\\export WORKON_HOME=\"$HOME/.virtualenvs\"\\nexport PIP_RESPECT_VIRTUALENV=true\\nsource /usr/local/bin/virtualenvwrapper.sh\' ~/.bash_profile')
    run("echo  >> ~/.bash_profile")
    run("echo if \[ -f ~/.bashrc \]\; then >> ~/.bash_profile")
    run("sed -i \'$ a\\    \. ~/.bashrc\' ~/.bash_profile")
    run("echo fi >> ~/.bash_profile")

    run("echo  >> ~/.bashrc")
    run("echo if \[ -f /etc/bashrc \]\; then >> ~/.bashrc")
    run("sed -i \'$ a\\    . /etc/bashrc\' ~/.bashrc")
    run("sed -i \'$ a\\fi\' ~/.bashrc")

    run("source .bashrc .bash_profile")

def celery():
    with prefix('source bin/activate'):
        run('pip install django-celery django-kombu')

# Install the dev env requirements from custom script
#def mysql_install():
#    with prefix('workon heroku'):
#        run("easy_install lxml")
#    sudo("apt-get -y install debconf-utils")
#    run("echo \"mysql-server-5.1 mysql-server/root_password password qwerty\" > mysql.preseed")
#    run("echo \"mysql-server-5.1 mysql-server/root_password_again password qwerty\" >> mysql.preseed")
#    run("echo \"mysql-server-5.1 mysql-server/start_on_boot boolean true\" >> mysql.preseed")
#    run("cat mysql.preseed | sudo debconf-set-selections")
#    sudo("apt-get -y install mysql-server")
#    run("rm mysql.preseed")

# Configure mysql files
#def mysql_setup():
#    with settings(warn_only=True):
#        if run("grep -i \"collation-server=utf8_general_ci\" /etc/mysql/my.cnf").failed:
#            sudo("sed -i \"/\[mysqld\]/ a\\init_connect=\'SET collation_connection = utf8_general_ci; SET NAMES utf8;\'\\ndefault-character-set=utf8\\ncharacter-set-server=utf8\\ncollation-server=utf8_general_ci\\ndefault-storage-engine=InnoDB\\nsync_frm=0\" /etc/mysql/my.cnf")
#            sudo('service mysql restart')

# called during runtime as the second function with two parameters
#def db_creation():
#    with settings(warn_only=True):
#        if run("grep -i \"default-storage-engine = innodb\" ~/.my.cnf").failed:
#            run("echo \"[mysqld]\" > .my.cnf")
#            run("echo \"default-storage-engine = innodb\" >> .my.cnf")
#            run("echo \"sync_frm = 0\" >> .my.cnf")
#            run("echo \"default-character-set = utf8\" >> .my.cnf")
#            run("sed -i \'$ a\\[mysql]\\nuser=root\\npassword=qwerty\' .my.cnf")
#        run('mysqladmin -uroot -pqwerty create heroku')
#        run('mysql -e \"flush privileges;\"')
#        run('mysql -e \"CREATE USER \'heroku\'@\'localhost\' IDENTIFIED BY \'qwerty\';\"')
#    run('mysql -e \"GRANT ALL PRIVILEGES ON *.* TO \'heroku\'@\'localhost\' IDENTIFIED BY \'qwerty\';\"')
