
date: None  
author(s): None  

# [rpm command cheat sheet for Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/package-management-on-linux/package-management-on-redhat-based-linux/rpm-command-cheat-sheet-for-linux)

pm is a powerful Package Manager for Red Hat, Suse and Fedora Linux. It can be used to build, install, query, verify, update, and remove/erase individual software packages. A Package consists of an archive of files, and package information, including name, version, and description:

|  **Syntax**|  **Description**|  **Example(s)**  
---|---|---  
rpm -ivh {rpm-file}| Install the package| rpm -ivh mozilla-mail-1.7.5-17.i586.rpm  
rpm -ivh --test mozilla-mail-1.7.5-17.i586.rpm  
rpm -Uvh {rpm-file}| Upgrade package| rpm -Uvh mozilla-mail-1.7.6-12.i586.rpm  
rpm -Uvh --test mozilla-mail-1.7.6-12.i586.rpm  
rpm -ev {package}| Erase/remove/ an installed package| rpm -ev mozilla-mail  
rpm -ev --nodeps {package}| Erase/remove/ an installed package without checking for dependencies| rpm -ev --nodeps mozilla-mail  
rpm -qa| Display list all installed packages| rpm -qa  
rpm -qa | less  
rpm -qi {package}| Display installed information along with package version and short description| rpm -qi mozilla-mail  
rpm -qf {/path/to/file}| Find out what package a file belongs to i.e. find what package owns the file| rpm -qf /etc/passwd  
rpm -qf /bin/bash  
rpm -qc {pacakge-name}| Display list of configuration file(s) for a package| rpm -qc httpd  
rpm -qcf {/path/to/file}| Display list of configuration files for a command| rpm -qcf /usr/X11R6/bin/xeyes  
rpm -qa --last| Display list of all recently installed RPMs| rpm -qa --last  
rpm -qa --last | less  
rpm -qpR {.rpm-file}  
rpm -qR {package}| Find out what dependencies a rpm file has| rpm -qpR mediawiki-1.4rc1-4.i586.rpm  
rpm -qR bash  
  
{package} - Replace with actual package name

Q. How do I find out what files are in RPM package called gnupg?

A. You can use rpm command itself to list the files inside a RPM package. rpm is a powerful Package Manager, which can be used to build, install, query, verify, update, and erase individual software packages. A package consists of an archive of files and meta-data used to install and erase the archive files.

Use following syntax to list the files for already INSTALLED package:  
 **rpm -ql package-name**

Use following syntax to list the files for RPM package:  
 **rpm -qlp package.rpm **Type the following command to list the files for gnupg rpm package:

`$ rpm -qlp rpm -qlp gnupg-1.4.5-1.i386.rpm`

  
Output:
    
    
    /usr/bin/gpg
    /usr/bin/gpgsplit
    /usr/bin/gpgv
    /usr/bin/lspgpot
    /usr/lib64/gnupg
    /usr/lib64/gnupg/gpgkeys_ldap
    /usr/lib64/gnupg/gpgkeys_mailto
    /usr/share/doc/gnupg-1.2.6
    /usr/share/doc/gnupg-1.2.6/AUTHORS
    /usr/share/doc/gnupg-1.2.6/BUGS
    /usr/share/doc/gnupg-1.2.6/COPYING
    /usr/share/doc/gnupg-1.2.6/ChangeLog
    /usr/share/doc/gnupg-1.2.6/DETAILS
    /usr/share/doc/gnupg-1.2.6/HACKING
    /usr/share/doc/gnupg-1.2.6/INSTALL
    /usr/share/doc/gnupg-1.2.6/NEWS
    ....
    ..
    ...

<http://www.cyberciti.biz/howto/question/linux/linux-rpm-cheat-sheet.php>

<http://www.cyberciti.biz/faq/howto-list-find-files-in-rpm-package/>

