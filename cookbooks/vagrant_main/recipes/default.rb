require_recipe "vim"
#require_recipe "python"
#require_recipe "rabbitmq"
#require_recipe "openssl"
require_recipe "git"
require_recipe "ack-grep"
require_recipe "xml"
require_recipe "xslt"
require_recipe "build-essential"
require_recipe "ubuntu"
require_recipe "postgresql"
require_recipe "apt"
#require_recipe "apache2"
#require_recipe "mysql::client"
#require_recipe "mysql::server"
#require_recipe "pacman"

#execute "disable-default-site" do
#    command "sudo a2dissite default"
#      notifies :reload, resources(:service => "apache2"), :delayed
#end

#web_app "project" do
#    template "project.conf.erb"
#      notifies :reload, resources(:service => "apache2"), :delayed
#end
