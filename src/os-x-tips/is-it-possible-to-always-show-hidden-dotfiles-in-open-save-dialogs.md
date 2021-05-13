# [Is it possible to always show hidden/dotfiles in Open/Save dialogs?](http://apple.stackexchange.com/questions/99213/is-it-possible-to-always-show-hidden-dotfiles-in-open-save-dialogs)

Just adding the key to the global domain seems to work:


    defaults write -g AppleShowAllFiles -bool true


You have to quit and reopen applications to apply changes as usual.
