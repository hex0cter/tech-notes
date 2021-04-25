
date: None  
author(s): None  

# [Who opened the port - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/networks-related-commands-on-linux/who-opened-the-port)

dpa@~> netstat -antpl | grep 8191

(Not all processes could be identified, non-owned process info

will not be shown, you would have to be root to see it all.)

tcp 0 0 127.0.0.1:8191 0.0.0.0:* LISTEN - 

tcp 1 0 127.0.0.1:43320 127.0.0.1:8191 CLOSE_WAIT 4635/java 

dpa@~> netstat -tonp | grep 8191

(Not all processes could be identified, non-owned process info

will not be shown, you would have to be root to see it all.)

tcp 1 0 127.0.0.1:43320 127.0.0.1:8191 CLOSE_WAIT 4635/java off (0.00/0/0)  
  
---

