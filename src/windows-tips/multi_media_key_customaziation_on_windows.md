
date: None  
author(s): None  

# [键盘多媒体键的一些研究心得 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/multi_media_key_customaziation_on_windows)

**前言** 最近对键盘的多媒体键产生了兴趣，研究了一些心得，特此记录下来与大家分享。

本文共分为以下四个部分：  
² 多媒体键简介  
² 定制多媒体键  
² 定制键盘任意键  
² 改造普通键盘硬件，增加多媒体键

 **多媒体键简介**

目前最常用的标准键盘是104键键盘，是在IBM定义的101键键盘标准上增加了两个Windows徽标键和一个右键菜单键而成，俗称Win95键盘。此类键盘一直沿用IBM标准，采用行列矩阵方式布局排列，称为扫描矩阵，扫描矩阵定义为8行×16列＝128键。对于104键键盘而言，还有24个闲置键位未定义。107键键盘就是从这些闲置键位中选择了三个定义为“Power”、“Sleep”和“Wake UP”。后来微软又增加了18个键定义，用于完成音量调整、播放/暂停、打开浏览器等功能，相关文档参见：<http://www.microsoft.com/whdc/archive/w2kbd.mspx>。为了方便，本文中我们将这18个键统称为多媒体键，各键功能详见下表：

  


| 

 **序号**

| 

 **键名**

| 

 **功能**

| 

 **注册表分支名称**  
  
---|---|---|---  
  
1

| 

Volume UP

| 

音量提高

|   
  
2

| 

Volume Down

| 

音量降低

|   
  
3

| 

Mute

| 

静音

|   
  
4

| 

Play/Pause

| 

播放/暂停

|   
  
5

| 

Stop

| 

停止

|   
  
6

| 

Scan Previous Track

| 

上一曲

|   
  
7

| 

Scan Next Track

| 

下一曲

|   
  
8

| 

WWW Back

| 

IE浏览器后退

| 

1  
  
9

| 

WWW Forward

| 

IE浏览器前进

| 

2  
  
10

| 

WWW Refresh

| 

IE浏览器刷新

| 

3  
  
11

| 

WWW Stop

| 

IE浏览器停止

| 

4  
  
12

| 

WWW Search

| 

IE浏览器搜索

| 

5  
  
13

| 

WWW Favorites

| 

IE浏览器收藏夹

| 

6  
  
14

| 

WWW Home

| 

IE浏览器首页

| 

7  
  
15

| 

Mail

| 

邮件

| 

15  
  
16

| 

Media Select

| 

媒体选择（播放器）

| 

16  
  
17

| 

My Computer

| 

我的电脑

| 

17  
  
18

| 

Calculator

| 

计算器

| 

18  
  
  
微软、罗技等一些厂家都推出过各式各样的带有多媒体键的键盘，有音量调节、播放、停止、计算器、复制、粘贴、备份、还原等多种功能，但有相当一部分各类的键盘需要另行安装驱动程序或应用程序。本文所讨论的多媒体键盘，仅指在XP/Vista/Windows7等操作系统下只使用系统自带的驱动程序和HID Input Service 服务，多媒体键即可生效的键盘，如微软精巧500/600、DELL 8135等，这些键盘使用的驱动程序名称为HID Keyboard Device（USB接口键盘）或“标准 101/102键盘或microsoft 自然 PS/2 键盘”（PS/2接口键盘）。  
另：按照微软提供的USB/PS2键盘扫描码对应表，USB键盘比PS/2键盘要多出一些键位定义，如：复制、粘贴、撤消等。因条件所限没有进一步研究。

 **定制多媒体键**

多媒体键虽然有18个之多，但并不一样都是用户想要的功能。比如说我可能更需要一键打开记事本而不是计算器；按下“我的电脑”键我希望能运行的是Total Commander。微软考虑到了用户这个需求，提供了两种解决方案：一是安装微软提供的IntelliType Pro驱动工具，使用常驻内存的程序来控制各个键的定义。二是在注册表中提供了部分键的自定义功能，允许定制上表中8至18号键位功能。微软也提供了个工具TweakUI可以修改这些键的定义保存至注册表，但修改的内容有限。使用第三方驱动还要有常驻内存的程序，我个人不是很感冒。在这里我们详细了解一下注册表修改这种方法。

例一：修改Calculator计算器键，把它的定义改为打开记事本。只须将如下内容保存为notepad.reg，双击导入注册表即可：

代码:
    
    
    Windows Registry Editor Version 5.00
    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AppKey\18]
    "ShellExecute"="notepad.exe"

如果要改为打开默认的邮件客户端，可以将上面的"ShellExecute"="calc.exe"一行改为：  


代码:
    
    
    "Association"="mailto"

或者：  


代码:
    
    
    "RegisteredApp"="mail"

例二：修改My Computer我的电脑键，将其改为运行Total Commander。需要导入如下注册表项目：

代码:
    
    
    Windows Registry Editor Version 5.00
    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AppKey\17]
    "ShellExecute"=" D:\\Program Files\\TotalCmd\\TOTALCMD.EXE"

（Total Commander实际路径需要根据实际情况修改）

在以上两例中：

  


