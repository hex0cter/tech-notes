
date: None  
author(s): None  

# [Using sudo - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/using-sudo)

Most systems have some way of letting ordinary users perform certain tasks as root or some other privileged user. SCO Open Server has "asroot" and can also directly assign "authorizations" such as backup privileges or being able to change other user's passwords. SCO Unixware/Open Unix 8 have a similar facility in "tfadmin".

Many other Unixes, and Linux, use **"sudo"**.

The configuration of sudo is by the /etc/sudoers file. I'm sure that there are more poorly written man pages, but "man sudoers" is among my all time favorites for obfuscation and poor explanation. The creation of the file and the actual use of sudo isn't all that bad though.

First a little background. The sudo program itself is a setuid binary. If you examine its permissions, you will see:

  

    
    
    ---s--x--x    1 root   root   81644 Jan 14 15:36 /usr/bin/sudo
     
    

That "s" means that this is a "setuid" program. You and everyone else have execute permission on this, so you can run it. When you do that, because it is setuid and owned by root, your effective user id becomes root- if you could get to a shell from sudo, you effectively WOULD be root- you could remove any file on the system, etc. That's why setuid programs have to be carefully written, and something like sudo (which is going to allow access to other programs) has to be especially careful.

A setuid program doesn't necessarily mean root access. A setuid program owned by a different user would give you that user's effective id. The sudo program can also change your effective id while it is running- I'll be showing an example of that here.

Finally, setuid and sudo are NOT the same thing as the administrative roles of Unixware or the authorizations and privileges of SCO Openserver. Those are entirely different concepts and I won't be talking about those things in this article.

## /etc/sudoers

You use "visudo" to edit the sudoers file. There are two reasons for that- it prevents two users from editing the file at the same time, and it also provides limited syntax checking. Even if you are the only root user, you need the syntax checking, so use "visudo".

We're going to start with the simplest setup of all: giving someone full root access. You might think there's no reason to do this- it would make more sense just to give them the root password, wouldn't it? Well, maybe, but then they can login as root also- with sudo they will have to use the sudo command and we can require a password that IS NOT root's password. Sudo commands can be logged, so we can keep track of what the person did. We can turn their sudo capability on or off at will without affecting other sudo users- no need to change the root password back and forth. This is a great way to keep track of consultants and other support people who may need root power, but you want to keep tabs on what they do. Of course there's a strong implication of honesty here- such a user could edit the sudo logs to hide any mischief.

So, here's a simple /etc/sudoers file (remember, edit with "visudo") to give "jim" access to root commands.
    
    
    # sudoers file.
    #
    # This file MUST be edited with the 'visudo' command as root.
    #
    
    # User privilege specification
    root    ALL=(ALL) ALL
    jim     ALL=(ALL)       ALL
    
    

That's it. With this in place, "jim" can use sudo to run any command with root privileges. Here's "jim" catting /etc/shadow:
    
    
    [jim@lnxserve jim]$ head -5 /etc/shadow
    cat: /etc/shadow: Permission denied
    [jim@lnxserve jim]$ sudo head -5 /etc/shadow
    Password:
    root:$1$bukQnNBS$dkGDMUTf1.W5r1VE4OYLy.:11595:0:99999:7:::
    bin:*:11595:0:99999:7:::
    daemon:*:11595:0:99999:7:::
    adm:*:11595:0:99999:7:::
    lp:*:11595:0:99999:7:::
    [jim@lnxserve jim]$ 
    
    

Note that "jim" does not get root's PATH; his PATH is used by sudo (with exceptions noted later). If "jim" wanted to run (for example) lpc, he'd have to explicitly do "sudo /usr/sbin/lpc". That's typical, although sudo can be compiled to use its own compiled in PATH instead.

The password requested is NOT root's. In this case, "jim" has to provide his own login password to get sudo to work.

By default, sudo remembers the password for 5 minutes and won't ask again if reinvoked within that time:
    
    
    [jim@lnxserve jim]$ sudo head -5 /etc/shadow
    root:$1$bukQnNBS$dkGDMUTf1.W5r1VE4OYLy.:11595:0:99999:7:::
    bin:*:11595:0:99999:7:::
    daemon:*:11595:0:99999:7:::
    adm:*:11595:0:99999:7:::
    lp:*:11595:0:99999:7:::
    [jim@lnxserve jim]$ 
    
    

The password behavior is entirely configurable: the password can be set to time out earlier, later, never or to be required always. Additionally, the password requested can be root's instead of their own. Let's change "jim" a bit by adding this line:
    
    
    # Defaults specification
    Defaults:jim    timestamp_timeout=0, runaspw, passwd_tries=1
    
    

This changes three things. First, "jim" needs root's password to run sudo (because of "runaspw"). Second, the password will not be remembered (timestamp_timeout), and he gets only one chance to enter it (the default is three tries).

If we set timestamp_timeout to -1, "jim" will only have to prove that he knows the password once. After that, it will not be forgotten, even if he logs out.

Different users can, of course, have different defaults. Here I've changed "jim", and added a new user "linda"
    
    
    # sudoers file.
    #
    # This file MUST be edited with the 'visudo' command as root.
    #
    Defaults:jim    timestamp_timeout=0 
    Defaults:linda  timestamp_timeout=-1, runaspw
    
    # User privilege specification
    root    ALL=(ALL) ALL
    jim     ALL=(ALL)       ALL
    linda   ALL=(ALL)       ALL
    
    

Jim and Linda have diffrent defaults. A "Default" not followed by a ":" and a user name will apply to everyone (example further on).

