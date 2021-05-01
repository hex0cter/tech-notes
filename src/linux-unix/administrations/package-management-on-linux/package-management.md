# package management on Debian/Ubuntu

Maybe you suspect that the file in question is supposed to be provided by the same package you're working with.


    dpkg -L <packagename>

will show you a list of files provided by that package. For example, you've just installed kxdocker_0.32-1_i386.deb and your first guess, "kxdocker", doesn't run the program.


    $ kxdocker
    -bash: kxdocker: command not found

Well it's in there somewhere:


    $ dpkg -L kxdocker | grep bin
    /usr/local/kde/bin
    /usr/local/kde/bin/kxdocker

Ah, it's there, but /usr/local/kde/bin isn't in your $PATH. Now you know that you can add it to your $PATH or run the command with the full path.

### dpkg -S

Sometimes you might want to find out which package provides a certain file.


    dpkg -S /full/path/to/file
