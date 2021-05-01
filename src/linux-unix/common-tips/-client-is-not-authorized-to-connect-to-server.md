# ["Client is not authorized to connect to server"](http://www.cs.washington.edu/lab/sw/uwcsexintro.html)

Usually a trio of messages, e.g.:

```
        Xlib:  connection to "stehekin:0.0" refused by server
        Xlib:  Client is not authorized to connect to server
        Error: Can't open display: stehekin:0
```

Make sure your `.Xauthority` file on the client side has an entry for the X server you want to use. Or, use the `xhost` command to force the server to accept clients. See man pages for `xauth` and`xhost`.
