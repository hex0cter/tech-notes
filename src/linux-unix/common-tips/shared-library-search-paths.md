# [Shared Library Search Paths](http://www.eyrie.org/~eagle/notes/rpath.html)

It's becoming more and more common these days to link everything against shared libraries, and in fact many software packages (Tcl and Cyrus SASL come to mind) basically just don't work properly static. This means that one has to more frequently deal with the issues involved in finding the appropriate libraries at runtime.

Here's a brief primer on the way that this works on Solaris and Linux. The search paths for libraries come from three sources: the environment variable LD_LIBRARY_PATH (if set), any rpath encoded in the binary (more on this later), and the system default search paths. They're searched in this order, and the first matching library found is used.

LD_LIBRARY_PATH is broken and should not be used if at all possible. It's broken because it overrides the search paths for all binaries that you run using it, not just the one that you care about, and it doesn't add easily to other competing settings of LD_LIBRARY_PATH. It has a tendency to cause odd breakage, and it's best to only use it with commercial applications like Oracle where there's no other choice (and then to set it only in a wrapper around a particular application, and never in your general shell environment).

Now, more about the other two mechanisms in detail.

## System default paths

Far and away the best way of handling shared libraries is to add every directory into which you install shared libraries to the system default paths. This doesn't work if you install a variety of conflicting libraries, but that's a rare case. If you're just installing software into /usr/local/lib, for example, then just add /usr/local/lib to your system default search paths.

On Linux, you do this by adding those directories to /etc/ld.so.conf and then running ldconfig. On Solaris, you do this by using the `crle` command (see the man page for more details).

This doesn't always work, though. The main case where this doesn't work is when you're installing shared libraries into a shared network file system for use throughout your cluster or enterprise. Then, you probably don't want to add that network file system to the default system search path, since that search path is used for every binary on the system, including ones integral to the operation of the system. If the network file system goes down, and the default search path includes it, the system will become unusable.

That leads to the next approach.
