
date: None  
author(s): None  

# [Find most recently updated files on Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/find-most-recently-updated-files-on-linux)

http://stackoverflow.com/questions/10575665/linux-find-command-find-10-latest-files-recursively-regardless-of-time-span  

    
    
    find . -type f -printf '%T@ %p\n' | sort -n | tail -10 |  
  
---

