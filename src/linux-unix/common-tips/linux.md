# Find all large/big files on a Linux machine

```
    find / -type f -size +20000k -exec ls -lh {} \; | awk '{ print $9 ": " $5 }' find / -size +10240000c -exec du -h {} \;
```
