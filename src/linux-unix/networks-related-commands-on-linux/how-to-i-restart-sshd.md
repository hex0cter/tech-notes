
date: None  
author(s): None  

# [How to I restart sshd - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/networks-related-commands-on-linux/how-to-i-restart-sshd)

<http://www.starnet.com/xwin32kb/How_to_I_restart_sshd/>

After you have changed your configuration on your remote Unix/linux server you must restart your ssh service.

The easiest way to do this is to simply restart your Unix machine. This is not always possible however.

To restart sshd without restarting your whole system, enter the following command

**RedHat and Fedora Core Linux**  
service sshd restart

**Suse linux**  
/etc/rc.d/sshd restart

**Solaris 9 and below** /etc/init.d/sshd stop

/etc/init.d/sshd start

**Solaris 10** svcadm disable ssh

svcadm enable ssh

**AIX** stopsrc -s sshd

startsrc -s sshd

[Category:Sessions -> SSH](http://www.starnet.com/ee/index.php/xwin32kb/Category:Sessions::SSH/)  
  
---

