# [What process created this X11 window?](http://unix.stackexchange.com/questions/5478/what-process-created-this-x11-window)

```
xdotool selectwindow getwindowpid
ps -ef | grep <pid>
```
