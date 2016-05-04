Vagrant.configure("2") do |config|

	# Ubuntu 14.04.4 32bit LTS
	config.vm.box = "trusty-server-cloudimg-i386-vagrant-disk1"
	config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"

	# Configuration of database node
	 config.vm.define "database" do |node|
	 	node.vm.hostname = "database"
	 	node.vm.network "private_network", ip: "10.10.10.11"
	 	node.vm.provider "virtualbox" do |v|
	 		v.memory = 512
	 	end
	 	node.vm.network "forwarded_port", guest: 22, host: 2221
	 	node.vm.synced_folder "./shared/database", "/home/vagrant/database", :mount_options => ["dmode=777", "fmode=777"]
	 	node.vm.provision "shell", path: "./_conf/database_setup.sh"
	end

	# Configuration of server node
	config.vm.define "server" do |node|
		node.vm.hostname = "server"
		node.vm.network "private_network", ip: "10.10.10.10"
	 	node.vm.provider "virtualbox" do |v|
	 		v.memory = 512
	 	end
	 	node.vm.network "forwarded_port", guest: 22, host: 2211
	 	node.vm.synced_folder "./shared/server", "/home/vagrant/server", :mount_options => ["dmode=777", "fmode=777"]
	 	node.vm.provision "shell", path: "./_conf/server_setup.sh"
	end

end
