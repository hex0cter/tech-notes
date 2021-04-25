
date: None  
author(s): None  

# [修改 Ubuntu 9.04 英文环境下的默认中文字体 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/default_chinese_font_for_ubuntu)

_**中文**_ _ **环境**_会导致很多 _ **软件**_出现半英半中的拉剃头现象，还是用 _ **英文**_得了，也算是学习。

1\. 安装中文 _ **语言**_支持，会自动安装文泉驿中文 _ **字体**_。

2\. 用 gedit 打开 /etc/fonts/conf.avail/69-language-selector-zh-cn.conf 调整字体顺序，另存为 ~/.fonts.conf。3. 重启即可。

![uploads/200909/07_181604_1.png](http://www.rainsts.net/uploads/200909/07_181604_1.png)

按 **Bitstream Vera *** , **DejaVu *** , **WenQuanYi Zen Hei** , **WenQuanYi Bitmap Song** , *** CN** 顺序排即可。

yuhen@yuhen-desktop:~$ **cat .fonts.conf**

  


<fontconfig> <match target="pattern"> <test qual="any" name="family"> <string>serif</string> </test> <edit name="family" mode="prepend" binding="strong"> <string>Bitstream Vera Serif</string> <string>DejaVu Serif</string> <string>WenQuanYi Bitmap Song</string> <string>AR PL UMing CN</string> <string>AR PL ShanHeiSun Uni</string> <string>AR PL UKai CN</string> <string>AR PL ZenKai Uni</string> </edit> </match> <match target="pattern"> <test qual="any" name="family"> <string>sans-serif</string> </test> <edit name="family" mode="prepend" binding="strong"> <string>Bitstream Vera Sans</string> <string>DejaVu Sans</string> <string>WenQuanYi Zen Hei</string> <string>WenQuanYi Bitmap Song</string> <string>AR PL UMing CN</string> <string>AR PL ShanHeiSun Uni</string> <string>AR PL UKai CN</string> <string>AR PL ZenKai Uni</string> </edit> </match> <match target="pattern"> <test qual="any" name="family"> <string>monospace</string> </test> <edit name="family" mode="prepend" binding="strong"> <string>Bitstream Vera Sans Mono</string> <string>DejaVu Sans Mono</string> <string>WenQuanYi Zen Hei</string> <string>WenQuanYi Bitmap Song</string> <string>AR PL UMing CN</string> <string>AR PL ShanHeiSun Uni</string> <string>AR PL UKai CN</string> <string>AR PL ZenKai Uni</string> </edit> </match>

</fontconfig>

 **TAG:** [ubuntu](http://www.m-12.cn/?action-tag-tagname-ubuntu) [Ubuntu](http://www.m-12.cn/?action-tag-tagname-Ubuntu) [环境](http://www.m-12.cn/?action-tag-tagname-%BB%B7%BE%B3) [英文](http://www.m-12.cn/?action-tag-tagname-%D3%A2%CE%C4) [中文](http://www.m-12.cn/?action-tag-tagname-%D6%D0%CE%C4) [字体](http://www.m-12.cn/?action-tag-tagname-%D7%D6%CC%E5)

