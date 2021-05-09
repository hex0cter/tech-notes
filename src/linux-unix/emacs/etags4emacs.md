# [etags 用法](http://blog.csdn.net/fyzhao/archive/2009/10/13/4658132.aspx)

## 1. etags 基本用法
在emacs里可以用etags命令生成emacs专用的tags文件，有了此文件之后便可以使用一些emacs tags的命令，比如对于编辑C/C++程序的人员可以方便的定位一个函数的定义，或者对函数名进行自动补齐：

```
find . -name "*.cpp" -print -o -name "*.h" -print | etags -
```
上述命令可以在当前目录查找所有的.h和.cpp文件并把它们的摘要提取出来做成TAGS文件，具体的etags的用法可以看一下etags的manual。

在.emacs中加入这样的语句：
```
(setq tags-file-name "{/SOURCE/CODE/PATH}/TAGS")
```

这样emacs就会自动读取这个tags文件的内容。

几个重要的命令。

  * M-. 查找一个tag，比如函数定义类型定义等。
  * C-u M-. 查找下一个tag的位置
  * M-* 回到上一次运行M-.前的光标位置。
  * M-TAB 自动补齐函数名。

## 2. 参考：一些整合的快捷键

易于编译和TAGS的使用，搜集自 zslevin 的帖子(LinuxForum GNU Emacs/XEmacs)

  * C-f5, 设置编译命令
  * f5, 保存当前窗口然后编译当前窗口文件


```
(defun du-onekey-compile ()
"Save buffers and start compile"
(interactive)
(save-some-buffers t)
(compile compile-command))
(global-set-key [C-f5] 'compile)
(global-set-key [f5] 'du-onekey-compile)
```


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

```
(global-set-key [(f7)] 'visit-tags-table) ; visit tags table
(global-set-key [C-f7] 'sucha-generate-tag-table) ; generate tag table
(global-set-key [(control .)] '(lambda () (interactive) (lev/find-tag t)))
(global-set-key [(control ,)] 'sucha-release-small-tag-window)
(global-set-key [(meta .)] 'lev/find-tag)
(global-set-key [(meta ,)] 'pop-tag-mark)
(global-set-key (kbd "C-M-,") 'find-tag)
(define-key lisp-mode-shared-map [(shift tab)] 'complete-tag)
(add-hook 'c-mode-common-hook ; both c and c++ mode
  (lambda ()
    (define-key c-mode-base-map [(shift tab)] 'complete-tag)))
```


上面定义的命令需要用到的函数：


```
(defun lev/find-tag (&optional show-only)
  "Show tag in other window with no prompt in minibuf."
  (interactive)
  (let ((default (funcall (or find-tag-default-function
                              (get major-mode 'find-tag-default-function)
                              'find-tag-default))))
    (if show-only
        (progn (find-tag-other-window default)
               (shrink-window (- (window-height) 12)) ;; 限制为 12 行
               (recenter 1)
               (other-window 1))
      (find-tag default))))

(defun sucha-generate-tag-table ()
  "Generate tag tables under current directory(Linux)."
  (interactive)
  (let
      ((exp "")
       (dir ""))
    (setq dir
          (read-from-minibuffer "generate tags in: " default-directory)
          exp
          (read-from-minibuffer "suffix: "))
    (with-temp-buffer
      (shell-command
       (concat "find " dir " -name \"" exp "\" | xargs etags ")
       (buffer-name)))))

(defun sucha-release-small-tag-window ()
  "Kill other window also pop tag mark."
  (interactive)
  (delete-other-windows)
  (ignore-errors
    (pop-tag-mark)))
```
