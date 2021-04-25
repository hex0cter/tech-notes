# [Change time zone on Ubuntu](http://webonrails.com/2009/07/15/change-timezone-of-ubuntu-machine-from-command-line/)
If you guys want to change timezone of your ubuntu machine then you can do it by issuing:

```
dpkg-reconfigure tzdata
```
This may be helpful if you deal with servers.

Non-interactively:

```
# echo "Europe/Dublin" > /etc/timezone
# dpkg-reconfigure -f noninteractive tzdata
```

<http://webonrails.com/2009/07/15/change-timezone-of-ubuntu-machine-from-command-line/>

<http://stackoverflow.com/questions/8671308/non-interactive-method-for-dpkg-reconfigure-tzdata>
