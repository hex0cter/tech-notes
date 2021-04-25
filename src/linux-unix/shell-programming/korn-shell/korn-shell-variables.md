
date: None  
author(s): None  

# [Korn Shell Variables - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/korn-shell/korn-shell-variables)

_**__**_

_**_Variables are set with the_**_ ** _=_** _ ** _operator as in Bourne shell. No space is allowed around the_**_ _ **= _operator. Variables may have attributes assigned by_**_ ** _typeset_** _ ** _with the following syntax:_**_

  
_**__**_ **Korn Shell** ** _typeset_ syntax**  
---  
_typeset -attrib(s) variable=[value]_ |  assign attribute and optional value  
_typeset +attrib(s) variable_ |  remove attribute  
_typeset_ |  list all vars and attributes  
_typeset -attrib_ |  list all vars with _-attrib_ type  
_typeset +attrib_ |  list only vars with _+attrib_ type  
List of _typeset_ Supported Attributes  
_-f_ |  the name refers to a function  
_-H_ |  system to hostname file mapping  
_-i_ |  integer  
_-l_ |  lower case  
_-L_ |  left justify, remove leading spaces  
_-LZ_ |  left justify, remove leading zeroes  
_-r_ |  read only (cannot be removed)  
_-R_ |  right justify  
_-RZ_ |  right justify with leading zeroes  
_-t_ |  tag named parameter  
_-u_ |  upper case  
_-x_ |  export  
 _ ** __**_

  
_**_  
Any variable can be assigned the output of a command or of a file with the syntax:_**_

  
_**__**_ _var=$(command)_ |  Korn specific  
---|---  
_var=`command`_ |  Bourne compatible  
_var=$(_`<` _file)_ |  Korn specific  
_var=`cat file`_ |  Bourne compatible  
 _ ** __**_

  
_**_  
Variables are removed by the_**_ ** _unset_** _ ** _builtin. To define a variable that executes a script file using_**_ ** _Ksh_** _ ** _syntax, do the following:_**_

_**__**_
    
    
    > ksh
    $ cv=$(<kls)
    $ echo $cv
    ls -al
    $
    $ $cv
    total 5
    drwxr-xr-x   3 john     users       8192 Mar 10 10:48 .
    drwxr-x--x  17 john     users       8192 Mar  9 16:05 ..
    -rw-r--r--   1 john     users        299 Mar  9 11:25 a.a
    -rwxr-xr-x   1 john     users        261 Mar 10 08:44 cread
    -rw-r--r--   1 john     users         37 Jun 18  1998 er

 _ ** __**_ ** _Ksh_** _ ** _Special variables are:_**_

  
_**__**_ **Korn Shell Special Variables**  
---  
_#_ |  number of positional parameters  
_?_ |  exit status  
_$_ |  process _ID_  
_-_ (dash) |  current options  
`_` (underscore) | the last argument of the previous command  
_!_ |  process _ID_ of last background  
_ERRNO_ |  error no. of last failed system call  
_LINENO_ |  the line no. of the current script line in execution  
_OLDPWD_ |  previous _cd_ directory  
_OPTARG_ |  last option processed by _getopts_  
_OPTIND_ |  index of last option processed by _getopts_  
_PPID_ |  parent `PID`  
_PWD_ |  current directory  
_RANDOM_ |  random funcion  
_REPLY_ |  menu item no. in response to _select Ksh_ command  
_SECONDS_ |  seconds since shell invocation  
_CDPATH_ |  search path for _cd_ command  
_COLUMNS_ |  edit window width  
_EDITOR_ |  editor management  
_ENV_ |  generate path name in tracked alias and functions  
_FCEDIT_ |  default editor for history processing command _fc_  
_FPATH_ |  search path for functions  
_IFS_ |  internal field separator  
_HISTFILE_ |  store command history file  
_HISTSIZE_ |  history buffer size  
_HOME_ |  home directory  
_LANG_ |  system locale  
_LC_COLLATE_ |  collating sequence  
_LC_CTYPE_ |  character classification  
_LC_MESSAGES_ |  language for system messages  
_LC_MONETARY_ |  monetary format  
_LC_NUMERIC_ |  numeric format  
_LC_TIME_ |  date and time format  
_LINES_ |  column length  
_LOGNAME_ |  login name  
_MAIL_ |  mail notify  
_MAILCHECK_ |  mail notify interval  
_MAILPATH_ |  mail notify  
_NLSPATH_ |  search path for messages  
_PATH_ |  searc path for commands  
_PS1_ |  primary promt  
_PS2_ |  secondary prompt  
_PS3_ |  selection prompt (default `#?`)  
_PS4_ |  trace prompt (default +)  
_SHELL_ |  shell in use  
_TMOUT_ |  command timeout to terminate shell  
_VISUAL_ |  editor option  
 _ ** __**_

  
