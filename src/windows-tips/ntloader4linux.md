
date: None  
author(s): None  

# [用NTLoader来引导linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/windows-tips/ntloader4linux)

我本人并不喜欢将grub安装到mbr,毕竟windows才是我主要用的系统,重装可能性比较大.grub安装到mbr会被重写,带来一些不必要要的麻烦.但写下重装到mbr的方法,以免误操作.

(一). 恢复被windows破坏的grub. 如果你用grub来引导linux和windows,当windows出毛病重新安装后,会破坏MBR中的grub,这时需要恢复grub. 1.把linux安装光盘的第一张放到光驱，然后重新启动机器，在BOIS中把系统用光驱来引导。 2.等安装界面出来后，按［F4］键，也就是linux rescue模式。 3.一系列键盘以及几项简单的配制，过后就［继续］了。。。这个过程，我不说了，比较简单。 4.然后会出现这样的提示符: sh# 5.我们就可以操作GRUB了.输入grub: sh#grub 会出现这样的提示符: grub> 我们就可以在这样的字符后面，输入: grub>root (hdX,Y) 

grub>setup (hd0) 

如果成功会有一个successful...... 这里的X，如果是一个盘，就是0，如果你所安装的linux的根分区在第二个硬盘上，那X就是1了；Y，就是装有linux系统所在的根分区。 setup (hd0)就是把GRUB写到硬盘的MBR上。 (二).用NTLoader来引导linux. 如果你在安装linux时没有选择安装grub,不必着急,现在我们来看看如何在安装linux后安装grub.并用windows的NTLoader来引导linux. 1. 安装grub 我用的grub是Redhat8.0带的grub安装包: grub-0.92-7.rpm 安装: rpm -ivh grub-0.92-7.rpm 其他安装方式也一样,只要你安装上grub就行了.RH8缺省用的grub, 1,2步骤可以省了. 2. 建立grub的环境 cp /usr/share/grub/i386-pc/* /boot/grub 3. 生成grub的配置文件/boot/grub/menu.lst 注意了, 这里我的linux在/dev/hda4,所以menu.lst那些分区位置为(hd0,3), 你的可能不一样了,不能完全照着"画瓢"噢! 下面第3步install的中的分区位置也应该和你的系统一致. 3. 安装grub至Linux分区boot 将grub的stage1安装到/dev/hda4的boot扇区(hd0,3). 过程如下: /sbin/grub (运行grub) 

grub> **install (hd0,3)/boot/grub/stage1 d (hd0,3) (hd0,3)/boot/grub/stage2 p (hd0,3)/boot/grub/menu.lst **

(注意,上面"grub>"为grub的提示符,其后内容写在一行上.) 4. 取得grub的boot信息 过程如下: 

dd if=/dev/hda4 of=/grub.lnx bs=512 count=1 

这样得到grub的引导信息,只要用NT Loader来加载它就行了. 5. 将上面得到的grub.lnx弄到Windows的C盘根目录下 可以先把grub.lnx弄得软盘上,然后启动windows,拷贝到C:\; 情况允许也可以直接在Linux下拷贝到C:了. 我的C盘(即设备/dev/hda1)为FAT32, 可以直接从Linux下弄过去了. 如下: mount -t vfat /dev/hda1 /mnt/c cp /grub.lnx /mnt/c umount /mnt/c 6. 修改NT Loader的boot.ini 在其中加入一行: C:\grub.lnx="Redhat Linux - GRUB" 加入后boot.ini的内容如下: [boot loader] timeout=15 default=C:\boot.lnx [operating systems] multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect 

[VGA mode]" /

basevideo /sos C:\grub.lnx="Redhat Linux - GRUB" OK. 可以用NT Loader加载Linux了, 其实上面过程基本上和用NT Loader加载LILO一样.其基本思想就是用NT Loader来加载LILO或grub的引导区(grub.lnx), 其中的关键就是LILO或grub的引导区的获取

[http://rainkt.spaces.live.com/blog/cns!D134C68494563C62!174.entry](http://rainkt.spaces.live.com/blog/cns%21D134C68494563C62%21174.entry)

  


