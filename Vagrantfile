# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/contrib-buster64"
  config.vm.box_check_update = false

  config.vm.provision "shell", path: "vagrant/python.sh"
  config.vm.provision "shell", path: "vagrant/pyenv.sh", privileged: false
  config.vm.provision "file", source: "vagrant/bashrc", destination: "/home/vagrant/.bashrc"
  config.vm.provision "shell", inline: "pyenv install 3.10.4", privileged: false

  # config.vm.network "forwarded_port", guest: 80, host: 8080
end
