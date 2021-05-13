# [Who is listening on a given TCP port on Mac OS X?](http://stackoverflow.com/questions/4421633/who-is-listening-on-a-given-tcp-port-on-mac-os-x)

    lsof -n -i4TCP:$PORT | grep LISTEN
