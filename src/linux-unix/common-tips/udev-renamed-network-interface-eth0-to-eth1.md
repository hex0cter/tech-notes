
date: None  
author(s): None  

# [udev: renamed network interface eth0 to eth1 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/udev-renamed-network-interface-eth0-to-eth1)

<http://lists.debian.org/debian-user/2010/08/msg00058.html>
    
    
    Take a look at /etc/udev/rules.d/70-persistent-net.rules and verify that
    the rule for your card (check its MAC) is consistent with the naming
    scheme you want.
    
    You can easily edit that file or even remove it if you want to
    regenerate it from scratch.  
  
---

