
date: None  
author(s): None  

# [How to create a git repository - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/git/git-1)

1\. apt-get install git-core

apt-get install python-setuptools

apt-get install gitosis

3\. git clone git://eagain.net/gitosis

4\. cd gitosis

5\. python setup.py install

6\. sudo adduser --system --shell /bin/sh --gecos 'git version control' --group --disabled-password --home /home/git git

7\. ssh-keygen -t rsa (ran by administrator, for example, root)

8\. sudo -H -u git gitosis-init < $HOME/.ssh/id_rsa.pub

9\. git clone git@127.0.0.1:gitosis-admin.git (server address may vary. This command is only usable for the administrator for now.)  
  
---

