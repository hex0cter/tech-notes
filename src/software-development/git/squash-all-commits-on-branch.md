# [Git: How to squash all commits on branch](https://stackoverflow.com/questions/25356810/git-how-to-squash-all-commits-on-branch)

Assume the base branch is `master`

```
git checkout yourBranch
git reset $(git merge-base master $(git branch --show-current))
git add -A
git commit -m "one commit on yourBranch"
```
