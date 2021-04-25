
date: None  
author(s): None  

# [etags 用法 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/emacs/etags4emacs)

在emacs里可以用etags命令生成emacs专用的tags文件，有了此文件之后便可以使用一些emacs tags的命令，比如对于编辑C/C++程序的人员可以方便的定位一个函数的定义，或者对函数名进行自动补齐：

上述命令可以在当前目录查找所有的.h和.cpp文件并把它们的摘要提取出来做成TAGS文件，具体的etags的用法可以看一下etags的manual。

在.emacs中加入这样的语句：

这样emacs就会自动读取这个tags文件的内容。

几个重要的命令。

  * M-. 查找一个tag，比如函数定义类型定义等。
  * C-u M-. 查找下一个tag的位置
  * M-* 回到上一次运行M-.前的光标位置。
  * M-TAB 自动补齐函数名。



## 2\. 参考：一些整合的快捷键

易于编译和TAGS的使用，搜集自 zslevin 的帖子(LinuxForum GNU Emacs/XEmacs)

  * C-f5, 设置编译命令
  * f5, 保存当前窗口然后编译当前窗口文件



[view plain](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[copy to clipboard](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[print](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[?](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)

  1. (defun du-onekey-compile () 
  2. "Save buffers and start compile" 
  3. (interactive) 
  4. (save-some-buffers t) 
  5. (compile compile-command)) 
  6. (global-set-key [C-f5] 'compile) 
  7. (global-set-key [f5] 'du-onekey-compile) 



  * F7, 查找 TAGS 文件（更新 TAGS 表）
  * C-F7, 在当前目录下生成包含所有递归子目录的 TAGS 文件（使用了shell中的find命令）
  * C-. 开个小窗查看光标处的 tag
  * C-, 只留下当前查看代码的窗口（关闭查看 tag 的小窗）
  * M-. 查找光标处的 tag，并跳转
  * M-, 跳回原来查找 tag 的地方
  * C-M-, 提示要查找的 tag，并跳转
  * C-M-. 要匹配的 tag 表达式（系统已定义）
  * Shift-Tab, C/C++ 和 lisp 等模式中补全函数名（一般情况下M-Tab被窗口管理器遮屏了）



定义按键，在生成相应 tag 文件时，比如一个目录下所有的 *.cpp 和 *.h 文件使用这样的正则表达式 *.[ch]*，在下面的 C-F7 中可能会用到。

[view plain](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[copy to clipboard](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[print](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[?](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)

  1. (global-set-key [(f7)] 'visit-tags-table) ; visit tags table 
  2. (global-set-key [C-f7] 'sucha-generate-tag-table) ; generate tag table 
  3. (global-set-key [(control .)] '(lambda () (interactive) (lev/find-tag t))) 
  4. (global-set-key [(control ,)] 'sucha-release-small-tag-window) 
  5. (global-set-key [(meta .)] 'lev/find-tag) 
  6. (global-set-key [(meta ,)] 'pop-tag-mark) 
  7. (global-set-key (kbd "C-M-,") 'find-tag) 
  8. (define-key lisp-mode-shared-map [(shift tab)] 'complete-tag) 
  9. (add-hook 'c-mode-common-hook ; both c and c++ mode 
  10. (lambda () 
  11. (define-key c-mode-base-map [(shift tab)] 'complete-tag))) 



上面定义的命令需要用到的函数：

[view plain](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[copy to clipboard](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[print](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)[?](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx#)

  1. (defun lev/find-tag (&optional show-only) 
  2. "Show tag in other window with no prompt in minibuf." 
  3. (interactive) 
  4. (let ((default (funcall (or find-tag-default-function 
  5. (get major-mode 'find-tag-default-function) 
  6. 'find-tag-default)))) 
  7. (if show-only 
  8. (progn (find-tag-other-window default) 
  9. (shrink-window (- (window-height) 12)) ;; 限制为 12 行 
  10. (recenter 1) 
  11. (other-window 1)) 
  12. (find-tag default)))) 
  13.   14. (defun sucha-generate-tag-table () 
  15. "Generate tag tables under current directory(Linux)." 
  16. (interactive) 
  17. (let 
  18. ((exp "") 
  19. (dir "")) 
  20. (setq dir 
  21. (read-from-minibuffer "generate tags in: " default-directory) 
  22. exp 
  23. (read-from-minibuffer "suffix: ")) 
  24. (with-temp-buffer 
  25. (shell-command 
  26. (concat "find " dir " -name \"" exp "\" | xargs etags ") 
  27. (buffer-name))))) 
  28.   29. (defun sucha-release-small-tag-window () 
  30. "Kill other window also pop tag mark." 
  31. (interactive) 
  32. (delete-other-windows) 
  33. (ignore-errors 
  34. (pop-tag-mark))) 



[](http://blog.csdn.net/fyzhao/archive/2009/10/13/Doc/Etags?action=sourceblock&ref=4)

http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx  
  
---

