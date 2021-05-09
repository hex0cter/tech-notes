# replace tabs with spaces in vi

```
:setl expandtab
:retab 4

If this doesn't work, you could always try

:%s/\t/ /g
```
