# [set path in tcsh](http://www.oreillynet.com/cs/user/view/cs_msg/14542)


For my shell, tcsh, I changed my $PATH environment variable in .tcshrc like so:

```
set path = ($path /usr/local/bin)
```

Seems to work better this way.

http://www.oreillynet.com/cs/user/view/cs_msg/14542


NOTE: in tcsh, use path instead of capital PATH.
