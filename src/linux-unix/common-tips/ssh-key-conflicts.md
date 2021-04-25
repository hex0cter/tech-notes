
date: None  
author(s): None  

# [SSH key conflicts - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/ssh-key-conflicts)

ssh-keygen -f "/home/dhan/.ssh/known_hosts" -R 10.177.124.105

dhan@dhan-ubuntu:~$ ssh root@10.177.124.105

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED! @

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!

Someone could be eavesdropping on you right now (man-in-the-middle attack)!

It is also possible that a host key has just been changed.

The fingerprint for the RSA key sent by the remote host is

4f:48:c2:6f:72:04:00:f5:56:a9:a4:ad:f4:fe:8e:37.

Please contact your system administrator.

Add correct host key in /home/dhan/.ssh/known_hosts to get rid of this message.

Offending RSA key in /home/dhan/.ssh/known_hosts:5

remove with: **ssh-keygen -f "/home/dhan/.ssh/known_hosts" -R 10.177.124.105**

RSA host key for 10.177.124.105 has changed and you have requested strict checking.

Host key verification failed.  
  
---

