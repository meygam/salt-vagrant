# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  config.vm.define "master" do |master|
    master.vm.box = "ubuntu/trusty64"
    master.vm.host_name = "master"
    master.vm.network "private_network", ip: "192.168.33.10"
    master.vm.synced_folder "etc/salt/master.d", "/etc/salt/master.d"
    # master.vm.synced_folder "etc/salt/minion.d", "/etc/salt/minion.d"
    master.vm.synced_folder "etc/pki/tls/certs", "/etc/pki/tls/certs"
    master.vm.synced_folder "srv", "/srv"

    master.vm.provision :salt do |salt|
      salt.install_master = true
      salt.install_type = "stable"
      salt.colorize = true
      salt.bootstrap_options = "-P -D"
      salt.verbose = true
      salt.minion_config = "etc/salt/minion"
    end
  end

  config.vm.define "minion1" do |minion1|
    minion1.vm.box = "ubuntu/trusty64"
    minion1.vm.host_name = "minion1"
    minion1.vm.network "private_network", ip: "192.168.33.11"
    # minion1.vm.synced_folder "etc/salt/minion.d", "/etc/salt/minion.d"
    minion1.vm.synced_folder "srv/salt", "/srv/salt"

    minion1.vm.provision :salt do |salt|
      salt.install_type = "stable"
      salt.colorize = true
      salt.bootstrap_options = "-P -D"
      salt.verbose = true
      salt.minion_config = "etc/salt/minion"
      salt.grains_config = "etc/salt/grains/minion1"
      salt.run_highstate = true
    end
  end

  config.vm.define "minion2" do |minion2|
    minion2.vm.box = "ubuntu/trusty64"
    minion2.vm.host_name = "minion2"
    minion2.vm.network "private_network", ip: "192.168.33.12"
    # minion2.vm.synced_folder "etc/salt/minion.d", "/etc/salt/minion.d"
    minion2.vm.synced_folder "srv/salt", "/srv/salt"

    minion2.vm.provision :salt do |salt|
      salt.install_type = "stable"
      salt.colorize = true
      salt.bootstrap_options = "-P -D"
      salt.verbose = true
      salt.minion_config = "etc/salt/minion"
      salt.grains_config = "etc/salt/grains/minion2"
      salt.run_highstate = true
    end
  end

  config.vm.define "minion3" do |minion3|
    minion3.vm.box = "ubuntu/trusty64"
    minion3.vm.host_name = "minion3"
    minion3.vm.network "private_network", ip: "192.168.33.13"
    # minion3.vm.synced_folder "etc/salt/minion.d", "/etc/salt/minion.d"
    minion3.vm.synced_folder "srv/salt", "/srv/salt"

    minion3.vm.provision :salt do |salt|
      salt.install_type = "stable"
      salt.colorize = true
      salt.bootstrap_options = "-P -D"
      salt.verbose = true
      salt.minion_config = "etc/salt/minion"
      salt.grains_config = "etc/salt/grains/minion3"
      salt.run_highstate = true
    end
  end
end
