
date: None  
author(s): None  

# [ssh passphrase for git pull - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/git/ssh-passphrase-for-git-pull)

https://stackoverflow.com/questions/21095054/ssh-key-still-asking-for-password-and-passphrase?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

`~/git/jenkins-config(master ✔) git pull`

`Enter passphrase for key '/Users/daniel.han/.ssh/id_rsa':`

`Already up to date.`

`~/git/jenkins-config(master ✔) ssh-add ~/.ssh/id_rsa`

`Enter passphrase for /Users/daniel.han/.ssh/id_rsa:`

`Identity added: /Users/daniel.han/.ssh/id_rsa (/Users/daniel.han/.ssh/id_rsa)`

`~/git/jenkins-config(master ✔) git pull`

`Already up to date.`  
  
---

