# [Find most recently updated files on Linux](http://stackoverflow.com/questions/10575665/linux-find-command-find-10-latest-files-recursively-regardless-of-time-span)


```
    find . -type f -printf '%T@ %p\n' | sort -n | tail -10 |
```
