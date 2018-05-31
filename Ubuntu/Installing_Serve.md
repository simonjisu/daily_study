
## Making a bootable Ubuntu USB disk Tutorial at Mac OS

* https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-macos#0

## Installing Ubuntu Server 18.04

* https://websiteforstudents.com/install-ubuntu-18-04-lts-server-screenshots/

## Command line
> man sudo_root
>
> sudo apt update && sudo apt upgrade

## ssh key setting
* https://www.ssh.com/ssh/copy-id
* http://programmingskills.net/archives/315
* https://conory.com/blog/19194

> ssh-keygen -f [filepath]
>
> ssh-copy-id -i [key_directory] -p [port] [user]@[ip_address]

change port:

> sudo vi /etc/ssh/sshd_config

change `Port 22` to whatever you want


## WOL

* http://ubuntuforums.org/showthread.php?t=234588
* https://wiki.archlinux.org/index.php/Wake-on-LAN
* http://blog.daum.net/peace20/16779844

> sudo apt-get install ethtool
>
> ifconfig

check your `Ethernet port` start with

`Ethernet port`: flags ~~

> sudo ethtool [your Ethernet port]

see if `Wake-on: g` has to be 'g' also set your router `WOL`.



