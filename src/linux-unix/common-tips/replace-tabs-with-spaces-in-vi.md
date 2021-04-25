
date: None  
author(s): None  

# [replace tabs with spaces in vi - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/replace-tabs-with-spaces-in-vi)

:setl expandtab  
:retab 4

If this doesn't work, you could always try

:%s/\t/ /g  
  
---

