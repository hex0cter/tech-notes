
date: None  
author(s): None  

# [greper - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/korn-shell/greper)

#!/bin/ksh## Usage: greper search-string## Greper will search all files for the given search-string,# starting at the current directory, and extending to all# subdirectories. Whenever the string is found, the relative# pathname and filename are printed, followed by a colon and# the line of the file which contains the search-string.## Example: To search for all occurances of the string# "example.funct" in the current working directory# and below, simply type:# greper example.funct## Author - Marvin Moser

#

if test $# -ne 1then echo Usage: greper search-string exit

fi

find . -type f -print | sed '/^.*\\.o$/d/^.*\\.out$/d' | xargs -l7 fgrep $1  
  
---

