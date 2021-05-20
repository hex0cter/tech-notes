# [How to check the open file limits](https://stackoverflow.com/questions/34588/how-do-i-change-the-number-of-open-files-limit-in-linux/34645)

## check currently limit
```
ulimit -n
```

## Check hard limit
```
ulimit -Hn
```

## Check soft limit
```
ulimit -Sn
```

## Update it for the current shell:
```
ulimit -c unlimited
```
or
```
ulimit -c 1048576
```

## Update it permenently:
```
vi /etc/security/limits.conf # or /etc/limits.conf
```
Add the following line
```
*                soft    nofile         unlimited
```

[How to enable core dumps](http://www.akadia.com/services/ora_enable_core.html)
