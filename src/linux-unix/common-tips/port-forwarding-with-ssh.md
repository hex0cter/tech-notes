
date: None  
author(s): None  

# [Local port forwarding with SSH - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/port-forwarding-with-ssh)

ssh -C -L 127.0.0.1:8080:10.177.7.7:80 root@10.177.7.7

Now you should be able to visit 10.177.7.7:80 by accessing 127.0.0.1:8080. For example. if 10.177.7.7 has a web server, visiting 127.0.0.1:8080 in your browser will give you the same page as 10.177.7.7.  
  
---

