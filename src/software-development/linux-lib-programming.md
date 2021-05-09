# [Linux静态、共享和动态库之编程](http://www.diybl.com/course/6_system/linux/Linuxjs/20071226/94196.html)


一.库的分类
有两种说法, 如果熟悉WIN平台下的DLL, 相信不难理解:

库可以有三种使用的形式:静态、共享和动态.静态库的代码在编译时就已连接到开发人员开发的应用程序中, 而共享库只是在程序开始运行时才载入, 在编译时, 只是简单地指定需要使用的库函数.动态库则是共享库的另一种变化形式.动态库也是在程序运行时载入, 但与共享库不同的是, 使用的库函数不是在程序运行开始, 而是在程序中的语句需要使用该函数时才载入.动态库可以在程序运行期间释放动态库所占用的内存, 腾出空间供其它程序使用.由于共享库和动态库并没有在程序中包括库函数的内容, 只是包含了对库函数的引用, 因此代码的规模比较小.

Linux下的库文件分为共享库和静态库两大类, 它们两者的差别仅在程序执行时所需的代码是在运行时动态加载的, 还是在编译时静态加载的.区分库类型最好的方法是看它们的文件后缀, 通常共享库以.so(Shared Object的缩写)结尾, 静态链接库通常以.a结尾(Archive的缩写).在终端缺省情况下, 共享库通常为绿色, 而静态库为黑色.

已经开发的大多数库都采取共享库的方式.ELF格式的可执行文件使得共享库能够比较容易地实现, 当然使用旧的a.out模式也可以实现库的共享.Linux系统中目前可执行文件的标准格式为ELF格式.

* .a的是为了支持较老的a.out格式的可执行文件的

* .so的是支持elf格式的可执行文件的库.

* .a是静态库文件, 可以用ar 命令生成.

* .so是动态库文件, 编译时加上指定的选项即可生成, 具体选项看相应的系统文档了.

二.库的命名规则
    GNU库的使用必须遵守Library GNU Public License(LGPL许可协议).该协议与GNU许可协议略有不同, 开发人员可以免费使用GNU库进行软件开发, 但必须保证向用户提供所用的库函数的源代码.

　　系统中可用的库都存放在/usr/lib和/lib目录中.库文件名由前缀lib和库名以及后缀组成.根据库的类型不同, 后缀名也不一样.共享库的后缀名由.so和版本号组成, 静态库的后缀名为.a.采用旧的a.out格式的共享库的后缀名为.sa.

　　libname.so.major.minor
　　libname.a

　　这里的name可以是任何字符串, 用来唯一标识某个库.该字符串可以是一个单字、几个字符、甚至一个字母.数学共享库的库名为libm.so.5, 这里的标识字符为m, 版本号为5.libm.a则是静态数学库.X-Windows库名为libX11.so.6, 这里使用X11作为库的标识, 版本号为6.

三.库操作命令

   Linux库操作可以使用命令完成, 目前常用的命令是ldd和ldconfig.

   1.ldd
 ldd是Library Dependency Display缩写, 它的作用是显示一个可执行程序必须使用的共享库.
 ```
 $ ldd /usr/bin/mesg
 libc.so.6 => /lib/tls/i686/cmov/libc.so.6 (0xb7eaf000)
 /lib/ld-linux.so.2 => /lib/ld-linux.so.2 (0xb7feb000)
 ```
   2.ldconfig
 库安装到系统以后, 为了让动态链接库为系统所认识及共享, 就需要运行ldconfig.ldconfig命令的用途, 主要是在默认搜寻目录(/lib和/usr/lib)以及动态库配置文件/etc/ld.so.conf内所列的目录下, 搜索出可共享的动态链接库(格式如lib*.so*), 进而创建出动态装入程序(ld.so)所需的连接和缓存文件.缓存文件默认为/etc/ld.so.cache, 此文件保存已排好序的动态链接库名字列表, ldconfig通常在系统启动时运行, 而当用户安装了一个新的动态链接库时,就需要手工运行这个命令.

