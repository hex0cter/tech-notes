# [Ubuntu 10.04/11.04/Linux Mint 中文字体问题](http://www.cnblogs.com/zengyongjoy/archive/2010/05/02/1725841.html)

前面的文章提到Ubuntu 10.04的默认显示中文字体已经很好看，感觉和window 7的微软雅黑效果差不多。

但是碰到一个很怪的问题，因为我默认安装的是English，在安装了中文语言包之后，默认的字体就变得太难看了，特别是在chrome里面，中文显示特别细，而且发虚。

查了网上，是默认字体的问题。方法：创建符号连接 `69-language-selector-zh-cn.conf`

```
cd /etc/fonts/conf.d/
sudo ln -s ../conf.avail/69-language-selector-zh-cn.conf .
```

然后刷新字体缓存

```
sudo fc-cache -vf
```

然后打开chrome就可以看到原来的效果。
