from fabric.api import *
import os.path
import textwrap
import getpass
######################################################################
# Vagrant
######################################################################

def devstack():
    #local("git clone git://github.com/openstack-dev/devstack.git")
    f=open('./localrc', 'w')
    
    vars = {}
    vars['password'] = password = getpass.getpass()

    print >>f, textwrap.dedent("""
          ENABLED_SERVICES=q-meta,q-lbaas,n-obj,n-cpu,n-sch,n-cauth,horizon,mysql,rabbit,sysstat,cinder,c-api,c-vol,c-sch,n-cond,quantum,q-svc,q-agt,q-dhcp,q-l3,n-novnc,n-xvnc,q-lbaas,g-api,g-reg,key,n-api,n-crt

          DATABASE_PASSWORD=%(password)s
          ADMIN_PASSWORD=%(password)s
          SERVICE_PASSWORD=%(password)s
          SERVICE_TOKEN=%(password)s
          RABBIT_PASSWORD=%(password)s

          # Compute Service
          NOVA_BRANCH=stable/grizzly

          # Volume Service
          CINDER_BRANCH=stable/grizzly

          # Image Service
          GLANCE_BRANCH=stable/grizzly

          # Web UI (Dashboard)
          HORIZON_BRANCH=stable/grizzly

          # Auth Services
          KEYSTONE_BRANCH=stable/grizzly

          # Quantum (Network) service
          QUANTUM_BRANCH=stable/grizzly

          #Enable Logging
          LOGFILE=/opt/stack/logs/stack.sh.log
          VERBOSE=True
          LOG_COLOR=False
          SCREEN_LOGDIR=/opt/stack/logs
          """ % vars) 
    f.close()
######################################################################
# Vagrant
######################################################################

def uninstall():
    local("sudo rm -fr /Applications/Vagrant")
    local("sudo rm -fr /usr/bin/vagrant")
    local("rm -rf ~/.vagrant.d/")
    local("rm -f ./Vagrant.dmg")
    

def download():
    local("curl -O http://files.vagrantup.com/packages/64e360814c3ad960d810456add977fd4c7d47ce6/Vagrant.dmg")

def install():
    if  not os.path.isfile("./Vagrant.dmg"):
        download()
    
    #local("open Vagrant.dmg")
    local("hdiutil attach Vagrant.dmg")
    local("sudo installer -pkg /Volumes/Vagrant/Vagrant.pkg -target /")

######################################################################
# Virtualbox
######################################################################

def download_virtualbox():
    local("curl -L http://download.virtualbox.org/virtualbox/4.2.12/VirtualBox-4.2.12-84980-OSX.dmg -O VirtualBox-4.2.12-84980-OSX.dmg")

def install_virtualbox():
    local("sudo installer -pkg /Volumes/VirtualBox/VirtualBox.mpkg -target /Volumes/Macintosh\ HD")


def init():
    local("rm -f Vagrantfile")
    local("vagrant init precise32 http://files.vagrantup.com/precise32.box")
    local("vagrant up")

def box():
    local("vagrant box add precise64 http://files.vagrantup.com/precise64.box")
    local("vagrant box add quantal64 http://cloud-images.ubuntu.com/quantal/current/quantal-server-cloudimg-vagrant-i386-disk1.box")
