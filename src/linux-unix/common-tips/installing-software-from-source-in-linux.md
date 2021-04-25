
date: None  
author(s): None  

# [Installing software from source in Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/installing-software-from-source-in-linux)

Maybe you've already noticed that the package containing the source code of the program has a `tar.gz` or a `tar.bz2` extension. This means that the package is a compressed tar archive, also known as a tarball. When making the package, the source code and the other needed files were piled together in a single tar archive, hence the `tar` extension. After piling them all together in the tar archive, the archive was compressed with gzip, hence the `gz` extension.

Some people want to compress the tar archive with `bzip2` instead of `gzip`. In these cases the package has a `tar.bz2` extension. You install these packages exactly the same way as `tar.gz` packages, but you use a bit different command when unpacking.

It doesn't matter where you put the tarballs you download from the internet but I suggest creating a special directory for downloaded tarballs. In this tutorial I assume you keep tarballs in a directory called `dls` that you've created under your home directory. However, the `dls` directory is just an example. You can put your downloaded `tar.gz` or `tar.bz2` software packages into any directory you want. In this example I assume your username is `me` and you've downloaded a package called pkg.tar.gz into the `dls` directory you've created (/home/me/dls).

Ok, finally on to unpacking the tarball. After downloading the package, you unpack it with this command:

`me@puter: ~/dls$ **tar xvzf pkg.tar.gz**`

As you can see, you use the `tar` command with the appropriate options (`xvzf`) for unpacking the tarball. If you have a package with `tar.bz2` extension instead, you must tell `tar` that this isn't a gzipped tar archive. You do so by using the `j` option instead of `z`, like this:

`me@puter: ~/dls$ **tar xvjf pkg.tar.bz2**`

What happens after unpacking, depends on the package, but in most cases a directory with the package's name is created. The newly created directory goes under the directory where you are right now. To be sure, you can give the `ls` command:

`me@puter: ~/dls$ **ls** pkg pkg.tar.gz

me@puter: ~/dls$

`

In our example unpacking our package pkg.tar.gz did what expected and created a directory with the package's name. Now you must `cd` into that newly created directory:

`me@puter: ~/dls$ **cd pkg**  
me@puter: ~/dls/pkg$`

Read any documentation you find in this directory, like README or INSTALL files, before continuing!

