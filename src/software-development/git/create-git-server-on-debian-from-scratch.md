# [Create git server on debian from scratch](http://www.hackido.com/2010/01/installing-git-on-server-ubuntu-or.html)

On Debian server (address: 10.10.10.10):

```
daniel@daniel-debian:/etc/ssh# sudo apt-get install gitosis
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
  python-setuptools
Suggested packages:
  git-daemon-run gitweb
The following NEW packages will be installed:
  gitosis python-setuptools
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.

daniel@daniel-debian:~$ sudo adduser \
>   --system \
>   --shell /bin/sh \
>   --gecos 'git version control' \
>   --group \
>   --disabled-password \
>   --home /home/git \
>   git
[sudo] password for daniel:
Adding system user `git' (UID 114) ...
Adding new group `git' (GID 123) ...
Adding new user `git' (UID 114) with group `git' ...
Creating home directory `/home/git' ...

daniel@daniel-debian:~$ sudo su

root@daniel-debian:/home/daniel# cd ~git

root@daniel-debian:/home/git# sudo -H -u git gitosis-init < /tmp/id_rsa.pub.daniel
Initialized empty Git repository in /home/git/repositories/gitosis-admin.git/
Reinitialized existing Git repository in /home/git/repositories/gitosis-admin.git/

root@daniel-debian:/home/git# ls
gitosis  repositories
```

On Ubuntu client:
```
daniel@daniel-ubuntu ~/Git $ git clone git@10.10.10.10:gitosis-admin.git
Cloning into gitosis-admin...
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 0), reused 5 (delta 0)
Receiving objects: 100% (5/5), done.

daniel@daniel-ubuntu ~/Git $ ls
gitosis-admin  intel-sdk

daniel@daniel-ubuntu ~/Git $ cd gitosis-admin/

daniel@daniel-ubuntu ~/Git/gitosis-admin $ ls
gitosis.conf  keydir

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git status
# On branch master
nothing to commit (working directory clean)

daniel@daniel-ubuntu ~/Git/gitosis-admin $ vi gitosis.conf

daniel@daniel-ubuntu ~/Git/gitosis-admin $ man git-commit

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
# modified:   gitosis.conf
#
no changes added to commit (use "git add" and/or "git commit -a")

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git add gitosis.conf

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git status
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
# modified:   gitosis.conf
#

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git diff --cached
diff --git a/gitosis.conf b/gitosis.conf
index 619fe0f..a7457a2 100644
--- a/gitosis.conf
+++ b/gitosis.conf
@@ -4,3 +4,7 @@
 writable = gitosis-admin
 members = daniel@daniel-ubuntu

+[group personal-web]
+writable = personal-web
+members = daniel@daniel-ubuntu
+

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git commit -m 'Added person-web repository'
[master 298eea2] Added person-web repository
 1 files changed, 4 insertions(+), 0 deletions(-)

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git push --dry-run
To git@10.10.10.10:gitosis-admin.git
   251bca1..298eea2  master -> master

daniel@daniel-ubuntu ~/Git/gitosis-admin $ git push
Counting objects: 5, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 381 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@10.10.10.10:gitosis-admin.git
   251bca1..298eea2  master -> master

daniel@daniel-ubuntu ~/Git/gitosis-admin $ cd ..

daniel@daniel-ubuntu ~/Git $ mkdir personal-web

daniel@daniel-ubuntu ~/Git $ cd personal-web/

daniel@daniel-ubuntu ~/Git/personal-web $ ls

daniel@daniel-ubuntu ~/Git/personal-web $ git init
Initialized empty Git repository in /home/daniel/Git/personal-web/.git/

daniel@daniel-ubuntu ~/Git/personal-web $ git remote add origin git@10.10.10.10:personal-web.git

daniel@daniel-ubuntu ~/Git/personal-web $ git status
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)

daniel@daniel-ubuntu ~/Git/personal-web $ git push origin master:refs/heads/master
error: src refspec master does not match any.
error: failed to push some refs to 'git@10.10.10.10:personal-web.git'

daniel@daniel-ubuntu ~/Git/personal-web $ ls

daniel@daniel-ubuntu ~/Git/personal-web $ touch ok

daniel@daniel-ubuntu ~/Git/personal-web $ ls
ok

daniel@daniel-ubuntu ~/Git/personal-web $ git add ok

daniel@daniel-ubuntu ~/Git/personal-web $ git commit -m 'initialized new repository'
[master (root-commit) f6c45dd] initialized new repository
 0 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 ok

daniel@daniel-ubuntu ~/Git/personal-web $ git push origin master:refs/heads/master
Counting objects: 3, done.
Writing objects: 100% (3/3), 221 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
To git@10.10.10.10:personal-web.git
 * [new branch]      master -> master
```
Now you should be able to clone the repository from anywhere else:
```
daniel@daniel-ubuntu /tmp $ git clone git@10.10.10.10:personal-web.git
Cloning into personal-web...
remote: Counting objects: 3, done.
Receiving objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
```
That's it!

---

Now assume another user wants to access this repository, or you yourself want to access it from another machine, say daniel-mint.

First, on daniel-mint, generate the ssh key pair with
```
daniel@daniel-mint:~/.ssh$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/daniel/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/daniel/.ssh/id_rsa.
Your public key has been saved in /home/daniel/.ssh/id_rsa.pub.
The key fingerprint is:
44:aa:49:11:ce:01:d9:ab:2d:d9:de:f2:c4:11:15:d1 daniel@daniel-mint
The key's randomart image is:
+--[ RSA 2048]----+
|  .++.  =+       |
|  .o.o +  E      |
|    +.o .        |
|   ..o o         |
|   =o . S        |
|  + o. .         |
|   o .o          |
|    o..          |
|     o.          |
+-----------------+
daniel@daniel-mint:~/.ssh$ ls
id_rsa  id_rsa.pub
```
Then on daniel-ubuntu (the one has gitosis-admin repo),
```
cd ~/Git/gitosis-admin/keydir
scp daniel@daniel-mint:.ssh/id_rsa.pub daniel@daniel-mint.pub
vi ~/Git/gitosis-admin/gitosis.conf
```

Add the following line to personal-web section:
```
 [group personal-web]
 writable = personal-web
 members = dhan@dhan-ubuntu daniel@daniel-mint
```
Now stage/commit and push the change. You should be able to clone the personal-web repo from daniel-mint.
```
daniel@daniel-mint:~/git$ git clone git@10.10.10.10:personal-web.git
Cloning into personal-web...
remote: Counting objects: 952, done.
remote: Compressing objects: 100% (695/695), done.
remote: Total 952 (delta 233), reused 949 (delta 233)
Receiving objects: 100% (952/952), 2.64 MiB | 2.34 MiB/s, done.
Resolving deltas: 100% (233/233), done.
```