_**_  
Variables are protected by braces:_**_

_**__**_
    
    
    $ print Current options/ERRNO: ${-}, $ERRNO
    Current options/ERRNO: ism, 10

 _ ** _Metacharacters are printed when prefixed by`\`. _**_

  
_**__**_ **Korn Shell Variable Usage and Setting Rules**  
---  
_varlen=${#var}_ |  variable length  
_var=${var1:-value}_ | _var=var1_ if _var1_ set, _var=value_ if _var1.not.set_ or empty  
_var=${var1-value}_ | _var=var1_ if _var1_ set, _var=value_ only if _var1.not.set_  
_var=${var1:=var2}_ | _var=$var1_ if _var1_ set and not empty, else _= $var2_  
_var=${var1=var2}_ | _var=$var1_ if _var1_ set even if empty, else _= $var2_  
_var=${var1:+var2}_ | _var=$var2_ if _var1_ set and not empty, else _var not set_  
_var=${var1:+var2}_ | _var=$var2_ if _var1_ set even if empty, else _var not set_  
_var=${var1#var2}_ | _var=var1_ with smallest part of left matched _var2_ deleted  
_var=${var1##var2}_ | _var=var1_ with largest part of left matched _var2_ deleted  
_var=${var1%var2}_ | _var=var1_ with smallest part of right matched _var2_ deleted  
_var=${var1%%var2}_ | _var=var1_ with largest part of right matched _var2_ deleted  
_var=${var1:?}_ | _var=var1_ if _var1_ set else _error message_  
_var=${var1:?var2}_ | _var=var1_ if _var1_ set else _var=var2_ and _exit_  
 _ ** __**_

_**_Korn shell can handle arrays as_**_ ** _C_** _ ** _shell but with a different syntax._**_

  
_**__**_ **Korn Shell Array Syntax**  
---  
`arr[0]=val0 arr[1]=val1 ...` |  init array in any order  
`set -A arr val0 val1 ...` | alternate init for ordered array  
`typeset arr[0]=val0 arr[1]=val1 ...` | alternate init array in any order  
`${arr}, $arr` | array element zero  
`${arr[n]}` | array element _n_  
`${arr[n+2]` |  array element _n+2_  
`${arr[$i]}` |  array element _$i_  
`${arr[*]}, ${arr[@]}` |  all elements of array  
`${#arr[*]}, ${#arr[@]}` | number of array elements  
`${#arr[n]}` | length of array element _n_  
 _ ** __**_

  
_**_  
Example of array usage:_**_

_**__**_
    
    
    #!/bin/ksh
    #-----------karray: arrays with Korn shell
    #
    echo Proc $0: arrays in Korn shell
    echo
    set -A rgb red green blue yellow magenta cyan
    print rgb is a ${#rgb[*]} items color array with values:
    print ${rgb[*]}
    print 4-th item is ${rgb[1+3]} ${#rgb[4]}-bytes long
    #
    #----------end script------------------

 _ ** _The_**_ ** _set +A_** _ ** _statement allows partial redefinition of ordered array elements. Consider the following:_**_
    
    
    $ set -A rgb red green blue yellow magenta cyan
    $ print ${rgb[*]}
    red green blue yellow magenta cyan
    

_**_If you use_**_ ** _-A_** _ ** _to change only the first item of array_**_ ** _rgb_** _ ** _, the array is truncated. If you use_**_ ** _+A_** _ ** _, the first items are changed keeping the remaining ones:_**_
    
    
    $ set -A rgb red green blue
    $ print ${rgb[*]}
    red green blue
    $ set -A rgb red green blue yellow magenta cyan
    $ set +A rgb rosso
    $ print ${rgb[*]}
    rosso green blue yellow magenta cyan
    

_**__**_

_**_In Korn shell quotes have the same usage as in Bourne shell._**_

_**__**_

`_single quotes_ `'` hide meaning of special characters, do not perform variable substitution within quoted string 

_double quotes_ `"` preserve embedded spaces and newlines, set _vars_ to 

  
_NULL_ , display single quotes, perform variable substitution   
_back quotes_ ``` assign command output to vars `

`<http://www.bo.infn.it/alice/alice-doc/mll-doc/impgde/node16.html>`

