# [Pass Shell Variables To awk](http://www.cyberciti.biz/faq/linux-unix-appleosx-bsd-bash-passing-variables-to-awk/)

How do I pass shell variables to awk command or script under UNIX like operating systems?

The -v option can be used to pass [shell variables](http://bash.cyberciti.biz/guide/Variables) to awk command. Consider the following simple example,

```
root="/webroot"
echo | awk -v r=$root '{ print "shell root value - " r}'
```
