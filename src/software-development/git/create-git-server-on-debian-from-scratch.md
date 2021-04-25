
date: None  
author(s): None  

# [Create git server on debian from scratch - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/git/create-git-server-on-debian-from-scratch)

`daniel@daniel-ubuntu ~/Git $ **git clone git@10.10.10.10:gitosis-admin.git**`

`Cloning into gitosis-admin...`

`remote: Counting objects: 5, done.`

`remote: Compressing objects: 100% (4/4), done.`

`remote: Total 5 (delta 0), reused 5 (delta 0)`

`Receiving objects: 100% (5/5), done.`

`daniel@daniel-ubuntu ~/Git $ **ls**`

`gitosis-admin intel-sdk`

`daniel@daniel-ubuntu ~/Git $ **cd gitosis-admin/**`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **ls**`

`gitosis.conf keydir`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git status**`

`# On branch master`

`nothing to commit (working directory clean)`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **vi gitosis.conf**`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **man git-commit**`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git status**`

`# On branch master`

`# Changes not staged for commit:`

`# (use "git add <file>..." to update what will be committed)`

`# (use "git checkout -- <file>..." to discard changes in working directory)`

`#`

`#` `modified: gitosis.conf`

`#`

`no changes added to commit (use "git add" and/or "git commit -a")`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git add gitosis.conf**`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git status**`

`# On branch master`

`# Changes to be committed:`

`# (use "git reset HEAD <file>..." to unstage)`

`#`

`#` `modified: gitosis.conf`

`#`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git diff --cached** `

`diff --git a/gitosis.conf b/gitosis.conf`

`index 619fe0f..a7457a2 100644`

`--- a/gitosis.conf`

`+++ b/gitosis.conf`

`@@ -4,3 +4,7 @@`

` writable = gitosis-admin`

` members = daniel@daniel-ubuntu`

`+[group personal-web]`

`+writable = personal-web`

`+members = daniel@daniel-ubuntu`

`+`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git commit -m 'Added person-web repository'**`

`[master 298eea2] Added person-web repository`

` 1 files changed, 4 insertions(+), 0 deletions(-)`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git push --dry-run** `

`To git@10.10.10.10:gitosis-admin.git`

` 251bca1..298eea2 master -> master`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **git push**`

`Counting objects: 5, done.`

`Delta compression using up to 2 threads.`

`Compressing objects: 100% (3/3), done.`

`Writing objects: 100% (3/3), 381 bytes, done.`

`Total 3 (delta 0), reused 0 (delta 0)`

`To git@10.10.10.10:gitosis-admin.git`

` 251bca1..298eea2 master -> master`

`daniel@daniel-ubuntu ~/Git/gitosis-admin $ **cd ..**`

`daniel@daniel-ubuntu ~/Git $ **mkdir personal-web**`

`daniel@daniel-ubuntu ~/Git $ **cd personal-web/**`

`daniel@daniel-ubuntu ~/Git/personal-web $ **ls**`

`daniel@daniel-ubuntu ~/Git/personal-web $ **git init**`

`Initialized empty Git repository in /home/daniel/Git/personal-web/.git/`

`daniel@daniel-ubuntu ~/Git/personal-web $ **git remote add origin git@10.10.10.10:personal-web.git**`

`daniel@daniel-ubuntu ~/Git/personal-web $ **git status**`

`# On branch master`

`#`

`# Initial commit`

`#`

`nothing to commit (create/copy files and use "git add" to track)`

`daniel@daniel-ubuntu ~/Git/personal-web $ **git push origin master:refs/heads/master**`

`error: src refspec master does not match any.`

`error: failed to push some refs to 'git@10.10.10.10:personal-web.git'`

`daniel@daniel-ubuntu ~/Git/personal-web $ **ls**`

`daniel@daniel-ubuntu ~/Git/personal-web $ **touch ok**`

`daniel@daniel-ubuntu ~/Git/personal-web $ **ls**`

`ok`

`daniel@daniel-ubuntu ~/Git/personal-web $ **git add ok**`

`daniel@daniel-ubuntu ~/Git/personal-web $ **git commit -m 'initialized new repository'**`

`[master (root-commit) f6c45dd] initialized new repository`

` 0 files changed, 0 insertions(+), 0 deletions(-)`

` create mode 100644 ok`

`daniel@daniel-ubuntu ~/Git/personal-web $ **git push origin master:refs/heads/master**`

`Counting objects: 3, done.`

`Writing objects: 100% (3/3), 221 bytes, done.`

`Total 3 (delta 0), reused 0 (delta 0)`

`To git@10.10.10.10:personal-web.git`

` * [new branch] master -> master`

