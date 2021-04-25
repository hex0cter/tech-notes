
date: None  
author(s): None  

# [Emacs Tips - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/emacs-tips)

1\. Start emacs in debugging mode:

2\. Check the value of your `load-path` by asking for help on the variable:

3\. Add your own load-path:
    
    
    (add-to-list 'load-path "/dir/subdir/")

Ref [http://www.gnu.org/software/emacs/emacs-faq.html](http://www.gnu.org/software/emacs/emacs-faq.html)

4\. Activate menu bar:

5\. Turn on color mode:

6\. To turn on color mode by default, add the following line in ~/.emacs:

`;; turn on font-lock mode`  
`(global-font-lock-mode t)`

`(setq font-lock-maximum-decoration t)`

  
7\. Jump to a particular line:

8\. Jump to the start/end of a block:

`C-M-f ``C-M-b or ``C-M-n ``C-M-p`

`M-x show-paren-mode`  


9\. Text Selection

Start  selection C-@

Copy  selected area Esc-w

Cut  selected area C-w

Paste  copied/cut area C-y

10\. Search the word under curor:

C-s C-w  
  
---

