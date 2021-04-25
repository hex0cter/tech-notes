
date: None  
author(s): None  

# [How To Set Permanent DNS Nameservers in Ubuntu and Debian - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/how-to-set-permanent-dns-nameservers-in-ubuntu-and-debian)

The /etc/resolv.conf is the main configuration file for the DNS name resolver library. The resolver is a set of functions in the C library that provide access to the Internet Domain Name System (DNS). The functions are configured to check entries in the /etc/hosts file, or several DNS name servers, or to use the host’s database of Network Information Service (NIS).

On modern Linux systems that use systemd (system and service manager), the DNS or name resolution services are provided to local applications via the systemd-resolved service. By default, this service has four different modes for handling the Domain name resolution and uses the systemd DNS stub file (/run/systemd/resolve/stub-resolv.conf) in the default mode of operation.

The DNS stub file contains the local stub 127.0.0.53 as the only DNS server, and it is redirected to the /etc/resolv.conf file which was used to add the name servers used by the system.

If you run the following [ls command](https://www.tecmint.com/15-basic-ls-command-examples-in-linux/) on the /etc/resolv.conf, you will see that this file is a symlink to the /run/systemd/resolve/stub-resolv.conf file.
    
    
    $ ls -l /etc/resolv.conf lrwxrwxrwx 1 root root 39 Feb 15 2019 /etc/resolv.conf -> ../run/systemd/resolve/stub-resolv.conf
    

Unfortunately, because the /etc/resolv.conf is indirectly managed by the systemd-resolved service, and in some cases by the network service (by using initscripts or NetworkManager), any changes made manually by a user can not be saved permanently or only last for a while.

In this article, we will show how to install and use the resolvconf program to set permanent DNS name servers in /etc/resolv.conf file under Debian and Ubuntu Linux distributions.

### Why Would You Want to Ddit /etc/resolv.conf File?

The main reason could be because the systems DNS settings are misconfigured or you prefer to use specific name servers or your own. The following [cat command](https://www.tecmint.com/13-basic-cat-command-examples-in-linux/) shows the default name server in the /etc/resolv.conf file on my Ubuntu system.
    
    
    $ cat /etc/resolv.conf
    

[![Check DNS Name Servers](https://www.tecmint.com/wp-content/uploads/2019/10/Check-DNS-Name-Servers.png)](https://www.tecmint.com/wp-content/uploads/2019/10/Check-DNS-Name-Servers.png)

Check DNS Name Servers

In this case, when local applications such as the [APT package manager](https://www.tecmint.com/apt-advanced-package-command-examples-in-ubuntu/) try to access FQDNs (Fully Qualified Domain Names) on the local network, the result is a “Temporary failure in name resolution” error as shown in the next screenshot.

[![Temporary Failure Resolving](https://www.tecmint.com/wp-content/uploads/2019/10/Temporary-failure-resolving.png)](https://www.tecmint.com/wp-content/uploads/2019/10/Temporary-failure-resolving.png)

Temporary Failure Resolving

The same happens when you run a [ping command](https://www.tecmint.com/linux-ping-command-examples/).
    
    
    $ ping google.com
    

[![Temporary Failure in Name Resolution](https://www.tecmint.com/wp-content/uploads/2019/10/Temporary-Failure-in-Name-Resolution.png)](https://www.tecmint.com/wp-content/uploads/2019/10/Temporary-Failure-in-Name-Resolution.png)

Temporary Failure in Name Resolution

So when a user tries to manually set the name servers, the changes do not last for long or are revoked after a reboot. To resolve this, you can install and use the reolvconf utility to make the changes permanent.

To install the resolvconf package as shown in the next section, you need to first of all manually set the following name servers in the /etc/resolv.conf file, so that you access the FQDMs of Ubuntu repository servers on the internet.
    
    
    nameserver 8.8.4.4
    nameserver 8.8.8.8
    

Read Also: [How to Setup Local DNS Using /etc/hosts File in Linux](https://www.tecmint.com/setup-local-dns-using-etc-hosts-file-in-linux/)

### Installing resolvconf in Ubuntu and Debian

First, update the system software packages and then install resolvconf from the official repositories by running the following commands.
    
    
    $ sudo apt update
    $ sudo apt install resolvconf
    

Once the resolvconf installation is complete, systemd will trigger the resolvconf.service to be automatically started and enabled. To check if it is up and running issues the following command.
    
    
    $ sudo systemctl status resolvconf.service
    

If the service is not started and enabled automatically for any reason, you can start and enable it as follows.
    
    
    $ sudo systemctl start resolvconf.service
    $ sudo systemctl enable resolvconf.service
    $ sudo systemctl status resolvconf.service
    

[![Check Resolvconf Service Status](https://www.tecmint.com/wp-content/uploads/2019/10/start-enable-and-view-resolvconf-service-status.png)](https://www.tecmint.com/wp-content/uploads/2019/10/start-enable-and-view-resolvconf-service-status.png)

Check Resolvconf Service Status

#### Set Permanent DNS Nameservers in Ubuntu and Debian

Next, open the /etc/resolvconf/resolv.conf.d/head configuration file.
    
    
    $ sudo nano /etc/resolvconf/resolv.conf.d/head
    

and add the following lines in it:
    
    
    nameserver 8.8.8.8 
    nameserver 8.8.4.4
    

[![Set Permanent DNS Name Servers in Resolvconf](https://www.tecmint.com/wp-content/uploads/2019/10/set-name-servers-in-resolvconf-head-config-file.png)](https://www.tecmint.com/wp-content/uploads/2019/10/set-name-servers-in-resolvconf-head-config-file.png)

Set Permanent DNS Name Servers in Resolvconf

Save the changes and restart the resolvconf.service or reboot the system.
    
    
    $ sudo systemctl start resolvconf.service
    

Now when you check the /etc/resolv.conf file, the name server entries should be stored there permanently. Henceforth, you will not face any issues concerning name resolution on your system.

[![Permanent DNS Name Servers ](https://www.tecmint.com/wp-content/uploads/2019/10/permanent-name-servers-set.png)](https://www.tecmint.com/wp-content/uploads/2019/10/permanent-name-servers-set.png)

Permanent DNS Name Servers

I hope this quick article helped you in setting the permanent DNS nameservers in your Ubuntu and Debian systems. If you have any queries or suggestions, do share it with us in the comments section below.

