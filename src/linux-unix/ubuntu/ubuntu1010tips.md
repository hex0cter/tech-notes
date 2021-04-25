
date: None  
author(s): None  

# [ubuntu 10.10诸多问题解决方法 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/ubuntu/ubuntu1010tips)

__**一、QQ上线一段时间后自动退出**__ 。

1\. 打开qq配置文件：在终端输入命令代码：sudo gedit /usr/bin/qq

2\. 在打开的qq配置文件中，在#!bin/sh下面一行，cd /usr/share/tencent/qq/前面一行的位置插入代码：

export GDK_NATIVE_WINDOWS=true

3\. 最终修改后的QQ脚本配置文件如下，保存关闭即可。

#!/bin/shexport GDK_NATIVE_WINDOWS=truecd /usr/share/tencent/qq/

./qq

4\. 重启QQ，qq不再自动退出和关闭了。

 _ _ **二、rhythmbox歌曲信息乱码**__

首先，需要有软件包mid3iconv。如果你的系统中没有安装它，可以通过如下代码自动安装：sudo apt-get install python-mutagen 然后转到你的MP3目录，执行以全命令进行转换：mid3iconv -e GBK *.mp3 如果需要包含子目录，可以将后缀改成如下格式：打命令的时候文件名字给 "*/*.mp3" 就行了。比如mid3iconv -e GBK */*.mp3 

最后，重新导入一次rhythmbox就OK了。解决Rhythmbox乱码

三、窗口最小化、最大化和关闭按钮显示在右边

  * 1\. Alt + F2 ，运行 gconf-editor
  * 2\. 在左侧目录树中，找到 /apps/metacity/general/
  * 3\. 在右侧找到键： button_layout ， 修改值为 menu:minimize,maximize,close



四、ubuntu自带的vi不支持backspace键和方向键，并且不支持中文输入

sudo apt-get install vim-gnome

五、解压rar文件

sudo apt-get install rar

六、显示VI行号

在VI的命令模式下输入“:set nu” 或者修改vi配置文件“vi ~/.vimrc”，在其中添加“set nu” 在VI的命令模式下输入“:set nu”，就有行号了。 但是想将这个设置写进VI的配置文件，就 # vi ~/.vimrc 在这个文件中，添加 set nu 

就行了

七、文件乱码打不开

有时候windows拷贝到ubuntu下面的office文件会显示为乱码或者打不开，使用下面的命令转换字符编码即可

convmv -f GBK -t UTF-8 --notest *.doc八、umount设备出现“device is busy“fuser -m -v /media/c:九、kdm gdm之间的切换sudo dpkg-reconfigure gdm

十、wireshark源码安装

安装完毕后，启动提示有几个.so文件找不到，解决办法如下：

ldd `which wireshark`|grep not 输出如下： libwiretap.so.0 => not found libwireshark.so.0 => not found 这说明checkinstall工具对wireshark支持不完善，需要如下手工补救： 进入到wireshark编译过的源代码目录： cp wiretap/.libs/libwiretap.so.0 /usr/lib/

cp epan/.libs/libwireshark.so.0 /usr/lib/

未完待续。。。。。。

本文出自 “[技术成就梦想](http://hover.blog.51cto.com/)” 博客，请务必保留此出处<http://hover.blog.51cto.com/258348/416930>

