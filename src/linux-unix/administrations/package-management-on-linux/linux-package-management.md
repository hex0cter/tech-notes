
date: None  
author(s): None  

# [Linux package management - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/package-management-on-linux/linux-package-management)

In Red Hat Enterprise Linux and Fedora by default, each administrative user needs to know the root password, in addition to their own password.

In Ubuntu, each user only has one password. Users in the **admin** group can run command line and graphical applications with elevated privileges. Graphical admin tools prompt for this password when run, and command line tools can be run with root-privileges using [sudo](https://help.ubuntu.com/community/RootSudo).

## Package Management

Ubuntu has more packages available than Fedora, so you'll have a better chance of finding what you want in the repositories. As with Fedora, graphical applications will put a link into the **Applications** menu.

### Graphical Tools

The **Synaptic package Manager** is an excellent tool for finding, fetching and installing packages. Press **System -> Administration -> Synaptic Package Manager** to start Synaptic.

### Command Line Tools

Ubuntu uses _apt-get_ instead of _yum_ , _up2date_ and so on to find, download, and install packages and their dependencies.

Note that, unlike yum, apt-get is only for packages available in repositories - it cannot handle packages you have already downloaded. The dpkg command is used instead.

### Table of Equivalent Commands

Below is a table of equivalent commands for package management on both Ubuntu/Debian and Red Hat/Fedora systems.

 **Task**

| 

 **Red Hat/Fedora**

| 

 **Ubuntu**  
  
---|---|---  
  
 **Adding, Removing and Upgrading Packages**  
  
Refresh list of available packages

| 

Yum refreshes each time it's used

| 

apt-get update  
  
Install a package from a repository

| 

yum install _package_name_

| 

apt-get install _package_name_  
  
Install a package file

| 

yum install _package.rpm_   
rpm -i _package.rpm_

| 

dpkg --install _package.deb_  
  
Remove a package

| 

rpm -e _package_name_

| 

apt-get remove _package_name_  
  
Check for package upgrades

| 

yum check-update

| 

apt-get -s upgrade   
apt-get -s dist-upgrade  
  
Upgrade packages

| 

yum update   
rpm -Uvh [args]

| 

apt-get dist-upgrade  
  
Upgrade the entire system

| 

yum upgrade

| 

apt-get dist-upgrade  
  
 **Package Information**  
  
Get information about an available package

| 

yum search _package_name_

| 

apt-cache search _package_name_  
  
Show available packages

| 

yum list available

| 

apt-cache dumpavail  
  
List all installed packages

| 

yum list installed   
rpm -qa

| 

dpkg --list  
  
Get information about a package

| 

yum info _package_name_

| 

apt-cache show _package_name_  
  
Get information about an installed package

| 

rpm -qi _package_name_

| 

dpkg --status _package_name_  
  
List files in an installed package

| 

rpm -ql _package_name_

| 

dpkg --listfiles _package_name_  
  
List documentation files in an installed package

| 

rpm -qd _package_name_

| 

-  
  
List configuration files in an installed package

| 

rpm -qc _package_name_

| 

-  
  
Show the packages a given package depends on

| 

rpm -qR _package_name_

| 

apt-cache depends  
  
Show other packages that depend on a   
given package (reverse dependency)

| 

rpm -q -whatrequires [args]

| 

apt-cache rdepends  
  
 **Package File Information**  
  
Get information about a package file

| 

rpm -qpi _package.rpm_

| 

dpkg --info _package.deb_  
  
List files in a package file

| 

rpm -qpl _package.rpm_

| 

dpkg --contents _package.deb_  
  
List documentation files in a package file

| 

rpm -qpd _package.rpm_

| 

-  
  
List configuration files in a package file

| 

rpm -qpc _package.rpm_

| 

-  
  
Extract files in a package

| 

rpm2cpio _package.rpm_ | cpio -vid

| 

dpkg-deb --extract _package.deb_ dir-to-extract-to  
  
Find package that installed a file

| 

rpm -qf _filename_

| 

dpkg --search _filename_  
  
Find package that provides a particular file

| 

yum provides _filename_

| 

apt-file search _filename_  
  
 **Misc. Packaging System Tools**  
  
Show stats about the package cache

| 

-

| 

apt-cache stats  
  
Verify all installed packages

| 

rpm -Va

| 

debsums  
  
Remove packages from the local cache directory

| 

yum clean packages

| 

apt-get clean  
  
Remove only obsolete packages from the local cache directory

| 

-

| 

apt-get autoclean  
  
Remove header files from the local cache directory   
(forcing a new download of same on next use)

| 

yum clean headers

| 

apt-file purge  
  
 **General Packaging System Information**  
  
Package file extension

| 

*.rpm

| 

*.deb  
  
Repository location configuration

| 

/etc/yum.conf

| 

/etc/apt/sources.list  
  
Some of the information in this table was derived (with permission) from [APT and RPM Packager Lookup Tables](http://www.jpsdomain.org/linux/apt.html).

More technical information about Debian-style packaging can be found in [Basics of the Debian package management system](http://www.debian.org/doc/FAQ/ch-pkg_basics.en.html)and the [Debian New Maintainers' Guide](http://www.debian.org/doc/manuals/maint-guide/index.en.html).

## Services

Services on Ubuntu are managed in a broadly similar way to those on Red Hat.

### Graphical Tools

Services can be configured by clicking **System** -> **Administration** -> **Services**. A tool called [Boot-Up Manager](http://www.marzocca.net/linux/bum.html) is also available.

### Command Line Tools

Below is a table of example commands for managing services. The _apache_ / _httpd_ service is used as an example.

 **Task**

| 

 **Red Hat / Fedora**

| 

 **Ubuntu**

| 

 **Ubuntu**   
(with sysv-rc-conf or sysvconfig)  
  
---|---|---|---  
  
 **Starting/stopping services immediately**

| 

service httpd start

| 

invoke-rc.d apache start

| 

service apache start  
  
 **Enabling a service at boot**

| 

chkconfig httpd on

| 

update-rc.d apache defaults

| 

sysv-rc-conf apache on  
  
 **Disabling a service at boot**

| 

chkconfig httpd off

| 

update-rc.d apache purge

| 

sysv-rc-conf apache off  
  
 **Note:** Whereas Red Hat and Fedora servers boot into runlevel 3 by default, Ubuntu servers default to runlevel 2.

 **Note:** The ` service` and `invoke-rc.d` commands call init scripts to do the actual work. You can also start and stop services by doing e.g. `/etc/init.d/apache start` on Ubuntu, or `/etc/init.d/httpd start` on Red Hat/Fedora.

## Network

### Graphical Tools

Fedora/RHEL have system-config-network, ubuntu pre 10.04 had [gnome-nettool](http://www.debianadmin.com/ubuntu-networking-for-basic-and-advanced-users.html) to edit static ip address, since 10.04 nm-connection-editor is the best choice. For Ubuntu 10.04 Studio there is only manual editing of files [since NetworkMontor is not included](https://bugs.launchpad.net/ubuntu/+source/gnome-system-tools/+bug/570828)

### Command Line Tools

* [ubuntu networking for basic and advanced users](http://www.debianadmin.com/ubuntu-networking-for-basic-and-advanced-users.html)

