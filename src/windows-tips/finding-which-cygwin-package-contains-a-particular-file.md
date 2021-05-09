# [Finding which cygwin package contains a particular file](http://www.trueblade.com/knowledge/finding-which-cygwin-package-contains-a-particular-file)

I often need to install a cygwin package to get a single file, but I can't find which package I need. This article explains how.

The other day I needed to install the cygwin "strings" command. No problem, I'll just run the cygwin installer, grab the "strings" package, and I'll be all set. But not so fast. There is no "strings" package; "strings" is part of some other package. But which one? I finally stumbled upon the cygwin package-grep facility. By using the URL:

<http://cygwin.com/cgi-bin2/package-grep.cgi?grep=strings.exe>

I was able to determine that strings.exe is in the "binutils" package.  A few minutes later, I was happily using the "strings" command.

I haven't found a user interface to package-grep, so I just build the URL by hand.
