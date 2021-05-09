# [How to Convince apt-get *not* to use IPv6 method](http://unix.stackexchange.com/questions/9940/convince-apt-get-not-to-use-ipv6-method)

Append the following to /etc/gai.conf

```
precedence ::ffff:0:0/96  100
precedence 2001:470::/32 100
```
