# [可以去掉文件绝对路径的printf debug](http://pubs.opengroup.org/onlinepubs/009695399/functions/strrchr.html)

<http://blog.csdn.net/unbutun/archive/2010/02/02/5281282.aspx>

```
#define DEBUG(fmt, arg...)                                               \
            printf ("[%s@%d] " fmt"\n", strrchr (__FILE__, '/') == 0 ?   \
                             __FILE__ : strrchr (__FILE__, '/') + 1,     \
                             __LINE__, ##arg);
```

<http://pubs.opengroup.org/onlinepubs/009695399/functions/strrchr.html>
