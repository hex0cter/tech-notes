
date: None  
author(s): None  

# [Close a listening port opened by hanging ssh tunnel - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/close-a-listening-port-opened-by-hanging-ssh-tunnel)

This concerns only the port opened by an SSH tunnel. For other ports, follow [this instruction](http://superuser.com/questions/127863/manually-closing-a-port-from-commandline).

`$`` `**`who`**

`dpa pts/0 2013-08-05 12:51 (10.216.6.218)`

`dpa pts/1 2013-08-06 11:38 (10.216.6.218)`

`dpa pts/2 2013-08-06 10:27 (10.216.6.218)`

`$`` `**`netstat -an | grep 8191`**

`tcp 0 0 127.0.0.1:8191 0.0.0.0:* LISTEN - `

`$ `**`skill -9 -t pts/1`**

`$`` `**`netstat -an | grep 8191`**

`$`` `

The **_skill_** command will kick out a logged-in user. In this case it will close an SSH session by force.  
  
---

