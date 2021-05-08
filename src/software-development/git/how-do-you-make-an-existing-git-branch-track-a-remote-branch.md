# [How do you make an existing Git branch track a remote branch?](http://stackoverflow.com/questions/520650/how-do-you-make-an-existing-git-branch-track-a-remote-branch)

Given a branch `foo` and a remote `upstream`:

 **As of Git 1.8.0:**

if you are standing on the branch already:

```
    git branch -u upstream/foo
    git branch -u origin/daniel_dev
```

Or, if local branch `foo` is not the current branch:

```
    git branch -u upstream/foo foo
```

Or, if you like to type longer commands, these are equivalent to the above two:

```
    git branch --set-upstream-to=upstream/foo
    git branch --set-upstream-to=upstream/foo foo
```

**As of Git 1.7.0:**

```
    git branch --set-upstream foo upstream/foo
```
