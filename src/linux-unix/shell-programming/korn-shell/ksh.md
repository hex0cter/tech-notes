# [Korn Shell Tips](http://home.nyc.rr.com/computertaijutsu/ksh.html)

Lately, I switched over to the Korn Shell, ksh. There were a few reasons, including the fact that it can handle decimal numbers. Also, at work we use AIX and it has ksh but not bash. This page is for those who are changing from bash to ksh. It's not going to cover any of the sophisticated differences, but these were a few of the things that I had to look up before getting it to work the way I wanted it to work.

First of all, just putting a .kshrc in your /home directory won't work. The Korn Shell, rather than looking for an rc file, first reads /home/username/.profile. So, in your home directory, if there isn't a .profile file, create one. There is probably one there already, but if not, the important line is:
```
ENV=$HOME/.kshrc; export ENV
```

That will tell the shell to read the .kshrc file.

(Actually, I've found in OpenBSD that this doesn't always work--I usually wind up putting the PS1 prompt in my $HOME/.profile.)

Various flavors of Linux have the bash command "source" somewhere in a profile--sometimes in the premade /home/username/.profile and other times in /etc/profile. (Depending upon the distro, this might be /etc/profiles, /etc/.profile or /etc/profile.env) If this is the case, you will get an annoying error every time you log in, to the effect that the source command is not found. The ksh equivalent is exec. (A period with a space after it will also work.) So, find out where the source command is and change it. It'll usually be something like
```
if [ -f .bashrc ]; then
source .bashrc
fi
```

You'll note that it's looking for .bashrc. You can change that to read .kshrc and change the word source to exec, comment out the line, or whatever. Even if you leave it alone, things will work, but I'm anal and hate seeing error messages if I can fix them.

Another little stupid Korn Shell Trick is a prompt. I happen to like the default Gentoo Linux prompt, which gives you colors and a few other useful bits of information. So, when I switched to ksh on FreeBSD, which is what I usually use, I changed my prompt to duplicate it.
```
HOST=`hostname`
export PS1='^[[01;32m${USER}@^[[1;34m${HOST%%.*} ^[[01;36m${PWD##*/} $^[[0m '
```

First I make the variable HOST, which will duplicate the hostname command. (Note that those are backticks around the hostname command, not single quotes--the backtick is usually found next to the number 1 in the top row of a standard keyboard, sharing the key with ~, the tilde.)

The PS1 is in single quotes. The ^[ is not made by typing in a ^ and [. It is the escape character. In vi, you first hit ctrl+v to make the next character a literal one--this will produce the ^. Then, if you hit the Esc key, you should see a [ the left bracket. In most terminals, this first ^[ will show up in blue The second [ following that one in the 4 places where I use it, is the standard left bracket typed in. In each case it's used to escape the left bracket--otherwise your actual prompt would look like [scottro@[scottro11, etc, with the left brackets showing.
If your browser shows colors, this prompt would appear as
```
scottro@scottro11 html $
```
(Assuming I was in my html directory, which is where I am as I type this.)

Although some of my friends consider this a girly-man prompt, I find it handy and use it. If you don't like the colors, then simply remove the left brackets and numbers, so it would read
```
HOST=`hostname`
export PS1='${USER}@${HOST%%.*} ${PWD##*/} $ '
```

This is of course, assuming that you like your prompt to be that way--on this particular machine, for example it comes out as
```
scottro@scottro11 html $
```

On most boxes I've found that the tab key will automatically do filename completion. Once in awhile, I've run into that not working. Although there is another way to do it with Esc and something else (I've forgotten now) if it's not working, then sometimes adding the line
```
bind ^i=complete
```
can help. (On other boxes, depending upon what version of ksh you're using, you might get an error for that line, however.).

In NetBSD, you want the following
```
set -o emacs
bind "^I=complete"
```

AIX's ksh
The ksh that ships with IBM's AIX lacks tab completion and history with arrow keys. As googling for the solutions indicates that a great many people have the same question, here are the quick and dirty answers.

One can choose to set -o emacs or set -o vi. Most bash users are familiar with what this means. The default bash (and many other shells) option is emacs mode, where simple command line editing is possible using emacs style keystrokes. Using vi mode uses vi style keystrokes. However, even many vi users use emacs mode for the command line.

With AIX, one has to set this, either on the command line or in your .profile. If you choose the emacs mode, command and filename completion is done with esc esc (in other words, hitting the escape key twice.) History is done with ctl+p and ctl+n, as in previous and next. Googling gives some keybindings you can add to use the arrow keys instead, but I never bothered.

If you are in vi mode then esc \ gives filename and command completion and history is done with esc k for the previous command. If you want to keep going back, after the first time, you can just hit k.

Anyway, these were the little things I had to look up to get my ksh working as I wanted it to work. Hopefully, some may find it of use.
