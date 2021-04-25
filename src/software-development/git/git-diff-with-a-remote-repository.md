
date: None  
author(s): None  

# [git-diff with a remote repository - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/git/git-diff-with-a-remote-repository)

Hi,

Yesterday I learned how to do git-diff with a non local repository. Something cvs or svn does  
by default(for it’s their nature). Anyway, here is how you do it

Create a local reference to the remote repository as

**$ git-remote add -t master -m master pivot git@10.0.0.1:./my-project**

This will create a local reference named `pivot’, to a remote branch named `master’ under the  
repository `git@10.0.0.1:./my-project’. You can see this local reference using

**$ git-branch -r**  
**$ git-remote**

And now do the diff like you would do with any other local branch

**$ git-diff pivot**

This also helps to git-pull or git-push changes to a remote repository. Just say

**$ git-pull pivot**  
**$ git-push pivot**

from your working branch.

…enjoy! :)

<http://pjps.tumblr.com/post/96756489/git-diff-with-a-remote-repository>

(I haven't tried this yet)  
  
---

