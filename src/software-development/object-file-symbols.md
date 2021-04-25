
date: None  
author(s): None  

# [List object file symbols - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/object-file-symbols)

**dhan@dhan-ubuntu:~/Dropbox/Python/example/dbus-example$ nm -gC libreadline_wrap.so**

w _Jv_RegisterClasses

00002014 A __bss_start

w __cxa_finalize@@GLIBC_2.1.3

w __gmon_start__

00002014 A _edata

0000201c A _end

00000508 T _fini

00000348 T _init

U puts@@GLIBC_2.0

0000048c T read

U readline

 **dhan@dhan-ubuntu:~/Dropbox/Python/example/dbus-example$ nm -D libreadline_wrap.so**

will also help for dynamic library.

 **dhan@dhan-ubuntu:~/Dropbox/Python/example/dbus-example$ objdump -TC libreadline_wrap.so**

libreadline_wrap.so: file format elf32-i386

DYNAMIC SYMBOL TABLE:

00000000 w D *UND* 00000000 __gmon_start__

00000000 w D *UND* 00000000 _Jv_RegisterClasses

00000000 D *UND* 00000000 readline

00000000 DF *UND* 00000000 GLIBC_2.0 puts

00000000 w DF *UND* 00000000 GLIBC_2.1.3 __cxa_finalize

0000048c g DF .text 0000003b Base read

0000201c g D *ABS* 00000000 Base _end

00002014 g D *ABS* 00000000 Base _edata

00002014 g D *ABS* 00000000 Base __bss_start

00000348 g DF .init 00000000 Base _init

00000508 g DF .fini 00000000 Base _fini

<http://sourceware.org/binutils/docs/binutils/nm.html>

