# [Group management on Linux](https://wiki.archlinux.org/index.php/Users_and_Groups)

`/etc/group` is the file that defines the groups on the system (`man group` for details).

Display group membership with the `groups` command:


    $ groups [user]


If `user` is omitted, the current user's group names are displayed.

The `id` command provides additional detail, such as the user's UID and associated GIDs:


    $ id [user]


To list all groups on the system:


    $ cat /etc/group


Create new groups with the `groupadd` command:


    # groupadd [group]


Add users to a group with the `gpasswd` command:


    # gpasswd -a [user] [group]


To delete existing groups:


    # groupdel [group]


To remove users from a group:


    # gpasswd -d [user] [group]


If the user is currently logged in, he/she must log out and in again for the change to have effect.

---
