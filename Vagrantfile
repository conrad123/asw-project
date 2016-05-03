Vagrant.configure("2") do |config|

	# Ubuntu 14.04.4 32bit LTS
	config.vm.box = "trusty-server-cloudimg-i386-vagrant-disk1"
	config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"

	# Shared folder
	config.vm.synced_folder ".", "/home/vagrant/site", :mount_options => ["dmode=777", "fmode=777"]


	# For OSX/LINUX
	# config.vm.network "private_network", ip: "10.10.10.10"

	# For WINDOWS (comment the OSX/LINUX and uncomment this line)
	# For WINDOWS, you can access it using http://127.0.0.1:8080/
	config.vm.network "forwarded_port", guest: 8080, host: 8080

	# Provisioning
	config.vm.provision "shell", path: "./_conf/vagrant_setup.sh"


	# Configuration of server node
	# config.vm.define "server" do |node|
	# 	node.vm.hostname = "server"
	# 	node.vm.network "private_network", ip: "10.11.1.101", virtualbox__intnet: true
	# 	node.vm.provider "virtualbox" do |v|
	# 		v.memory = 1024
	# 	end
	# 	node.vm.network "forwarded_port", guest: 22, host: 2211, id: 'ssh', auto_correct: true
	# 	node.ssh.forward_agent = true
	# 	node.vm.provision "shell", path: "./_conf/server_setup.sh"
	# end

	# Configuration of database node
	# config.vm.define "database" do |node|
	# 	node.vm.hostname = "database"
	# 	node.vm.network "private_network", ip: "10.11.1.201", virtualbox__intnet: true
	# 	node.vm.provider "virtualbox" do |v|
	# 		v.memory = 1024
	# 	end
	# 	node.vm.network "forwarded_port", guest: 22, host: 2221, id: 'ssh', auto_correct: true
	# 	node.ssh.forward_agent = true
	# 	node.vm.provision "shell", path: "./_conf/database_setup.sh"
	# end
end
