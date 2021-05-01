# How to mount remote windows partition (windows share) under Linux

<http://www.howtogeek.com/wiki/Mount_a_Windows_Shared_Folder_on_Linux_with_Samba>

<http://www.cyberciti.biz/tips/how-to-mount-remote-windows-partition-windows-share-under-linux.html>

```
sudo mount -t cifs //VALINE/Projects -o domain=mydomain,username=myusername,password=mypasswd /mnt/ntserver
```
