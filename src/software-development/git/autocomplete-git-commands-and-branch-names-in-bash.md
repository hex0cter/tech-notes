# [Autocomplete Git Commands and Branch Names in Bash](http://code-worrier.com/blog/autocomplete-git/)

In bash in Mac OS X, you can use [TAB] to autocomplete file paths. Wouldn’t if be nice if you could do the same with git commands and branch names?

You can. Here’s how.

First get the `git-completion.bash` script (view it [here](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash)) and put it in your home directory:

    curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash


Next, add the following lines to your `.bash_profile`. This tells bash to execute the git autocomplete script if it exists.


    if [ -f ~/.git-completion.bash ]; then
     . ~/.git-completion.bash
    fi


Now open a new shell, `cd` into a git repo, and start typing a git command. You should find that [TAB] now autocompletes git commands and git branch names.

For example, if you type `git` then add a space and hit [TAB], you’ll get a readout like this, which lists all available git commands:

    add filter-branch reflog
    am format-patch relink
    annotate fsck remote
    apply gc repack
    archive get-tar-commit-id replace
    bisect grep request-pull
    blame gui reset
    branch help revert
    bundle imap-send rm
    checkout init send-email
    cherry instaweb shortlog
    cherry-pick log show
    citool merge show-branch
    clean mergetool stage
    clone mv stash
    commit name-rev status
    config notes submodule
    describe p4 svn
    diff pull tag
    difftool push whatchanged
    fetch rebase


Now to learn what some of these more exotic git commands do! What’s your favorite git command?

(I learned this way of installing `git-completion.bash` [here](http://apple.stackexchange.com/questions/55875/how-can-i-get-git-to-autocomplete-e-g-branches-at-the-command-line/55886#55886).)
