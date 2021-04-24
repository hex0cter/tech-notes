
# [如何更换安卓手机的声音文件](http://www.anzhuoba.com/forum.php?mod=viewthread&action=printable&tid=26037)

**安卓系统自带有很多种声音文件，比如 闹钟、短信通知、铃声和系统界面声音等等，如何替换它们呢？**

 **1\. 系统自带声音文件存放的位置和内容。**


总目录：/system/media/audio
闹钟：/system/media/audio/alarms
短信通知：/system/media/audio/notificati**
铃声：/system/media/audio/ringtones
系统界面声音：/system/media/audio/ui

 **2\. 在sd卡中自定义各种声音。**


在sd卡的根目录下建立文件夹media
在media目录下建立文件夹 alarms 里面放闹钟所需的音乐文件
在media目录下建立文件夹 notificati** 里面放短信通知所需的音乐文件
在media目录下建立文件夹 ringtones 里面放电话铃声所需的音乐文件
本方法的优点是sd卡容量大 音乐文件大小不受**，缺点，读取sd卡 慢 不方便 还费电。

 **3\. 替换系统内置的声音**


首先你的机子必须root过，并且文件管理器要取得最高权限，然后设置/system 为可写入。并且注意你要替换的音乐文件的大小。
闹钟请放到这里，原有的可以删除：/system/media/audio/alarms
短信通知请放到这里，原有的可以删除，：/system/media/audio/notificati**
铃声请放到这里，原有的可以删除：/system/media/audio/ringtones
系统界面声音必须更名为系统的名字后替换本文件夹中的相应文件：/system/media/audio/ui
本方法的优点是读取快速，省电，方便而且恢复出厂设置都不会丢失，缺点是音乐的大小数量 局限性很大。设置好了重启下就OK啦。
最后，在 设置 -> 声音 -> 手机铃声 里选择自己的新铃声即可。
