# [How To Make a Shared Library in C](http://www.unixguide.net/linux/faq/05.11.shtml)


```
$ gcc -fPIC -c *.c
$ gcc -shared -Wl,-soname,libfoo.so -o libfoo.so *.o
```
