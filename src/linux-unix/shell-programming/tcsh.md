# [TCSH programming](http://faculty.plattsburgh.edu/jan.plaza/computing/help/tcsh.htm)

There is almost no difference between syntax of csh and tcsh statements which are useful in scripts; the two shells differ mostly in the interactive features (such as capabilities of command completion). There are Unix systems which contain csh but not tcsh. Every Unix system which contains tcsh, either also contains csh, or csh could be added to it just by creating a symbolic link called csh which points to tcsh. Tcsh is an extension of csh, compatible with csh. (When tcsh is invoked through a link called csh, the tcsh notices this fact and assumes the exact behavior of csh.???) For these reasons most programmers write just csh scripts, not tcsh scripts.

The first line of every csh script should contain #!/bin/csh or #!/bin/csh -f , preceded by no spaces or tabs. This is more than just a comment -- this line tells the system how to call the interpreter which will execute the script. The -f option causes that the csh which executes the script does not read (ANY OR USER'S ???) initialization files.

**Debugging** The following statements, individually or together, are useful during the development of the script:set echoset verbose

When the script is executed, they will cause that a trace of execution will be printed on the screen.

 **Shell variables.** By convention names of shell variables are not capitalized.set VARNAME = VALUEset aa = Helloset bb = 'Hello world'set aa = "$aa my friend"set outputFile = ~/csc319/out.txtset user1 = abcd1234set nn = 345set ee unset bb

Remember to put spaces around the = symbol.

 **Shell list (array) variables**.There are only lists of strings; there are no lists of lists.set users = ($user1 bcde2345)set users = (root $users cdef3456)

set $users[0] = defg4567

 **Command line parameters** $0 -- the name through which the script was invoked$1, $2, ..., $9 -- the first, second, ..., ninth parameter with which the script was invoked.$* -- the list of all command line parameters, (excluding the name of the script).$#argv -- the number of command line parameters. It is useful to use :q operation, in case if the parameters escaped contained white space.If the user of a script wants to specify a parameter string which contains white space, every white space character must be preceded by \\. If the user typed myscript fff\ ggg, in the script the following values would be received:$1 would have value fff$2 would have value ggg$* would have value (fff ggg)$1:q would have value 'fff ggg'

$*:q would have value ('fff ggg')

 **Input
** Every time user presses Enter, special variable $< is updated to store one line of users input; the line break is not a part if the string in $<.
WHAT IF USER TYPES CTRL-D ?

 **Output** echo 'echo "cc = $cc" -- echo adds a line break after the string.echo "$bb\n $cc" -- Use \n to specify an additional line break.echo -n "$aa $bb $cc" -- With -n, echo will not add a line break.echo $aa > $outputFileecho $cc >> $outputFile

echo "$nn+$nn" -- addition not performed.

cat << ENDLABEL -- this outputs all the text up to but excluding ENDLABEL. ... You can use MESSAGE1_END, etc as the end label. ... This feature is called a "here document"ENDLABEL

**String operations
**

There is no concatenation operator. To concatenate strings, put them one next to the other.set newstring = aaa$string1${string2}bbb

Notice that curly braces can be used to delimit the variable name (so that the shell does not think the variable name is string2bbb.)

set myfile = /usr/users/abcd1234/sorter.cset head = $myfile:h -- gets value /usr/users/abcd1234set tail = $myfile:t -- gets value sorter.c set root = $myfile:r -- gets value /usr/users/abcd1234/sorter

set extension = $myfile:e -- gets value c

**Boolean expressions**

$?VARIABLE -- test if VARIABLE is defined

== -- test if two strings are equal!= -- test if two strings are diferent=~ -- test if the string on the left matches the string pattern on the right (the expression can can contain *, meaning "any string ofs characters, of length 0 or more")

!~ --test if the string on the left does not match the string pattern on the right

-e $file -- test if $file exists-d $file -- test if $file exists and is a directory-f $file -- test if $file exists and is a regular file-r $file -- test if $file exists and is readable by the current process-w $file -- test if $file exists and is writable by the current process-x $file -- test if $file exists and is executable by the current processBoolean expressions can be combined using && (conjunction), || (disjunction) and ! (negation).

 **Arithmetic operations**

set aa = 2+2 -- variable aa gets value '2+2'@ aa = 2+2 -- variable aa gets value 4@ a++ -- now, aa has value 5.

Arbitrary arithmetic expressions with +, -, *, /, ++, -- are allowed.

 **One line conditional statement** if (BOOLEAN-EXPESSION) COMMANDif (-r comments.txt) cat comments.txt >> summary.txtNotice that there are no words "then" or "end".

Notice that the statement must be on a the same line (unless line breaks are escaped).

 **If-then-else statement**

if (EXPR1) then ... ...else if (EXPR2) then ... ...else ... ...endifThere can be any number else-if parts.

Else-if and else parts are optional.

 **Switch-case statement**

switch (EXPR) case STRINGPATTERN1: ... ... breaksw case STRINGPATTERN2: case STRINGPATTERN3: ... ... breaksw default: ... ...

endsw

 **Foreach loop** foreach VARNAME LIST ... ...

end

For instance:foreach user ($users) grep $user /etc/passwd

end

foreach file (csc*) if (! -d $file) chmod o-r $file

end

 **While loop**

while (EXPR) ... ...

end

 **Other features**

If you use a file pattern with a wildcard (e.g. csc*), the pattern will expand to a list of files whose names match the pattern.

There are no functions, procedures, methods, subroutines in csh or tcsh. Instead, one can use aliases with parameters and goto statements.

To obtain output of a command for processing in the script, enclose the command in backquotes:
set fileInfo = `ls -l project.java`

<http://faculty.plattsburgh.edu/jan.plaza/computing/help/tcsh.htm>

<http://en.wikipedia.org/wiki/C_shell#Command_substitution>
