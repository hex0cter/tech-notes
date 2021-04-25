
date: None  
author(s): None  

# [Find all large/big files on a Linux machine - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/linux)


    find / -type f -size +20000k -exec ls -lh {} \; | awk '{ print $9 ": " $5 }' find / -size +10240000c -exec du -h {} \;  
  
---

