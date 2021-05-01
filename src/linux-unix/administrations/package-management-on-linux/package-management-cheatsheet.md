# [Package Management Cheatsheet](http://lpilinux.com/package-management-cheatsheet.htmlt)

The following table lists package management tasks in the four most popular distribution groups – Debian (including Ubuntu, Linux Mint, KNOPPIX, sidux and other Debian derivatives), openSUSE, Fedora (including Red Hat Enterprise Linux, CentOS, Scientific Linux and other Fedora-based distributions), and Mandriva Linux.

Task| apt (deb)  Debian, Ubuntu| zypp (rpm) openSUSE| yum (rpm) Fedora, CentOS| urpmi (rpm) Mandriva
---|---|---|---|---
 **Managing software**| | | |
Install new software from package repository| apt-get install _pkg_|  zypper install _pkg_|  yum install _pkg_|  urpmi _pkg_
Install new software from package file| dpkg -i _pkg_|  zypper install _pkg_|  yum localinstall _pkg_|  urpmi _pkg_
Update existing software| apt-get install _pkg_|  zypper update -t package _pkg_|  yum update _pkg_|  urpmi _pkg_
Remove unwanted software| apt-get remove _pkg_|  zypper remove _pkg_|  yum erase _pkg_|  urpme _pkg_
 **Updating the system**| | | |
Update package list| apt-get update
aptitude update| zypper refresh| yum check-update| urpmi.update -a
Update system| apt-get upgrade
aptitude safe-upgrade| zypper update| yum update| urpmi –auto-select
 **Searching for packages**| | | |
Search by package name| apt-cache search _pkg_|  zypper search _pkg_|  yum list _pkg_|  urpmq _pkg_
Search by pattern| apt-cache search _pattern_|  zypper search -t pattern _pattern_|  yum search _pattern_|  urpmq –fuzzy _pkg_
Search by file name| apt-file search _path_|  zypper wp _file_|  yum provides _file_|  urpmf _file_
List installed packages| dpkg -l| zypper search -is| rpm -qa| rpm -qa
 **Configuring access to software repositories**| | | |
List repositories| cat /etc/apt/sources.list| zypper repos| yum repolist| urpmq –list-media
Add repository| (edit /etc/apt/sources.list)| zypper addrepo _path_ _name_|  (add _repo_ to /etc/yum.repos.d/)|  urpmi.addmedia _name_ _path_
Remove repository| (edit /etc/apt/sources.list)| zypper removerepo _name_|  (remove _repo_ from /etc/yum.repos.d/)| urpmi.removemedia _media_
