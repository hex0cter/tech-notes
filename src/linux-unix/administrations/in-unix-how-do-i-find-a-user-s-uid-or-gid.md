# [In Unix, how do I find a user's UID or GID?](http://kb.iu.edu/data/adwf.html)

To find a user's UID or GID in Unix, use the `id` command. To find a specific user's UID, at the Unix prompt, enter:
```
id -u username
```

Replace `username` with the appropriate user's username. To find a user's GID, at the Unix prompt, enter:
```
id -g username
```

If you wish to find out all the [groups](http://kb.indiana.edu/data/aeqw.html) a user belongs to, instead enter:
```
id -G username
```

If you wish to see the UID and all groups associated with a user, enter `id` without any options, as follows:
```
id username
```
