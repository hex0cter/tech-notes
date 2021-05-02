# Linux和Windows 文件共享

**1,检查是否安装了samba软件**

用如下命令检查: `rpm –q samba`

**2,** 对samba进行设置 samba的设置文件位于：/etc/samba/smb.conf (需要有超级用户权限才能对此文件进行修改)。

要设置一个特定的共享目录，建议在smb.conf文件尾部增加一个全程单元。一般包括几条语句。下面是一个例子:
```
[share]
comment = my share
path = /home/share
valid users = administrator, win2ktest$
public = no
writable = yes
printable = no
create mask = 0765
```

说明： comment:提示，在windows的网络邻居上显示为备注。path：linux上共享目录 valid users: 允许访问linux共享目录的用户，此用户需是linux的samba用户 public：允许guest访问 writable: 允许用户写 printable: 若设为yes，则被认定为打印机 create mask：在共享目录上建立的文件的权限 每一个共享目录需要一个全程单元定义。 smb.conf修改完成后，建议用testparm来测试。如果运行OK就会列出可供装载的服务项，否则会给出出错信息。

注：在smb.conf修改完成后，需重启samba，才能使修改生效。以超级用户权限执行：`/sbin/service smb restart`

**3,samba用户设置**

以超级用户权限执行如下命令：
```
smbpasswd -a administrator
```

**4,samba的启动**

1) 在linux启动时自动启动

以超级用户权限修改/etc/rc.d/rc.local在文件尾部加入一条语句如下：
```
service smb restart
```

2) 用命令启动samba
以超级用户特权执行：`/sbin/service smb restart`


**5, 查看samba的状态**
```
/sbin/service smb status
```

<http://topic.csdn.net/t/20041016/00/3461169.html>

<http://www.wangchao.net.cn/bbsdetail_26898.html>
