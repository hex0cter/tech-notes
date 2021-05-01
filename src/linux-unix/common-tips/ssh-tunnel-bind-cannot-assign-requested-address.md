# [SSH tunnel: bind: Cannot assign requested address](http://serverfault.com/questions/444295/ssh-tunnel-bind-cannot-assign-requested-address)

When creating a SSH tunnel using local port forwarding generates the error below:
```
ssh -L 22203:localhost:22203 -v user@host
debug1: Local forwarding listening on ::1 port 22203.
bind: Cannot assign requested address
```

Answer:
```
ssh -4 -L 22203:localhost:22203 -v user@host
```