代码:
    
    
    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AppKey]

和  


代码:
    
    
    [HKEY_CURRENT_USER \SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AppKey]

这两个主键下提供了对多媒体键定义功能，两个主键的区别是作用范围是全体用户还是当前用户。也就是说如果多人共用一台计算机，不同的账户下同一个键可以设定不同的功能。  
每个多媒体键都有一个数字编号的分支，具体编号对应情况见上表。  
键名有ShellExecute、Assocication和RegisteredApp三种类型可选：  
ShellExecute 是执行一个外部程序，在键值中指定要执行的程序名称即可。  
Assocication是指定关联，可以将键值设定为一个扩展名如“.rar”，将调用Winrar程序；也可以指定一个协议，http即调用默认的http浏览器，mailto则是调用默认的邮件客户端。  
[size=2]RegisteredApp是指定已注册的默认程序，键值可以设定为mail、news、Calendar、Contacts、Media[font=宋体]等，分别代表默认的邮件客户端、新闻组程序、日历、联系人、媒体播放器等。具体在注册表中的位置如下：  


代码:
    
    
    [HKEY_LOCAL_MACHINE\SOFTWARE\Clients]

 **定制键盘任意键**

有人可能会问：我的键盘上只有表中1~7号多媒体键，或者根本就没有任何多多媒体键，有没有办法将某些键定义成打开指定程序或者其它多媒体键呢？回答是肯定的，那就是利用微软提供的扫描码映射（Scan Code Mapper）功能，详细资料参见：

  
[ _http://www.microsoft.com/whdc/archive/w2kscan-map.mspx_](http://www.microsoft.com/whdc/archive/w2kscan-map.mspx) 。  
实际上这是个很古老的技术了，KeyTweak、RemapKey、KeybMap等软件都是利用了这项技术通过修改注册表来完成键盘值转义功能。下面我们手动操作，将Scroll Lock 键改为打开记事本功能：  
1、 先将Scroll Lock 键映射为Calculator键，即打开计算器。导入如下注册表项目：  


代码:
    
    
    Windows Registry Editor Version 5.00
    [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout]
    "Scancode Map"=hex:00,00,00,00,00,00,00,00,02,00,00,00,21,e0,46,00,00,00,00,00

2、 重启计算机，此时按下Scroll Lock 键，可以打开计算器。  
3、 按照前面介绍的方法，再将Calculator键的定义修改为打开记事本即可。  
修改1~7号无法定制功能的多媒体键方法也是一样的。  
注意：Power、Sleep、Wake Up 这三个电源键有些特殊，它们也可以映射到其它键，但必须先从控制面板－电源选项中将Power和Sleep的功能设定为“不采取任何操作”。另外在USB键盘上，这三个键映射无效，若是通过转换口连接到PS/2接口上，则是可以使用的。  
为了减化操作，我升级了KeybMap这个工具，增加了对多媒体键的自定义功能，可以很方便地实现以上功能。有兴趣的朋友可以下载使用。下载地址：  
[ _http://www.mympc.org/down/1/2005-11-26_0111998067.html_](http://www.mympc.org/down/1/2005-11-26_0111998067.html)

 **改造普通键盘硬件，增加多媒体键**

这时又有朋友问了：我用的是标准104键键盘，不想修改现有的键定义，能不能增加几个多媒体键？回答仍然是可行的！不过需要你有一定的DIY能力，能够熟练的使用电烙铁等工具。

  
前面我们提到过现在通用的键盘都是使用了IBM定义的矩阵，一共有8行×16列＝128个键位，空闲了24个键位。而电源键和多媒体键都是利用了这些空闲键位。由此想来现在常用的键盘控制器芯片一定可以完整处理这128个键，厂家没有必要为普通104键键盘和多媒体键盘开发不同的键盘控制器芯片，更没有必要在普通104键键盘上屏蔽那多余的24个键位处理能力。基于以上理由，我们推测市场上最常见的104键键盘能够支持多媒体键，只是没有做出相应的键位而已。  
下面就来验证一下我们的推测：拆开一块普通的104键键盘，找到线路板，可以看到上面有与键盘薄膜电路相连的金手指触点，这些触点通过键盘薄膜电路两两组合，从而得到了不同的按键。因为这一部分电路没有统一的标准，我只能用穷举法来一个个测试：找一根导线按顺序短接不同的触点。经过一段时间的测试，我果然找到了静音、音量增大、音量减小、计算器、我的电脑等热键；不幸的是在测试的过程中我也找到了电源键，于是系统就自动地关机了……不管怎么说，试验是成功了。  
我先后在IBM、联想、浪潮、清华同方等四块不同品牌计算机的键盘上做过以上试验，不管是PS/2接口还是USB接口的键盘，都是成功的。  
下面要做的就是去电子市场买一些轻触开关，想办法固定在键盘的空闲的地方，找到所需的键位组合，用导线焊好就可以了。当然，要想做得美观，需要你有较强的动手能力。  
也许费了这么大功夫，改造一块不到一百元的键盘纯属浪费精力，但是对我们DIY爱好者来说，结果并不是目的，探索的过程中才是我们最大的乐趣。我们口号是：生命在于折腾……  


