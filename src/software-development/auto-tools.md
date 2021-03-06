# [autotools举例](http://www.xxlinux.com/linux/article/development/soft/20071118/12163.html)


最近开始学习linux c开发，对autotools比较感兴趣，所以找了一些国外的文档看了看，然后自己做了小例子，在这里跟大家分享。

1、准备:

需要工具autoscan aclocal autoheader automake autoconf make 等工具.

2、测试程序编写：

建立目录：mkdir include src 编写程序：`include/str.h`:

```
#include <stdio.h>
int str(char *string);
```
编写程序：`src/str.c`

```C
#include "str.h"
//print string
int str(char *string){
        printf("\n----PRINT STRING----\n\"%s\"\n",string);
        return 0;
}

//interface of this program
int main(int argc , char **argv){
        char str_read[1024];
        printf("Please INPUT something end by [ENTER]\n");
        scanf("%s",str_read);
        return str(str_read );
}
```

3、生成configure.ac

configure.ac是automake的输入文件，所以必须先生成该文件。 执行命令：

```
[root@localhost str]# ls
include  src
[root@localhost str]# autoscan
autom4te: configure.ac: no such file or directory
autoscan: /usr/bin/autom4te failed with exit status: 1
[root@localhost str]# ls
autoscan.log  configure.scan  include  src
[root@localhost str]# cp configure.scan configure.ac
```

修改 configure.ac

```
#  -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
AC_INIT(FULL-PACKAGE-NAME, VERSION, BUG-REPORT-ADDRESS)
AC_CONFIG_SRCDIR([include/str.h])
AC_CONFIG_HEADER([config.h])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.
AC_OUTPUT
```

修改
```
AC_INIT(FULL-PACKAGE-NAME, VERSION, BUG-REPORT-ADDRESS)
```
为
```
AC_INIT(str,0.0.1, [bug@sounos.org])
```
FULL-PACKAGE-NAME 为程序名称，VERSION为当前版本， BUG-REPORT-ADDRESS为bug汇报地址

添加AM_INIT_AUTOMAKE


添加AC_CONFIG_FILES([Makefile])

```C
# -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)
#AC_INIT(FULL-PACKAGE-NAME, VERSION, BUG-REPORT-ADDRESS)
AC_INIT(str, 0.0.1, [bug@sounos.org])
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR([include/str.h])
AC_CONFIG_HEADER([config.h])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.

# Checks for header files.

# Checks for typedefs, structures, and compiler characteristics.

# Checks for library functions.
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
```

4、执行aclocal

```
[root@localhost str]# aclocal
/usr/share/aclocal/libfame.m4:6: warning: underquoted definition of AM_PATH_LIBFAME
  run info '(automake)Extending aclocal'
  or see http://sources.redhat.com/automake/automake.html#Extending-aclocal
```

or see http://sources.redhat.com/automake/automake.html#Extending-aclocal

5、制作Makefile.am

```
[root@localhost str]# cat Makefile.am
#Makefile.am
bin_PROGRAMS    = str
str_SOURCES     = include/str.h src/str.c
str_CPPFLAGS    = -I include/
```

6、autoheader
```
[root@localhost str]# autoheader
```

7、automake必须文件：
```
    *  install-sh
    * missing
    * INSTALL
    * NEWS
    * README
    * AUTHORS
    * ChangeLog
    * COPYING
    * depcomp
```

其中

```
    * install-sh
    * missing
    * INSTALL
    * COPYING
    * depcomp
```

可以通过automake -a选项自动生成，所以这里只需要建立如下文件

[root@localhost str]# touch NEWS README AUTHORS ChangeLog

8、执行automake

```bash
[root@localhost str]# automake -a
configure.ac: installing `./install-sh'
configure.ac: installing `./missing'
Makefile.am: installing `./INSTALL'
Makefile.am: installing `./COPYING'
Makefile.am: installing `./compile'
Makefile.am: installing `./depcomp'
```

9、autoconf

```
[root@localhost str]# autoconf
[root@localhost str]# ls
aclocal.m4      autoscan.log  config.h.in   configure.scan  include     Makefile.am  NEWS
AUTHORS         ChangeLog     configure     COPYING         INSTALL     Makefile.in  README
autom4te.cache  compile       configure.ac  depcomp         install-sh  missing      src
```

10、执行测试： 执行./configure

```
[root@localhost str]# ./configure --prefix=/u
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ANSI C... none needed
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
configure: creating ./config.status
config.status: creating Makefile
config.status: creating config.h
config.status: config.h is unchanged
config.status: executing depfiles commands
```

执行 make

```
[root@localhost str]# make
make  all-am
make[1]: Entering directory `/data/devel/c/str'
if gcc -DHAVE_CONFIG_H -I. -I. -I.  -I include/   -g -O2 -MT str-str.o -MD -MP -MF ".deps/str-str.Tpo" -c -o str-str.o `test -f 'src/str.c' || echo './'`src/str.c; \
then mv -f ".deps/str-str.Tpo" ".deps/str-str.Po"; else rm -f ".deps/str-str.Tpo"; exit 1; fi
gcc  -g -O2   -o str  str-str.o
make[1]: Leaving directory `/data/devel/c/str'
```

执行 make install

```
[root@localhost str]# make install
make[1]: Entering directory `/data/devel/c/str'
test -z "/u/bin" || mkdir -p -- "/u/bin"
  /usr/bin/install -c 'str' '/u/bin/str'
make[1]: Nothing to be done for `install-data-am'.
make[1]: Leaving directory `/data/devel/c/str'
```

11、测试程序：

```
[root@localhost str]# /u/bin/str
Please INPUT something end by [ENTER]
abcksdhfklsdklfdjlkfd

----PRINT STRING----
"abcksdhfklsdklfdjlkfd"
```

结束语：这只是一个小例子，如果要把这个用得很好需要不断的磨练。。。。呵呵，见笑了。
