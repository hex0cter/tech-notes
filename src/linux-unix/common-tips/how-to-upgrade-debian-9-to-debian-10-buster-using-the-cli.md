
date: None  
author(s): None  

# [How to upgrade Debian 9 to Debian 10 Buster using the CLI - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-upgrade-debian-9-to-debian-10-buster-using-the-cli)

Ihave Debian 9.x installed on AWS EC2. How do I upgrade Debian 9 Stretch to Debian 10 Buster using the [apt command](https://www.cyberciti.biz/faq/ubuntu-lts-debian-linux-apt-command-examples/)/[apt-get command](https://www.cyberciti.biz/tips/linux-debian-package-management-cheat-sheet.html) CLI? How can I upgrade Debian 9 to Debian 10 using ssh client?  
  
Debian Linux 10 “Buster” released. The new version offers updated packages and five years of support. In this release, GNOME defaults to using the Wayland display server instead of Xorg. However, the Xorg display server still installed by default. This page shows how to update Debian 9 Stretch to Debian 10 Buster using command-line options.

  * Updated desktop environments such as Cinnamon 3.8, GNOME 3.30, KDE Plasma 5.14, LXDE 0.99.2, LXQt 0.14, MATE 1.20, Xfce 4.12.
  * Secure Boot support greatly improved
  * AppArmor is installed and enabled by default
  * Apache
  * BIND
  * Chromium
  * Emacs
  * Firefox
  * GIMP
  * GNU
  * GnuPG
  * Golang
  * Inkscape
  * LibreOffice
  * Linux
  * MariaDB
  * OpenJDK
  * Perl
  * PHP
  * PostgreSQL
  * Python
  * Ruby
  * Rustc
  * Samba
  * systemd
  * Thunderbird
  * Vim



The procedure is as follows:

  1. Backup your system.
  2. Update existing packages and reboot the Debian 9.x system.
  3. Edit the file `/etc/apt/sources.list` using a text editor and replace each instance of `stretch` with `buster`.
  4. Update the packages index on Debian Linux, run: `sudo apt update`
  5. Prepare for the operating system upgrade, run: `sudo apt upgrade`
  6. Finally, update Debian 9 to Debian 10 buster by running: `sudo apt full-upgrade`
  7. Reboot the Linux system so that you can boot into Debian 10 Buster
  8. Verify that everything is working correctly.



Let us see all command in details.

## Step 1. Backup your system

It is crucial to backup all data and system configurations. Cloud-based VMs can be quickly backup and restore using snapshots. I use [rsnapshot](https://www.cyberciti.biz/faq/linux-rsnapshot-backup-howto/), which is the perfect solution for making backups on the local or remote servers. [Check os version in Linux](https://www.cyberciti.biz/faq/how-to-check-os-version-in-linux-command-line/):  
`lsb_release -a`  
Sample outputs:
    
    
    No LSB modules are available.
    Distributor ID:	Debian
    Description:	Debian GNU/Linux 9.9 (stretch)
    Release:	9.9
    Codename:	stretch

Note down the [Linux kernel version](https://www.cyberciti.biz/faq/find-print-linux-unix-kernel-version/) too:  
`uname -mrs`  
Sample outputs:
    
    
    Linux 4.9.0-9-amd64 x86_64

## Step 2. Update installed packages

Type the following [apt command](https://www.cyberciti.biz/faq/ubuntu-lts-debian-linux-apt-command-examples/) or [apt-get command](https://www.cyberciti.biz/tips/linux-debian-package-management-cheat-sheet.html):  
`sudo apt updatesudo apt upgradesudo apt full-upgrade

sudo apt --purge autoremove

`OR

`sudo apt-get updatesudo apt-get upgradesudo apt-get full-upgrade

sudo apt-get --purge autoremove

`

  
[Reboot the Debian 9.x stretch](https://www.cyberciti.biz/faq/howto-reboot-linux/) to apply the kernel and other updates:  
`sudo reboot`

## Step 3. Update /etc/apt/sources.list file

Before starting the upgrade you must reconfigure APT’s source-list files. To view current settings using the [cat command](https://www.cyberciti.biz/faq/linux-unix-appleosx-bsd-cat-command-examples/):  
`cat /etc/apt/sources.list`  
Sample outputs:
    
    
    deb http://cdn-aws.deb.debian.org/debian stretch main
    deb http://security.debian.org/debian-security stretch/updates main
    deb http://cdn-aws.deb.debian.org/debian stretch-updates main  
  
---  
  
The stretch indicates that we are using an older version. Hence, we must change all the references in this file from Stretch to Buster using a text editor such as vim:  
`vi /etc/apt/sources.list`  
I prefer to use sed tool, but first backup all config files using the [cp command](https://www.cyberciti.biz/faq/cp-copy-command-in-unix-examples/):  
`sudo cp -v /etc/apt/sources.list /root/sudo cp -rv /etc/apt/sources.list.d/ /root/sudo sed -i 's/stretch/buster/g' /etc/apt/sources.listsudo sed -i 's/stretch/buster/g' /etc/apt/sources.list.d/*### see updated file now ###

cat /etc/apt/sources.list

`  


![How To Upgrade Debian 9 Stretch To Linux Debian 10 Buster](https://www.cyberciti.biz/media/new/faq/2019/07/How-To-Upgrade-Debian-9-Stretch-To-Linux-Debian-10-Buster.png)APT source-list files updated to use buster

### Updating the package list

Simply run:  
`sudo apt update`  
![Updating the package list](https://www.cyberciti.biz/media/new/faq/2019/07/Updating-the-package-list.png)

## Step 4. Minimal system upgrade

A two-part process is necessary to avoid the removal of large numbers of packages that you want to keep. Therefore, first run the following:  
`sudo apt upgrade`  
![Debian 9 to Debian 10 Minimal system upgrade](https://www.cyberciti.biz/media/new/faq/2019/07/Debian-9-to-Debian-10-Minimal-system-upgrade.png)Just follow on-screen instructions. During the upgrade process, you may get various questions, like “Do you want to restart the service? ” OR “keep or erase config options” and so on.

![Restart services during package upgrades without asking](https://www.cyberciti.biz/media/new/faq/2019/07/Restart-services-during-package-upgrades-without-asking.png)

And:

![What do you want to do about modified config file](https://www.cyberciti.biz/media/new/faq/2019/07/What-do-you-want-to-do-about-modified-config-file.png)

## Step 5. Upgrading Debain 9 to Debian 10

In addition, minimum upgrades we need to do full upgrades to finish the whole Debian 9 to Debian 10 update process. This is the main part of the upgrade. In other words, execute the following command to perform a complete upgrade of the system, installing the newest available versions of all packages, and resolving all possible dependency:  
`sudo apt full-upgrade`  
![How to upgrade Debian 9 to Debian 10 Buster using the CLI](https://www.cyberciti.biz/media/new/faq/2019/07/How-to-upgrade-Debian-9-to-Debian-10-Buster-using-the-CLI.png)  
[Reboot the Linux system](https://www.cyberciti.biz/faq/ssh-restart-linux-system-reboot-command/) to boot into Debian Linux 10 buster, issue:  
`sudo reboot`

## Step 6. Verification

It is time to confirm the upgrade. Run:  
`uname -r  
lsb_release -a`  
Sample outputs:
    
    
    No LSB modules are available.
    Distributor ID:	Debian
    Description:	Debian GNU/Linux 10 (buster)
    Release:	10
    Codename:	buster

Finally, clean up outdated packages using the [apt command](https://www.cyberciti.biz/faq/ubuntu-lts-debian-linux-apt-command-examples/)/[apt-get command](https://www.cyberciti.biz/tips/linux-debian-package-management-cheat-sheet.html):  
`sudo apt --purge autoremove`  
![How to Upgrade Debian 9 Stretch to Debian 10 Buster](https://www.cyberciti.biz/media/new/faq/2019/07/How-to-Upgrade-Debian-9-Stretch-to-Debian-10-Buster.png)

## Conclusion

And there you have it. We have successfully upgraded to Debian Linux 10. Debian project also posted an in-depth guide [here](https://www.debian.org/releases/buster/amd64/release-notes/ch-upgrading.en.html) that explains other issues one might face during installation.

