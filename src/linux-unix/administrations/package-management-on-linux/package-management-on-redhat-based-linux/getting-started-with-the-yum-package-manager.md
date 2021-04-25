
date: None  
author(s): None  

# [Getting started with the yum package manager - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/package-management-on-linux/package-management-on-redhat-based-linux/getting-started-with-the-yum-package-manager)

_Vincent Danen introduces you to the yum package manager, including basic configuration and some common commands._

——————————————————————————

There are a variety of package managers available for different Linux distributions. Mandriva uses urpmi; Debian and Ubuntu use apt. Fedora and Red Hat use yum, while Gentoo uses portage. Some distributions provide support for more than one package manager as well.

This week, we take a look at yum, or Yellowdog Updater Modified. Yum is written in python and has been in use with Fedora and Red Hat for many years. Yum has been proven to work, and despite some criticism as to its speed in comparison to other package mangers, it does the job, even if it is a little bit slower.

The main yum configuration file is _/etc/yum.conf_ and per-repository configuration files live in the _/etc/yum.repos.d/ directory_. These files, as installed, are largely sufficient as the Red Hat/Fedora installer takes care of adding update sources. Unless you plan on adding other repositories or have a need to tweak certain configuration settings, these configuration files work as-is. If you would like to figure out the various options and tweak the configuration file, the yum.conf(5) manpage will help you there.

Yum itself is quite straightforward. Most individuals will likely use graphical frontends to yum, but knowing the yum commands directly is a great idea in case X is not working or you are working remotely on a server.

To install a package with yum, use the install command:
    
    
    # yum install zsh

This will install the zsh package and any dependencies it may have. You can specify more than one package at a time to install (i.e., _yum install zsh joe_ ).

If you are not sure what a package is called, you can search the repository metadata using yum’s search command. For instance, if you are working with some python code and need the MySQL interface available, but don’t have it installed and really don’t know what it is called, search for it:
    
    
    # yum search MySQL | grep python

With this command, you are searching for any package related to MySQL, and then filtering that list for those packages that contain the word _python_. The first hit on that search is MySQL-python, which would be the package you are looking for.

If you want to list an available package, you can use the _list_ command. This will list all available packages and note which are installed. This is useful particularly if you are using a 64-bit distribution and may require a 32-bit package. For instance:
    
    
    # yum list openssl
    
    
    Loaded plugins: refresh-packagekit
    
    
    Installed Packages
    
    
    openssl.x86_64                                                        0.9.8g-12.fc10                                                         installed
    
    
    Available Packages
    
    
    openssl.i386                                                          0.9.8g-12.fc10                                                         updates
    
    
    openssl.i686                                                          0.9.8g-12.fc10                                                         updates

To upgrade packages, either specify the package to upgrade with the _update_ command or do not specify any packages to upgrade everything that has an updated package available:
    
    
    # yum update

And finally, a few other quick commands. To remove a package from the system, use the _remove_ command. This will remove the noted package as well as any requirements for that package that are no longer required by other packages. To get full information on a package, such as version, architecture, and a description, use _yum info [package]_. To find out if any package needs to be upgraded, but without performing any upgrade actions, use _yum check-update_ and a list of available updates will be printed.

Overall, yum is a decent package manager. It doesn’t feel as fast as urpmi, but it does feel more polished. If you are used to other package managers, it may take some time to remember the commands, but the manpage that accompanies it is very well written and easy to understand.

Get the [PDF version](http://downloads.techrepublic.com.com/abstract.aspx?docid=938271) of this tip here.

 _Delivered each Tuesday, TechRepublic’s free Linux and Open Source newsletter provides tips, articles, and other resources to help you hone your Linux skills.[Automatically sign up today!](http://nl.com.com/MiniFormHandler?brand=techrepublic&list_id=e011)_

