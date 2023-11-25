#!/usr/bin/env bash
# using puppet to make changes to configuration file

file {  'etc/ssh/ssh_config' :
	 ensure => present,
content => "
	#ssh client configuration
	host*
	IdentifyFile ~/.ssh/school
	paswordAuthentication no
}
