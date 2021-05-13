# [netcat examples](https://mylinuxbook.com/linux-netcat-command/)

## 1. Chatting room:
```
server> nc -vv -l -p 12000
client> nc -v 10.10.10.74 12000
```
## 2. remote shell
```
server> nc -vv -l -p 12000 -e /bin/bash
client> nc -v 10.10.10.74 12000
```
## 3. file transfer:
```
server> nc -l -p 12000 > newfile
client> nc 10.10.10.74 12000 < oldfile
```
## 4. port scan:
```
client> nc -z -v -n 10.10.10.10 21-25
```
## 5. server detection (any client simulator):
```
client> nc -vv 10.10.10.10 21
```
## 6. connect server from a particular port:
```
server> nc -vv -l -p 12000
client> nc 10.10.10.74 12000 -p 2000
```


<http://blog.jobbole.com/38067/>

<http://mylinuxbook.com/linux-netcat-command/>

<http://chronoslinux.org/wiki/Kernel_Programming_Tips#Netconsole>
