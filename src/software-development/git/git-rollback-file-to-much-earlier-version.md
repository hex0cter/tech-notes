
date: None  
author(s): None  

# [Git: Rollback file to much earlier version - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/git/git-rollback-file-to-much-earlier-version)

<http://stackoverflow.com/questions/373812/rollback-file-to-much-earlier-version>

ometimes you just want to go back and forget about every change past a certain point because they're all wrong.

Start with:

`$ git log`

which shows you a list of recent commits, and their SHA1 hashes.

Next, type:

`$ git reset --hard SHA1_HASH`

to restore the state to a given commit and erase all newer commits from the record permanently.

THIS COMMAND MUST BE USED WITH CAUTION! All tracked files (either stashed or unstashed or committed) will be reset!!!  
  
---

