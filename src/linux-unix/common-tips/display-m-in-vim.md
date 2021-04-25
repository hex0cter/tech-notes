
date: None  
author(s): None  

# [display ^M in vim - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/display-m-in-vim)

http://stackoverflow.com/questions/3852868/how-to-make-vim-show-m-and-substitute-it

| | 

:e ++ff=unix

## Substitute CRLF for LF:

:setlocal ff=unix:w

:e  
  
---|---

