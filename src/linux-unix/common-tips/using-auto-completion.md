
date: None  
author(s): None  

# [Using auto-completion - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/using-auto-completion)

If you are lazy enough that you don't want to type the entire _make menuconfig_ command line, you can enable auto-completion in your shell. Here is how you can do that using _bash_ :
    
    
    $ complete -W menuconfig make
    

Then just enter the beginning of the line, and ask _bash_ to complete it for you by pressing the _TAB_ key:
    
    
    $ make me<TAB>
    

will result in _bash_ to append _nuconfig_ for you!

Alternatively, some distributions (of which Debian and Mandriva are but an example) have more powerful make completion. Depending on you distribution, you may have to install a package to enable completion. Under Mandriva, this is _bash-completion_ , while Debian ships it as part of the _bash_ package.

Other shells, such as _zsh_ , also have completion facilities. See the documentation for your shell.

