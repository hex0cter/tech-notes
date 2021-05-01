# [Ubuntu 10.04英文环境中设置默认中文字体(http://forum.ubuntu.org.cn/viewtopic.php?f=8&t=204439&start=0)


1. 下载雅黑字体，见附件。 http://rapidshare.com/files/34563809/YaHei.Consolas.1.11b.zip

解压后，复制到 /usr/share/fonts/truetype 目录，并重命名为YaHei_Consolas.ttf:

sudo cp YaHei.Consolas.1.11b.ttf /usr/share/fonts/truetype/YaHei_Consolas.ttf

2. 生成字体目录列表等命令：
```
sudo chmod 644 /usr/share/fonts/truetype/*
cd /usr/share/fonts/truetype/
sudo mkfontscale
sudo mkfontdir
sudo fc-cache /usr/share/fonts/truetype/
```

3. 更改配置文件，见附件。

4. 重新启动系统。
