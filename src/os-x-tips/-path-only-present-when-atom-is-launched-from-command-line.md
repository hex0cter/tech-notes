
date: None  
author(s): None  

# [`$PATH` only present when Atom is launched from command line - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/os-x-tips/-path-only-present-when-atom-is-launched-from-command-line)

https://github.com/atom-community/linter/issues/150 

I am on ubuntu and the error fire even when launched from command line, even after adding the :
    
    
    process.env.PATH = ["/usr/local/bin", process.env.PATH].join(":")

line in ~/.atom/init.coffee (same for OS X)  
  
---

