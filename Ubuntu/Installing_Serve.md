# Installing Ubuntu 18.04 GPU Server for DeepLearning

> gpu = Gforce GTX 1060
>
> ubuntu = 18.04
>
> Cuda = 9.0

## Making a bootable Ubuntu USB disk Tutorial at Mac OS

just do it

Useful links:

* https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-macos#0

## Installing Ubuntu Server 18.04

just do it

Useful links:

* https://websiteforstudents.com/install-ubuntu-18-04-lts-server-screenshots/

## After install

> sudo apt update && sudo apt upgrade
>
> sudo apt install gcc
>
> sudo apt install make
>
> sudo apt install zlib1g-dev 


### ssh key setting

`@ Server`

change `Port 22` to whatever you want

> sudo vi /etc/ssh/sshd_config

`@ Local PC`

> ssh-keygen -f [filepath]
>
> ssh-copy-id -i [key_directory] -p [port] [user]@[ip_address]

Useful links:

* https://www.ssh.com/ssh/copy-id
* http://programmingskills.net/archives/315
* https://conory.com/blog/19194

### WOL(Wake-On-Lan)

First, Check your main board support this
Second, type follow `@ Server` Command Line

> sudo apt-get install ethtool
>
> ifconfig

check your `Ethernet port` start with

> `Ethernet port`: flags ~~

then, type

> sudo ethtool [your Ethernet port]

see if `Wake-on: g` has to be 'g', if not change it.

> sudo ethtool -s [your Ethernet port] wol g

also set your router support `WOL`.

If it supports `WOL`, then use it. Setting the port that you writed in `/etc/ssh/sshd_config`.

You will see green light on LAN port. 

Useful links:

* http://ubuntuforums.org/showthread.php?t=234588
* https://wiki.archlinux.org/index.php/Wake-on-LAN
* http://blog.daum.net/peace20/16779844

## Install Python

1. Download `Python-3.6.5.tgz` from [https://www.python.org/](https://www.python.org/)
2. Unzip
> sudo -zxvf Python-3.6.5.tgz
3. install
> ./configure
>
> make
>
> make test
>
> sudo make install

When you face `sudo pip3 install <package>` error like: 

> pip is configured with locations that require TLS/SSL, however the ssl module in Python is not available.
>
> Collecting <package>
>
>  Could not fetch URL https://pypi.python.org/simple/<package>/: There was a problem confirming the ssl certificate: Can't connect to HTTPS URL because the SSL module is not available. - skipping
>
>  Could not find a version that satisfies the requirement <package> (from versions: )
>
> No matching distribution found for <package>

Install following necessary module
> sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

Then go back to Python Source Folder and 

> sudo make
>
> sudo make install

Upgrade pip

> sudo pip3 install --upgrade pip

After these now you can install packages using either `pip` or `pip3`

Useful links:
* https://stackoverflow.com/questions/41328451/ssl-module-in-python-is-not-available-when-installing-package-with-pip3

## Install CUDA

Install CUDA toolkit first is recommanded. Since you don't need you install cuda driver.

Userful links:
* https://github.com/markjay4k/Install-Tensorflow-on-Ubuntu-17.10-/blob/master/Tensorflow%20Install%20instructions.ipynb
* https://park-ju-hyeong.github.io/2018/04/05/CUDA-8.0-to-9.0/
* http://m.blog.daum.net/goodgodgd/20


