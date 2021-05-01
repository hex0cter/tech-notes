# [How do I get rid of those "rc" packages?](http://www.linuxquestions.org/questions/debian-26/how-do-i-get-rid-of-those-rc-packages-as-seen-in-dpkg-l-output-418956/)

```
dpkg --list | grep <package>
dpkg -P <package>
```
