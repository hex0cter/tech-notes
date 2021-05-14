# [Bash options](http://tldp.org/LDP/abs/html/options.html)


Options are settings that change shell and/or script behavior.

The [set](http://tldp.org/LDP/abs/html/internal.html#SETREF) command enables options within a script. At the point in the script where you want the options to take effect, use **set -o option-name** or, in short form, **set -option-abbrev**. These two forms are equivalent.

|


          #!/bin/bash

          set -o verbose
          # Echoes all commands before executing.


---


          #!/bin/bash

          set -v
          # Exact same effect as above.



![Note](http://tldp.org/LDP/abs/images/note.gif) To _disable_ an option within a script, use **set +o option-name** or **set +option-abbrev**.


          #!/bin/bash

          set -o verbose
          # Command echoing on.
          command
          ...
          command

          set +o verbose
          # Command echoing off.
          command
          # Not echoed.


          set -v
          # Command echoing on.
          command
          ...
          command

          set +v
          # Command echoing off.
          command

          exit 0


---

An alternate method of enabling options in a script is to specify them immediately following the `_#!_` script header.


          #!/bin/bash -x
          #
          # Body of script follows.


---

It is also possible to enable script options from the command line. Some options that will not work with **set** are available this way. Among these are `_-i_` , force script to run interactive.

` **bash -v script-name**`

` **bash -o verbose script-name**`

The following is a listing of some useful options. They may be specified in either abbreviated form (preceded by a single dash) or by complete name (preceded by a _double_ dash or by ` -o`).

 **Table 33-1. Bash options**

Abbreviation| Name| Effect
---|---|---
`-B`| brace expansion|  _Enable_ [brace expansion](http://tldp.org/LDP/abs/html/special-chars.html#BRACEEXPREF) (default setting = _on_ )
`+B`| brace expansion|  _Disable_ brace expansion
` -C`| noclobber| Prevent overwriting of files by redirection (may be overridden by >|)
`-D`| (none)| List double-quoted strings prefixed by $, but do not execute commands in script
`-a`| allexport| Export all defined variables
`-b`| notify| Notify when jobs running in background terminate (not of much use in a script)
`-c ...`| (none)| Read commands from **...**
` checkjobs`|  | Informs user of any open [jobs](http://tldp.org/LDP/abs/html/x9644.html#JOBSREF) upon shell exit. Introduced in [version 4](http://tldp.org/LDP/abs/html/bashver4.html#BASH4REF) of Bash, and still "experimental." _Usage:_ shopt -s checkjobs ( _Caution:_ may hang!)
` -e`| errexit| Abort script at first error, when a command exits with non-zero status (except in [until](http://tldp.org/LDP/abs/html/loops1.html#UNTILLOOPREF) or [while loops](http://tldp.org/LDP/abs/html/loops1.html#WHILELOOPREF), [if-tests](http://tldp.org/LDP/abs/html/testconstructs.html#TESTCONSTRUCTS1), [list constructs](http://tldp.org/LDP/abs/html/list-cons.html#LCONS1))
`-f`| noglob| Filename expansion (globbing) disabled
`globstar`| [ _globbing_ star-match](http://tldp.org/LDP/abs/html/bashver4.html#GLOBSTARREF)|  Enables the ** [globbing](http://tldp.org/LDP/abs/html/globbingref.html) operator ([version 4+](http://tldp.org/LDP/abs/html/bashver4.html#BASH4REF) of Bash). _Usage:_ shopt -s globstar
` -i`| interactive| Script runs in _interactive_ mode
` -n`| noexec| Read commands in script, but do not execute them (syntax check)
`-o Option-Name`| (none)| Invoke the _Option-Name_ option
` -o posix`| POSIX| Change the behavior of Bash, or invoked script, to conform to [POSIX](http://tldp.org/LDP/abs/html/sha-bang.html#POSIX2REF) standard.
`-o pipefail`| pipe failure| Causes a pipeline to return the [exit status](http://tldp.org/LDP/abs/html/exit-status.html#EXITSTATUSREF) of the last command in the pipe that returned a non-zero return value.
`-p`| privileged| Script runs as "suid" (caution!)
`-r`| restricted| Script runs in _restricted_ mode (see [Chapter 22](http://tldp.org/LDP/abs/html/restricted-sh.html)).
` -s`| stdin| Read commands from `stdin`
`-t`| (none)| Exit after first command
`-u`| nounset| Attempt to use undefined variable outputs error message, and forces an exit
`-v`| verbose| Print each command to `stdout` before executing it
`-x`| xtrace| Similar to `-v`, but expands commands
`-`| (none)| End of options flag. All other arguments are [positional parameters](http://tldp.org/LDP/abs/html/internalvariables.html#POSPARAMREF).
`--`| (none)| Unset positional parameters. If arguments given (` _-- arg1 arg2_` ), positional parameters set to arguments.
