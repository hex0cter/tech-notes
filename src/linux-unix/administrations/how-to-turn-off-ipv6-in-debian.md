
date: None  
author(s): None  

# [How to turn off IPv6 in Debian - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/how-to-turn-off-ipv6-in-debian)

<http://wiki.debian.org/DebianIPv6#How_to_turn_off_IPv6>

### In squeeze

  * Disable ipv6 in kernel : _echo net.ipv6.conf.all.disable_ipv6=1 > /etc/sysctl.d/disableipv6.conf_ will disable ipv6 at next reboot.

    * fetchmail will stop sending dns AAAA queries.
    * If you've built a custom kernel with IPv6 as a module be aware that due to a race condition with the init scripts you'll need to load the ipv6 module before the procps init script is run (see /usr/share/doc/procps/README.Debian and [507788](http://bugs.debian.org/507788))

    * You will probably need to comment-out any IPv6 address in /etc/hosts (especially the one for loopback) otherwise ssh will fail to forward ports (or you must always use -4 to ssh).
  * In exim4:
    * put _disable_ipv6 = true_ into your exim configuration file

    * run _update-exim4.conf_

    * then restart exim4
  * In sshd:
    * put _[AddressFamily](http://wiki.debian.org/AddressFamily) inet_ into /etc/ssh/sshd_config

    * restart sshd: /etc/init.d/ssh restart
  * Change /etc/avahi/avahi-daemon.conf to say _use-ipv6=no_


  
  
---

