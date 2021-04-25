
date: None  
author(s): None  

# [Linux/unix 下常用压缩格式的压缩与解压方法 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/ziponlinux)

.tar

解包：tar xvf FileName.tar打包：tar cvf FileName.tar DirName（注：tar是打包，不是压缩！）---------------------------------------------.gz解压1：gunzip FileName.gz解压2：gzip -d FileName.gz压缩：gzip FileName .tar.gz解压：tar zxvf FileName.tar.gz压缩：tar zcvf FileName.tar.gz DirName--------------------------------------------- .bz2解压1：bzip2 -d FileName.bz2解压2：bunzip2 FileName.bz2压缩： bzip2 -z FileName.tar.bz2解压：tar jxvf FileName.tar.bz2 压缩：tar jcvf FileName.tar.bz2 DirName---------------------------------------------.bz解压1：bzip2 -d FileName.bz 解压2：bunzip2 FileName.bz压缩：未知.tar.bz解压：tar jxvf FileName.tar.bz压缩：未知---------------------------------------------.Z解压：uncompress FileName.Z压缩：compress FileName.tar.Z解压：tar Zxvf FileName.tar.Z压缩：tar Zcvf FileName.tar.Z DirName---------------------------------------------.tgz解压：tar zxvf FileName.tgz压缩：未知.tar.tgz解压：tar zxvf FileName.tar.tgz压缩：tar zcvf FileName.tar.tgz FileName---------------------------------------------.zip解压：unzip FileName.zip压缩：zip FileName.zip DirName---------------------------------------------.rar解压：rar a FileName.rar

压缩：rar e FileName.rar

  
rar请到：<http://www.rarsoft.com/download.htm> 下载！解压后请将rar_static拷贝到/usr/bin目录（其他由$PATH环境变量指定的目录也可以）：[root@www2 tmp]# cp rar_static /usr/bin/rar---------------------------------------------.lha解压：lha -e FileName.lha 

压缩：lha -a FileName.lha FileName

lha请到：<http://www.infor.kanazawa-it.ac.jp/~ishii/lhaunix/>下载！解压后请将lha拷贝到/usr/bin目录（其他由$PATH环境变量指定的目录也可以）：[root@www2 tmp]# cp lha /usr/bin/---------------------------------------------.tar .tgz .tar.gz .tar.Z .tar.bz .tar.bz2 .zip .cpio .rpm .deb .slp .arj .rar .ace .lha .lzh .lzx .lzs .arc .sda .sfx .lnx .zoo .cab .kar .cpt .pit .sit .sea解压：sEx x FileName.* 

压缩：sEx a FileName.* FileName

sEx只是调用相关程序，本身并无压缩、解压功能，请注意！  
sEx请到：<http://sourceforge.net/projects/sex>下载！解压后请将sEx拷贝到/usr/bin目录（其他由$PATH环境变量指定的目录也可以）：[root@www2 tmp]# cp sEx /usr/bin/  
  
---

