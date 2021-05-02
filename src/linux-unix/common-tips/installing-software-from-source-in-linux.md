# [Installing software from source in Linux](http://www.tuxfiles.org/linuxhelp/softinstall.html)

## < The procedure >

The installation procedure for software that comes in tar.gz and tar.bz2 packages isn't always the same, but usually it's like this:

```
# tar xvzf package.tar.gz (or tar xvjf package.tar.bz2)
# cd package
# ./configure
# make
# make install
```

If you're lucky, by issuing these simple commands you unpack, configure, compile, and install the software package and you don't even have to know what you're doing. However, it's healthy to take a closer look at the installation procedure and see what these steps mean.

## < Step 1. Unpacking >

Maybe you've already noticed that the package containing the source code of the program has a `tar.gz` or a `tar.bz2` extension. This means that the package is a compressed tar archive, also known as a tarball. When making the package, the source code and the other needed files were piled together in a single tar archive, hence the `tar` extension. After piling them all together in the tar archive, the archive was compressed with gzip, hence the `gz` extension.

Some people want to compress the tar archive with `bzip2` instead of `gzip`. In these cases the package has a `tar.bz2` extension. You install these packages exactly the same way as `tar.gz` packages, but you use a bit different command when unpacking.

It doesn't matter where you put the tarballs you download from the internet but I suggest creating a special directory for downloaded tarballs. In this tutorial I assume you keep tarballs in a directory called `dls` that you've created under your home directory. However, the `dls` directory is just an example. You can put your downloaded `tar.gz` or `tar.bz2` software packages into any directory you want. In this example I assume your username is `me` and you've downloaded a package called pkg.tar.gz into the `dls` directory you've created (/home/me/dls).

Ok, finally on to unpacking the tarball. After downloading the package, you unpack it with this command:

```
me@puter: ~/dls$ tar xvzf pkg.tar.gz
```

As you can see, you use the `tar` command with the appropriate options (`xvzf`) for unpacking the tarball. If you have a package with `tar.bz2` extension instead, you must tell `tar` that this isn't a gzipped tar archive. You do so by using the `j` option instead of `z`, like this:

```
me@puter: ~/dls$ tar xvjf pkg.tar.bz2
```

What happens after unpacking, depends on the package, but in most cases a directory with the package's name is created. The newly created directory goes under the directory where you are right now. To be sure, you can give the `ls` command:

```
me@puter: ~/dls$ **ls** pkg pkg.tar.gz
me@puter: ~/dls$
```

In our example unpacking our package pkg.tar.gz did what expected and created a directory with the package's name. Now you must `cd` into that newly created directory:

```
me@puter: ~/dls$ **cd pkg**
me@puter: ~/dls/pkg$
```

Read any documentation you find in this directory, like README or INSTALL files, before continuing!

## < Step 2. Configuring >
Now, after we've changed into the package's directory (and done a little RTFM'ing), it's time to configure the package. Usually, but not always (that's why you need to check out the README and INSTALL files) it's done by running the configure script.

You run the script with this command:

```
me@puter: ~/dls/pkg$ ./configure
```

When you run the configure script, you don't actually compile anything yet. configure just checks your system and assigns values for system-dependent variables. These values are used for generating a Makefile. The Makefile in turn is used for generating the actual binary.

When you run the configure script, you'll see a bunch of weird messages scrolling on your screen. This is normal and you shouldn't worry about it. If configure finds an error, it complains about it and exits. However, if everything works like it should, configure doesn't complain about anything, exits, and shuts up.

If configure exited without errors, it's time to move on to the next step.

## < Step 3. Building >
It's finally time to actually build the binary, the executable program, from the source code. This is done by running the make command:

```
me@puter: ~/dls/pkg$ make
```

Note that make needs the Makefile for building the program. Otherwise it doesn't know what to do. This is why it's so important to run the configure script successfully, or generate the Makefile some other way.

When you run make, you'll see again a bunch of strange messages filling your screen. This is also perfectly normal and nothing you should worry about. This step may take some time, depending on how big the program is and how fast your computer is. If you're doing this on an old dementic rig with a snail processor, go grab yourself some coffee. At this point I usually lose my patience completely.

If all goes as it should, your executable is finished and ready to run after make has done its job. Now, the final step is to install the program.


## < Step 4. Installing >
Now it's finally time to install the program. When doing this you must be root. If you've done things as a normal user, you can become root with the su command. It'll ask you the root password and then you're ready for the final step!

```
me@puter: ~/dls/pkg$ su
Password:
root@puter: /home/me/dls/pkg#
```

Now when you're root, you can install the program with the make install command:

```
root@puter: /home/me/dls/pkg# make install
```

Again, you'll get some weird messages scrolling on the screen. After it's stopped, congrats: you've installed the software and you're ready to run it!

Because in this example we didn't change the behavior of the configure script, the program was installed in the default place. In many cases it's /usr/local/bin. If /usr/local/bin (or whatever place your program was installed in) is already in your PATH, you can just run the program by typing its name.

And one more thing: if you became root with su, you'd better get back your normal user privileges before you do something stupid. Type exit to become a normal user again:

```
root@puter: /home/me/dls/pkg# exit
exit
me@puter: ~/dls/pkg$
```

## < Cleaning up the mess >
I bet you want to save some disk space. If this is the case, you'll want to get rid of some files you don't need. When you ran make it created all sorts of files that were needed during the build process but are useless now and are just taking up disk space. This is why you'll want to make clean:

```
me@puter: ~/dls/pkg$ make clean
```

However, make sure you keep your Makefile. It's needed if you later decide to uninstall the program and want to do it as painlessly as possible!

## < Uninstalling >
So, you decided you didn't like the program after all? Uninstalling the programs you've compiled yourself isn't as easy as uninstalling programs you've installed with a package manager, like rpm.

If you want to uninstall the software you've compiled yourself, do the obvious: do some old-fashioned RTFM'ig. Read the documentation that came with your software package and see if it says anything about uninstalling. If it doesn't, you can start pulling your hair out.

If you didn't delete your Makefile, you may be able to remove the program by doing a make uninstall:

```
root@puter: /home/me/dls/pkg# make uninstall
```

If you see weird text scrolling on your screen (but at this point you've probably got used to weird text filling the screen? :-) that's a good sign. If make starts complaining at you, that's a bad sign. Then you'll have to remove the program files manually.

If you know where the program was installed, you'll have to manually delete the installed files or the directory where your program is. If you have no idea where all the files are, you'll have to read the Makefile and see where all the files got installed, and then delete them.
