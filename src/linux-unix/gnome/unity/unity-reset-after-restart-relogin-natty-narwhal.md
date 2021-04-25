
date: None  
author(s): None  

# [Unity Reset after Restart / Relogin, Natty Narwhal - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/gnome/unity/unity-reset-after-restart-relogin-natty-narwhal)

<http://ubuntu4beginners.blogspot.com/2011/07/unity-reset-after-restart-relogin.html>

You may have the issue that changes you do to Unity, for example, adding launchers to the side bar or changing settings in Dconf, also regarding the top panel, are not remembered on reboot/relogin. One possible cause is that you tried Gnome 3 and reverted back to Gnome 2 delivered with Natty Narwhal. Not at least because Unity doesn't work with Gnome 3 yet. But there are, of course, multiple other reasons that may have led to this.The culprit is that the package "libdconf0" is either not installed or corrupted. So, we'll check if it is installed and then either install or reinstall it. Of course, this could also be done with a single step --by just running the latter most command-- but you may want to know what's going on, right!? And make the process more transparent.

Check if the package "libdconf0" is installed:

If it doesn't show up there, install it:

sudo apt-get install libdconf0

If it does show up there, thus being seemingly corrupted, reinstall it:

sudo apt-get install --reinstall libdconf0

Then relogin to make the changes take effect.

That's all, hopefully!

