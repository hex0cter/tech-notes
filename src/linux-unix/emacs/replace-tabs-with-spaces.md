
date: None  
author(s): None  

# [replace tabs with spaces - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/replace-tabs-with-spaces)

http://dev-tricks.net/emacs-replace-tabs-with-spaces

Posted on [May 6, 2011](http://dev-tricks.net/emacs-replace-tabs-with-spaces) by [Julien Palard](http://dev-tricks.net/author/mandark)

When you want to replace tab with spaces or vice versa don’t use M-% (query-replace) but M-x tabify or M-x untabify. They work on the current selection so if you want it to be applied to a whole buffer, try C-x h (mark-whole-buffer) before to select the whole buffer.

  
  
  
---

