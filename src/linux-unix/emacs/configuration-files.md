# configuration file

```
[daniel@daniel-laptop:~$](mailto:daniel@daniel-laptop:~$) cat .emacs

;;add private load-path
(add-to-list 'load-path "/home/daniel/.emacs.d/site-lisp")

;;toggle F5 as the shortkey to speedbar
(global-set-key [(f5)] 'speedbar)

;;need cscope for development
(require 'xcscope)

;;do not update tags database before each search to speed up cscope
(setq cscope-do-not-update-database t)

[daniel@daniel-laptop:~$](mailto:daniel@daniel-laptop:~$)
```
