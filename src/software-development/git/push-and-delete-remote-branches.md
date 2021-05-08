# [push and delete remote branches](http://gitready.com/beginner/2009/02/02/push-and-delete-branches.html)


This is an action that many Git users need to do frequently, but many (including the author) have forgotten how to do so or simply don’t know how. Here’s the definitive guide if you’ve forgotten.

So let’s say you have [checked out a new branch](http://gitready.com/beginner/2009/01/25/branching-and-merging.html), committed some awesome changes, but now you need to share this branch though with another developer. You can push the branch up to a remote very simply:

```
git push origin newfeature
```

Where `origin` is your remote name and `newfeature` is the name of the branch you want to push up. This is by far the easiest way, but there’s another way if you want a different option. [Geoff Lane](http://zorched.net/)has created a [great tutorial](http://www.zorched.net/2008/04/14/start-a-new-branch-on-your-remote-git-repository/) which goes over how to push a ref to a remote repository, fetch any updates, and then start tracking the branch.

Deleting is also a pretty simple task (despite it feeling a bit kludgy):

```
git push origin :newfeature
```

That will delete the `newfeature` branch **on the`origin` remote** , but you’ll still need to delete the branch locally with `git branch -d newfeature`.
