
date: None  
author(s): None  

# [Debian Linux apt-get package management cheat sheet - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/package-management-on-linux/package-management/debian-linux-apt-get-package-management-cheat-sheet)

Both Debian and Ubuntu Linux provides a number of package management tools. This article summaries package management command along with it usage and examples for you.

(1) **apt-get** : APT is acronym for Advanced Package Tool. It supports installing packages over internet (ftp or http). You can also upgrade all packages in single operations, which makes it even more attractive.

(2) **dpkg** : Debian packaging tool which can be use to install, query, uninstall packages.

(3) Gui tools:You can also try GUI based or high level interface to the Debian GNU/Linux package system. Following list summaries them:

(1) [aptitude](http://www.cyberciti.biz/images/blogs/tips_tricks/aptitude030505.jpg): It is a text-based interface to the Debian GNU/Linux package system.

  
(2) [synaptic](http://www.cyberciti.biz/images/blogs/tips_tricks/synaptic.png): GUI front end for APT

Red hat Linux package names generally end in .rpml similarly Debian package names end in .deb, for example:  
apache_1.3.31-6_i386.deb

 **apache** : Package name  
 **1.3.31-6** : Version number  
 **i386** : Hardware Platform on which this package will run (i386 == intel x86 based system)  
 **.deb** : Extension that suggest it is a Debian package

Remember whenever I refer **.deb** file it signifies complete file name, and whenever I refer package name it must be first part of .deb file. For example when I refer to package sudo it means sudo only and not the .deb file i.e. sudo_1.6.7p5-2_i386.deb. However do not worry you can find out complete debian package list with the following command:  
apt-cache search {package-name}

## apt-get add a new package

Add a new package called samba  
Syntax: apt-get install {package-name}
    
    
    # apt-get install samba

## apt-get remove the package called samba but keep the configuration files

Syntax: apt-get remove {package-name}
    
    
    # apt-get remove samba

## apt-get remove (erase) package and configuration file

Syntax: apt-get --purge remove {package-name}
    
    
    # apt-get --purge remove samba

## apt-get Update (upgrade) package

Syntax: apt-get upgrade

To upgrade individual package called sudo, enter:  
`# apt-get install sudo`

## apt-get display available software updates

Following command will display the list of all available upgrades (updates) using -u option, if you decided to upgrade all of the shown packages just hit 'y'
    
    
    # apt-get upgrade samba

However if you just wish to upgrade individual package then use apt-get command and it will take care of rest of your worries:  
Syntax: apt-get install {package-name}

## dpkg command to get package information such as description of package, version etc.

Syntax: dpkg --info {.deb-package-name}
    
    
    # dpkg --info sudo_1.6.7p5-2_i386.deb | less

## List all installed packages

Syntax: dpkg -l
    
    
    # dpkg -l

## To list individual package try such as apache
    
    
    # dpkg -l apache

You can also use this command to see (verify) if package sudo is install or not (note that if package is installed then it displays package name along with small description):
    
    
    # dpkg -l | grep -i 'sudo'

To list packages related to the apache:
    
    
    # dpkg -l '*apache*'

List files provided (or owned) by the installed package (for example what files are provided by the installed samba package)  
Syntax: dpkg -L {package-name}
    
    
    # dpkg -L samba

(H) List files provided (or owned) by the package (for example what files are provided by the uninstalled sudo package)  
Syntax: dpkg --contents {.deb-package-name}
    
    
    # dpkg --contents sudo_1.6.7p5-2_i386.deb

## Find, what package owns the file /bin/netstat?

Syntax: dpkg -S {/path/to/file}
    
    
    # dpkg -S /bin/netstat

## Search for package or package description

Some times you don’t know package name but aware of some keywords to search the package. Once you got package name you can install it using apt-get -i {package-name} command:  
Syntax: apt-cache search "Text-to-search"

## Find out all the Debian package which can be used for Intrusion Detection
    
    
    # apt-cache search "Intrusion Detection"

Find out all sniffer packages
    
    
    # apt-cache search sniffer

## Find out if Debian package is installed or not (status)

Syntax: dpkg -s {package-name} | grep Status
    
    
    # dpkg -s samba| grep Status

## List ach dependency a package has...

Display a listing of each dependency a package has and all the possible other packages that can fulfill that dependency. You hardly use this command as apt-get does decent job fulfill all package dependencies.  
Syntax: apt-cache depends package

Display dependencies for lsof and mysql-server packages:
    
    
    # apt-cache depends lsof
    # apt-cache depends mysql-server

## Further reading