（1）命令格式
```
 ldconfig [选项] [libs]
```
（2）主要选项
 -v或--verbose ldconfig将显示正在扫描的目录、搜索到的动态链接库, 以及它所创建的连接的名字.

 -f CONF 指定动态链接库的配置文件为CONF, 系统默认为/etc/ld.so.conf.

 -C CACHE 指定生成的缓存文件为CACHE, 系统默认的是/etc/ld.so.cache,文件存放已排好序的可共享的动态链接库的列表.

 -p或--print-cache 让ldconfig打印出当前缓存文件所保存的所有共享库的名字.

 -r ROOT 改变应用程序的根目录为ROOT.

 －n ldconfig仅扫描命令行指定的目录, 不扫描默认目录(/lib、/usr/lib),也不扫描配置文件/etc/ld.so.conf所列的目录.

 运行没有选项的ldconfig命令时, 用于更新高速缓冲文件.这个命令主要用于高速缓冲DNS服务器(Caching DNS Server).高速缓冲DNS服务器的原理是提供查询的历史记录, 并且利用这些记录来提高查询的效率.

 当某个查询是第一次被发送到高速缓冲DNS服务器时, 高速缓冲DNS服务器就将此查询的整个过程记录下来, 在一定的时期内用它来回答所有相同的查询, 从而减少整个DNS系统的负担并且提高查询速度.

四.库的升级

 Linux系统软件更新很快, 新的核心几乎每几个星期就公布一次, 其它软件的更新也是非常频繁.多数情况下, 盲目跟随潮流的升级并不必要, 如果确实需要新版本的特性时再升级.换句话说, 不要为了升级而升级.Linux系统中多数软件都是用共享库来编译的, 其中包含了在不同程序之间共享的公用子例程.

在运行某个程序时, 如果看到如下信息:“Incompatible library version．”则表明需要将该库升级到程序所需要的版本.库是向下兼容的, 也就是说, 用老版本库编译的程序可以在新安装的版本库上运行, 反之则不行.

Linux库函数的升级是一项重要的工作, 往往与其它软件包的升级有一定关联作用, 所以操作前一定要备份文件.下面看一下如何把Glibc 2.2.4.13升级至2.3.2版本, 其过程如下:

  1.下载.gz压缩文件并解压

在GUN C网站下载的四个.gz压缩文件, 解压至一临时目录中:
```
cd /usr/caolinux
tar xzvf glibc-2.3.2.tar.gz
cd glibc-2.3.2
tar xzvf ../glibc-linuxthreads-2.3.2.tar.gz
tar xzvf ../glibc-crypt-2.3.2.tar.gz
tar xzvf ../glibc-localedata-2.3.2.tar.gz
```
  2.建立库函数的安装目录
```
mkdir /usr/higlibc
cd /usr/higlibc
```
   3.建立编译目录
```
mkdir cao
cd cao
./configure --enable-add-ons=linuxthreads,crypt,localedata -prefix=/usr/higlibc
```
  4.编译与安装
```
make
make check
make install
```
  5.改变数据库的链接
ln -s /usr/higlibc/lib/ld-linux.so.2 /lib/ld-linux.so.2

然后, 修改/etc/ld.so.conf, 加入一行/usr/higlibc/lib, 执行下面代码:
ldconfig -v

更新/etc/ld.so.cache的内容, 列出每个库的版本号, 扫描目录和所要创建及更新的链接.

 6.更改GCC设置
```
cd /usr/lib/gcc-lib
cp -r i386-redhat-linux higlibc
```
 7.更新符号链接
```
cd /usr/higlibc/include
ln -s /usr/src/linux/include/linux
ln -s /usr/src/linux/include/asm
ln -s /usr/X11R6/include/X11
```

8.测试并完成

五.高级共享库特性
 1. soname

共享库的一个非常重要的, 也是非常难的概念是 soname——简写共享目标名（short for shared object name）.这是一个为共享库（.so）文件而内嵌在控制数据中的名字.如前面提到的, 每一个程序都有一个需要使用的库的清单.这个清单的内容是一系列库的 soname, 如同 ldd 显示的那样, 共享库装载器必须找到这个清单.

soname 的关键功能是它提供了兼容性的标准.当要升级系统中的一个库时, 并且新库的 soname 和老的库的 soname 一样, 用旧库连接生成的程序, 使用新的库依然能正常运行.这个特性使得在 Linux 下, 升级使用共享库的程序和定位错误变得十分容易.

在 Linux 中, 应用程序通过使用 soname, 来指定所希望库的版本.库作者也可以通过保留或者改变 soname 来声明, 哪些版本是相互兼容的, 这使得程序员摆脱了共享库版本冲突问题的困扰.

查看/usr/local/lib 目录, 分析 MiniGUI 的共享库文件之间的关系

2. 共享库装载器

当程序被调用的时候, Linux 共享库装载器（也被称为动态连接器）也自动被调用.它的作用是保证程序所需要的所有适当版本的库都被调入内存.共享库装载器名字是 ld.so 或者是 ld-linux.so, 这取决于 Linux libc 的版本, 它必须使用一点外部交互, 才能完成自己的工作.然而它接受在环境变量和配置文件中的配置信息.

文件 /etc/ld.so.conf 定义了标准系统库的路径.共享库装载器把它作为搜索路径.为了改变这个设置,
