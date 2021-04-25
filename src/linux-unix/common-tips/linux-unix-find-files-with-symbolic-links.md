
date: None  
author(s): None  

# [Linux / UNIX find files with symbolic links - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/linux-unix-find-files-with-symbolic-links)

<http://www.cyberciti.biz/faq/linux-unix-find-files-with-symbolic-links/>

Q. How do I find file with symbolic links. Find command is not working for me. So how do I find files across symbolic links under CentOS 5.0?

A. Find command search for files in a directory hierarchy. You need to tell find command to follow symbolic links. When find examines or prints information about files, the information used shall be taken from the properties of the file to which the link points, not from the link itself (unless it is a broken symbolic link or find is unable to examine the file to which the link points). 

**find command -L option - follow symbolic links**

When the -L option is in effect, the -type predicate will always match against the type of the file that a symbolic link points to rather than the link itself (unless the symbolic link is broken). Using -L causes the -lname and -ilname predicates always to return false.

Type command as follows:  


find -L /path/to/searh "files"

For example find all *.jpg:  


$ find -L /data -iname "*.jpg"  
  
  
---

