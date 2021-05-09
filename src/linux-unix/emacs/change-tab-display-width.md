# [Change tab display width](http://stackoverflow.com/questions/69934/set-4-space-indent-in-emacs-in-text-mode)

```
M-x set-variable
Set variable: tab-width
```

This change the display width.

To change it permenantly, try (not verified):

```
(setq-default indent-tabs-mode nil)
(setq-default tab-width 4)
(setq indent-line-function 'insert-tab)
```
