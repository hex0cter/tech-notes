
date: None  
author(s): None  

# [win7家庭版显示或隐藏用户帐户 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/hide-account-in-windows-7-home-basic)

<http://wenwen.soso.com/z/q282483445.htm>   


首先关闭UAC，在控制面板里-用户帐户里面-选择”打开或关闭用户帐户控制” 去掉勾号，重启电脑。

如果想显示管理员，

1、使用安装时创建的帐号登陆windows7。  
2、开始—>所有程序—>附件—>在“命令提示符”上右击—>选择“以管理员身份运行”—>“允许” 。  
3、在打开的命令提示符窗口，输入”regedit”，回车，打开了注册表程序窗口。  
4、进入HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon  
5、在Winlogon上右击—>新建—项(k)，名称为SpecialAccounts  
6、在刚新建的SpecialAccounts上右击—>新建—>项(k)，名称为UserList  
7、在刚新建的UserList上右击—>新建—>DWORD (32-位)值(D)，名称为Administrator，然后双击它，把它的[键值](http://wenwen.soso.com/z/Search.e?sp=S%E9%94%AE%E5%80%BC&ch=w.search.yjjlink&cid=w.search.yjjlink)改为1  
8、在命令提示符窗口输入：net user administrator /active:yes 并回车。稍等就有成功提示。  
9、注销或重启，就可以看到超级管理员administrator账户显示出来了！默认没有密码，可以登录啦！  
 _  
【Daniel's note】其他用户不需要进行3-7部，只需将administrator改为相应的用户名即可。_

  
如果想禁用，在命令行cmd中输入：net user administrator /active:no  
  
---

