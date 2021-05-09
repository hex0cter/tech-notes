# [Speed up cscope in emacs](http://www.linuxforum.net/forum/showthreaded.php?Cat=&Board=vim&Number=648083&page=&view=&sb=&o=)


在emacs里cscope为什么这么慢？ [re: doudoumeter]

不是再查一遍，而是重新建一次数据库。

这样做的好处是你在emacs里修改文件后，cscope能够反应最新的代码。

缺点就是慢（不过项目不大的情况下感觉不出来）。

解决办法（如果用的是xcscope.el）：

```
;; xcscope for cscope
(require 'xcscope)
(setq cscope-do-not-update-database t)
```
