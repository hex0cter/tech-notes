# [Change login screen on Windows 7](http://blog.chdzone.cn/20100922279.html)

无需任何软件，简单修改Win7开机登陆界面背景图片，让您的电脑更为个性。

```
[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\Background]
```
右侧新建一个双字节值“OEMBackground”（OEM版本的Win7已经有这个键值）→右击该双字节值→“修改”将键值修改为“0”。
