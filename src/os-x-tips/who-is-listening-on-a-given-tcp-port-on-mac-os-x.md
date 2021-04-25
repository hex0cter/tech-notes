
date: None  
author(s): None  

# [Who is listening on a given TCP port on Mac OS X? - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/os-x-tips/who-is-listening-on-a-given-tcp-port-on-mac-os-x)

http://stackoverflow.com/questions/4421633/who-is-listening-on-a-given-tcp-port-on-mac-os-x
    
    
    lsof -n -i4TCP:$PORT | grep LISTEN  
  
---

