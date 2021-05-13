# [How to run an alias in a shell script?](http://askubuntu.com/questions/98782/how-to-run-an-alias-in-a-shell-script)


Alias are deprecated in favor of shell functions. From `bash` manual page:

>For almost every purpose, aliases are superseded by shell functions.

To create a function, and export it to subshells, put the following in your `~/.bashrc`:


    petsc() { ~/petsc-3.2-p6/petsc-arch/bin/mpiexec "$@"
    }
    export -f petsc

Then you can freely call your command from your scripts.
