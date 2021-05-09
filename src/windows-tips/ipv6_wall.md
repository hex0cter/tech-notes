# [Windows 7 使用 IPv6 翻墙](http://vzone.me/system/ipv6-proxy-browsing-web.html)


Vista/Win7的方法是鼠标右键点击“开始－>程序－>附件－>命令提示符”，选择“以管理员身份运行”。
在新开启的【命令提示符】窗口中执行以下两条命令：


```
netsh interface ipv6 isatap set router isatap.sjtu.edu.cn
netsh interface ipv6 isatap set state enabled
```

替换 C:\Windows\System32\drivers\etc\hosts为附件中的内容。
