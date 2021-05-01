# dpkg command cheat sheet for Debian Linux

dpkg is package manager for Debian Linux which is use to install/manage individual packages. Here is quick cheat sheet you will find handy while using dpkg at shell prompt:

|  **Syntax**|  **Description**|  **Example**
---|---|---
dpkg -i {.deb package}| Install the package| dpkg -i zip_2.31-3_i386.deb
dpkg -i {.deb package}| Upgrade package if it is installed else install a fresh copy of package| dpkg -i zip_2.31-3_i386.deb
dpkg -R {Directory-name}| Install all packages recursively from directory| dpkg -R /tmp/downloads
dpkg -r {package}| Remove/Delete an installed package except configuration files| dpkg -r zip
dpkg -P {package}| Remove/Delete everything including configuration files| dpkg -P apache-perl
dpkg -l| List all installed packages, along with package version and short description| dpkg -ldokg -l <br> lessdpkg -l '*apache*' <br> dpkg -l | grep -i 'sudo'
dpkg -l {package}| List individual installed packages, along with package version and short description| dpkg -l apache-perl
dpkg -L {package}| Find out files are provided by the installed package i.e. list where files were installed| dpkg -L apache-perl
dpkg -L perl
dpkg -c {.Deb package}| List files provided (or owned) by the package i.e. List all files inside debian .deb package file, very useful to find where files would be installed| dpkg -c dc_1.06-19_i386.deb
dpkg -S {/path/to/file}| Find what package owns the file i.e. find out what package does file belong| dpkg -S /bin/netstat
dpkg -S /sbin/ippool
dpkg -p {package}| Display details about package package group, version, maintainer, Architecture, display depends packages, description etc| dpkg -p lsof
dpkg -s {package} | grep Status| Find out if Debian package is installed or not (status)| dpkg -s lsof | grep Status

{package} - Replace with actual package name
