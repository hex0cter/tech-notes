
date: None  
author(s): None  

# [emacs, convert dos to unix and vice versa - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/emacs-convert-dos-to-unix-and-vice-versa)

<http://edivad.wordpress.com/2007/04/03/emacs-convert-dos-to-unix-and-vice-versa/>

If in emacs you need a different file coding system (line terminator), for example you are on a windows system and need to type a unix like text file (or vice versa), you can easily convert the _buffer coding system._

 **Dos to unix**

`M-x set-buffer-file-coding-system RET undecided-unix  
save the file (C-x C-s)`

or

`C-x RET f undecided-unix  
C-x C-f`

 **Unix to dos**

`M-x set-buffer-file-coding-system RET undecided-dos  
save the file (C-x C-s)`

or

`C-x RET f undecided-dos  
C-x C-f`  
  
---

