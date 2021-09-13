
# [How to remove local untracked files from the current Git branch](https://koukia.ca/how-to-remove-local-untracked-files-from-the-current-git-branch-571c6ce9b6b1)

![](https://miro.medium.com/max/1024/1*SptUKxY2gmxa4XC3W1_nRw.jpeg)

Well, the short answer as per the Git Documents is [git clean](https://git-scm.com/docs/git-clean)

If you want to see which files will be deleted you can use the `-n` option
before you run the actual command:

Then when you are comfortable (because it will delete the files for real!) use
the **-f** option:

Here are some more options for you to delete directories, files, ignored and
non-ignored files

  * To remove directories, run `git clean -f -d` or `git clean -fd`
  * To remove ignored files, run `git clean -f -X` or `git clean -fX`
  * To remove ignored and non-ignored files, run `git clean -f -x` or `git clean -fx`

 **Note the case difference on the**` **X**` **for the two latter commands.**

If you use GIT regularly, I recommend to get this book and have it on your desk:

![](https://miro.medium.com/max/500/1*ZoGu8n3MF1M9bD9XQkmirQ.png)

> If you liked this article, click the👏 below so other people will see it here
on Medium.

>

> Let’s be friends on [Twitter](https://twitter.com/aramkoukia). Happy Coding :)

Cheers!

