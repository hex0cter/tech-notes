# [convert small letters to capital letters](http://www.unix.com/shell-programming-scripting/25063-change-parameter-capital-letters.html)


1.

```
$mah="hello"
$ typeset -u mah
$ echo $mah
```

2.
```
sid=`echo $sid | tr '[a-z]' '[A-Z]'`
```
