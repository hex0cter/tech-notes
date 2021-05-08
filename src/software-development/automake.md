# [AutoMake使用小结](http://blog.csdn.net/oeichenwei/archive/2005/12/08/547235.aspx)


以一个Hello 程序描述为一个project生成Makefile的过程。 这个例子其实在 Info automake 里能看到。大家把它翻成中文的，不错。 但实际上按照这个例子来做的话，步骤都对，就是太简单，一些常用的设置需要写进去，但是没有提到，还是要自己info , google ,try . 下面是我对Automake一个小总结。

1 步骤总述

(1) autoscan 生成configure.scan .

(2) 在configure.scan基础上手动编辑，主要要添加的 ： AM_INIT_AUTOMAKE(myprojectname , version) AC_OUTPUT( 最后要生成的Makefile , 包括 子目录中的，中间用空格隔开) , 例如 AC_OUTPUT(Makefile subdir/Makefile subdir1/Makefile) AC_PROG_RANLIB (意义见第四条末尾)

(3) aclocal autoconf 生成configure脚本。

(4) 这步我基本靠手，呵呵，有没有脚本来完成这个的？就是在每个最后需要生成Makefile的目录中，写一个Makefile.am . 最上层的要写明 AUTOMAKE_OPTIONS = foreign 如果这个目录没有要编译的文件 ，只包含了子目录，则只写个 SUBDIRS = dir1 就ok了。 例如我的工程，最上层只是包含了源码目录，于是就写了

AUTOMAKE_OPTIONS=foreign SUBDIRS=src 如果有文件要编译，则要指明target 先。比如我的src目录底下既有文件，又有目录，而src的这层目录中的文件最后是要编译成一个 可执行文件，则src目录下的Makefile.am这么写。 bin_PROGRAMS= myprogram SUBDIRS= sub1myprogram_SOURCES= \ a.cpp\ b.cpp\ # 要编译的源文件。这儿的_SOURCES是关键字 EXTRA_DIST= \ a.h \ b.h# 不用编成.o，但生成target myprogram也需要给编译器处理的头文件放这里 myprogram_LDADD = libsub1.a 这个_LDADD是关键字， # 最后生成myprogram这个执行文件，还要link src/sub1这个目录中的内容编成的一个lib :libsub1.a， myprogram_LDFLAGS = -lpthread -lglib-2.0 -L/usr/bin $(all_libraries) # myprogram还要link系统中的动态so，以此类推，需要连自编译的so,也写到这个关键字 _LDFLAGS后面就好了。AM_CXXFLAGS = -D_LINUX # 传递给g++编译器的一些编译宏定义，选项，

INCLUDES=-IPassport -Isub1/ -I/usr/include/glib-2.0\ -I/usr/lib/glib-2.0/include $(all_includes)

# 传递给编译器的头文件路径。

下面是sub1种生成lib的Makefile.am noinst_LIBRARIES = libprotocol.a # 不是生成可执行文件，而是静态库，target用noinst_LIBRARIES libprotocol_a_SOURCES = \ alib.cpp EXTRA_DIST = mylib.h\ alib.h INCLUDES= -I../ $(all_includes)

AM_CXXFLAGS = -D_LINUX -DONLY_EPOLL -D_SERVER

ok ,最后补上AC_PROG_RANLIB涵义，如果要自己生成lib，然后link到最终的可执行文件中，则要加上这个宏，否则不用。

2\. 剩下的就是 automake --add-missing Ok , Makefile.in应该放到各个目录下了。
