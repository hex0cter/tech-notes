
date: None  
author(s): None  

# [add domain name to hostname automatically when connecting to remote server - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/add-domain-name-to-hostname-automatically-when-connecting-to-remote-server)

http://askubuntu.com/questions/58781/resolv-conf-keeps-getting-reset-by-something

 _1\. Before change:_

danielh@ubuntu ~ $ ping zsi3

ping: unknown host zsi3

 _2\. after change:_

danielh@ubuntu ~ $ ping zsi3

PING zsi3.internet (10.216.21.168) 56(84) bytes of data.

64 bytes from zsi3.sto1.3s.intern (10.216.21.168): icmp_seq=1 ttl=255 time=1.51 ms

Here is the change:

`danielh@ubuntu ~ $ sudo vi /etc/resolv.conf`

`search sto.internet`

`nameserver 127.0.1.1`

sudo resolvconf -u  
  
---

