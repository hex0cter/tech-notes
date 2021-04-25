
date: None  
author(s): None  

# [Conditions in bash scripting (if statements) - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/bash-tips/conditions-in-bash-scripting-if-statements)

If you use bash for scripting you will undoubtedly have to use conditions a lot, for example for an _if ... then_ construct or a _while_ loop. The syntax of these conditions can seem a bit daunting to learn and use. This tutorial aims to help the reader understanding conditions in bash, and provides a comprehensive list of the possibilities. A small amount of general shell knowledge is assumed.

Difficulty: _**Basic - Medium**_

## Introduction

Bash features a lot of built-in checks and comparisons, coming in quite handy in many situations. You've probably seen if statements like the following before:

> if [ $foo -ge 3 ]; then

The condition in this example is essentially a command. It may sound strange, but surrounding a comparison with square brackets is the same as using the built-in test command, like this:

> if test $foo -ge 3; then

If $foo is **G** reater then or **E** qual to 3, the block after 'then' will be executed. If you always wondered why bash tends to use -ge or -eq instead of >= or ==, it's because this condition type originates from a command, where -ge and -eq are options.  
And that's what _if_ does essentially, checking the exit status of a command. I'll explain that in more detail further in the tutorial.There also are built-in checks that are more specific to shells. What

about this one?

> if [ -f regularfile ]; then

The above condition is true if the file 'regularfile' exists _and_ is a regular file. A regular file means that it's not a block orcharacter device, or a directory. This way, you can make sure a usablefile exists before doing something with it. You can even check if a

file is readable!

> if [ -r readablefile]; then

The above condition is true if the file 'readablefile' exists _and_ is readable. Easy, isn't it?

## The syntax of an if statement (a short explanation)

The basic syntax of an _if ... then_ statement is like this:

> if _<condition>_ ; then  
>  _<commands>_  
>  fi

The condition is, depending on its type, surrounded by certainbrackets, eg. [ ]. You can read about the different types further on

in the tutorial. You can add commands to be executed when the condition is false using the _else_ keyword, and use the _elif_ (elseif) keyword to execute commands on another condition if the primary condition is false. The _else_ keyword always comes last. Example:

> if [ -r somefile ]; thencontent=$(cat somefile)elif [ -f somefile ]; thenecho "The file 'somefile' exists but is not readable to the script."elseecho "The file 'somefile' does not exist."
> 
> fi

A short explanation of the example: first we check if the file somefile is readable ("if [ -r somefile ]"). If so, we read it into a variable. If not, we check if it actually exists ("elif [ -f somefile ]"). If that's true, we report that it exists but isn't readable (if it was, we would have read the content). If the file doesn't exist, we report so, too. The condition at _elif_ is only executed if the condition at _if_ was false. The commands belonging to _else_ are only executed if both conditions are false.

## The basic rules of conditions

When you start writing and using your own conditions, there are some rules you should know to prevent getting errors that are hard to trace. Here follow three important ones:

  1.  **Always keep spaces between the brackets and the actual check/comparison**. The following won't work:  


> if [$foo -ge 3]; then

Bash will complain about a "missing `]'".

  2.  **Always terminate the line before putting a new keyword like "then"**. The words _if_ , _then_ , _else_ , _elif_ and _fi_ are shell keywords, meaning that they cannot share the same line. Put a ";" between the previous statement and the keyword or place the keyword on the start of a new line. Bash will throw errors like "syntax error near unexpected token `fi'" if you don't.
  3.  _It is a good habit to quote string variables if you use them in conditions_ , because otherwise they are likely to give trouble if they contain  
spaces and/or newlines. By quoting I mean:

> if [ "$stringvar" == "tux" ]; then

There are a few cases in which you should not  
quote, but they are rare. You will see one of them further on in the tutorial.




Also, there are two things that may be useful to know:

  1.  _You can invert a condition_ by putting an "!" in front of it. Example:  


> if [ ! -f regularfile ]; then

Be sure to place the "!" inside the brackets!

  2.  _You can combine conditions_ by using certain operators. For the single-bracket syntax that we've been using so far, you can use "-a" for _and_ and "-o" for _or_. Example:  


> if [ $foo -ge 3 -a $foo -lt 10 ]; then

The above condition will return true if $foo contains an integer greater than or equal to 3 and **L** ess **T** han 10. You can read more about these combining expressions at the respective condition syntaxes.




And, one more basic thing: don't forget that conditions can also be used in other statements, like _while_ and _until_. It is outside the scope of this tutorial to explain those, but you can read about them at the [Bash Guide for Beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_02.html).

Anyway, I've only shown you conditions between single brackets so far. There are more syntaxes, however, as you will read in the next section.

## Different condition syntaxes

Bash features different syntaxes for conditions. I will list the three of them:

### 1\. Single-bracket syntax

This is the condition syntax you have already seen in the previous paragraphs; it's the oldest supported syntax. It supports three types of conditions:

  *  **File-based conditions**
    * Allows different kinds of checks on a file. Example:  


> if [ -L symboliclink ]; then

The above condition is true if the file 'symboliclink' exists and is a symbolic link. For more file-based conditions see [the table](http://www.linuxtutorialblog.com/post/tutorial-conditions-in-bash-scripting-if-statements#file-based-conditions) below.

  *  **String-based conditions**
    * Allows checks on a string and comparing of strings. Example one:  


> if [ -z "$emptystring" ]; then

The above condition is true if $emptystring is an empty string or an uninitialized variable. Example two:

> if [ "$stringvar1" == "cheese" ]; then

The above condition is true if $stringvar1 contains just the string "cheese". For more string-based conditions see [the table](http://www.linuxtutorialblog.com/post/tutorial-conditions-in-bash-scripting-if-statements#string-based-conditions) below.

  *  **Arithmetic (number-based) conditions**
    * Allows comparing integer numbers. Example:  


> if [ $num -lt 1 ]; then

The above condition returns true if $num is less than 1. For more arithmetic conditions see [the table](http://www.linuxtutorialblog.com/post/tutorial-conditions-in-bash-scripting-if-statements#arithmetic-conditions) below.




### 2\. Double-bracket syntax

You may have encountered conditions enclosed in double square brackets already, which look like this:

> if [[ "$stringvar" == *string* ]]; then

The double-bracket syntax serves as an enhanced version of the single-bracket syntax; it mainly has the same features, but also some important differences with it. I will list them here:

  *  _The first difference_ can be seen in the above example; when comparing strings, the double-bracket syntax features shell globbing. This means that an asterisk ("*") will expand to literally anything, just as you probably know from normal command-line usage. Therefore, if $stringvar contains the phrase "string" anywhere, the condition will return true. Other forms of shell globbing are allowed, too. If you'd like to match both "String" and "string", you could use the following syntax:  


> if [[ "$stringvar" == *[sS]tring* ]]; then

Note that only general shell globbing is allowed. Bash-specific things like {1..4} or {foo,bar} will not work. Also note that the **globbing will not work if you quote the right string**. In this case you should leave it unquoted.

  *  _The second difference_ is that word splitting is prevented. Therefore, you could omit placing quotes around string variables and use a condition like the following without problems:  


> if [[ $stringvarwithspaces != foo ]]; then

Nevertheless, the quoting string variables remains a good habit, so I recommend just to keep doing it.

  *  _The third difference_ consists of not expanding filenames. I will illustrate this difference using two examples, starting with the old single-bracket situation:  


> if [ -a *.sh ]; then

The above condition will return true if there is one single file in the working directory that has a .sh extension. If there are none, it will return false. If there are several .sh files, bash will throw an error and stop executing the script. This is because *.sh is expanded to the files in the working directory. Using double brackets prevents this:

> if [[ -a *.sh ]]; then

The above condition will return true only if there is a file in the working directory called "*.sh", no matter what other .sh files exist. The asterisk is taken literally, because the double-bracket syntax does not expand filenames.

  *  _The fourth difference_ is the addition of more generally known combining expressions, or, more specific, the operators "&&" and "||". Example:  


> if [[ $num -eq 3 && "$stringvar" == foo ]]; then

The above condition returns true if $num is equal to 3 and $stringvar is equal to "foo". The -a and -o known from the single-bracket syntax is supported, too.

Note that the _and_ operator has precedence over the _or_ operator, meaning that "&&" or "-a" will be evaluated before "||" or "-o".

  *  _The fifth difference_ is that the double-bracket syntax allows regex pattern matching using the "=~" operator. See [the table](http://www.linuxtutorialblog.com/post/tutorial-conditions-in-bash-scripting-if-statements#string-based-conditions) for more information.



### 3\. Double-parenthesis syntax

There also is another syntax for arithmetic (number-based) conditions, most likely adopted from the Korn shell:

> if (( $num <= 5 )); then

The above condition is true if $num is less than or equal to 5. This syntax may seem more familiar to programmers. It features all the 'normal' operators, like "==", "<" and ">=". It supports the "&&" and "||" combining expressions (but not the -a and -o ones!). It is equivalent to the built-in let command.

## Table of conditions

The following table list the condition possibilities for both the single- and the double-bracket syntax. Save a single exception, the examples are given in single-bracket syntax, but are always compatible with double brackets.  
  
---  
Condition| True if| Example/explanation  
[ -a existingfile ]| file 'existingfile' exists.| if [ -a tmp.tmp ]; then  
rm -f tmp.tmp # _Make sure we're not bothered by an old temporary file  
_ fi  
[ -b blockspecialfile ]| file 'blockspecialfile' exists and is block special.| Block special files are special kernel files found in /dev, mainly used for ATA devices like hard disks, cd-roms and floppy disks.

if [ -b /dev/fd0 ]; then  
dd if=floppy.img of=/dev/fd0 # _Write an image to a floppy_  
fi  
  
[ -c characterspecialfile ]| file 'characterspecialfile' exists and is character special.| Character special files are special kernel files found in /dev, used for all kinds of purposes (audio hardware, tty's, but also /dev/null).

if [ -c /dev/dsp ]; then  
cat raw.wav > /dev/dsp # _This actually works for certain raw wav files_  
fi  
  
[ -d directory ]| file 'directory' exists and is a directory.| In UNIX-style, directories are a special kind of file.

if [ -d ~/.kde ]; then echo "You seem to be a kde user."

fi  
  
[ -e existingfile ]| file 'existingfile' exists.| (same as -a, see that entry for an example)  
[ -f regularfile ]| file 'regularfile' exists and is a regular file.| A regular file is neither a block or character special file nor a directory.

if [ -f ~/.bashrc ]; then source ~/.bashrc

fi  
  
[ -g sgidfile ]| file 'sgidfile' exists and is set-group-ID.| When the SGID-bit is set on a directory, all files created in that directory will inherit the group of the directory.

if [ -g . ]; then echo "Created files are inheriting the group '$(ls -ld . | awk '{ print $4 }')' from the working directory."

fi  
  
[ -G fileownedbyeffectivegroup ]| file 'fileownedbyeffectivegroup' exists and is owned by the effective group ID.| The effective group id is the primary group id of the executing user.

if [ ! -G file ]; then # _An exclamation mark inverts the outcome of the condition following it_  
chgrp $(id -g) file # _Change the group if it's not the effective one_  
fi  
  
[ -h symboliclink ]| file 'symboliclink' exists and is a symbolic link.| if [ -h $pathtofile ]; then  
pathtofile=$(readlink -e $pathtofile) # _Make sure $pathtofile contains the actual file and not a symlink to it_  
fi  
[ -k stickyfile ]| file 'stickyfile' exists and has its sticky bit set.| The sticky bit has got [quite a history](http://en.wikipedia.org/wiki/Sticky_bit), but is now used to prevent world-writable directories from having their contents deletable by anyone.

if [ ! -k /tmp ]; then # _An exclamation mark inverts the outcome of the condition following it_ echo "Warning! Anyone can delete and/or rename your files in /tmp!"

fi  
  
[ -L symboliclink ]| file 'symboliclink' exists and is a symbolic link.| (same as -h, see that entry for an example)  
[ -N modifiedsincelastread ]| file 'modifiedsincelastread' exists and was modified after the last read.| if [ -N /etc/crontab ]; then  
killall -HUP crond # _SIGHUP makes crond reread all crontabs  
_ fi  
[ -O fileownedbyeffectiveuser ]| file 'fileownedbyeffectiveuser' exists and is owned by the user executing the script.| if [ -O file ]; then  
chmod 600 file # _Makes the file private, which is a bad idea if you don't own it_  
fi  
[ -p namedpipe ]| file 'namedpipe' exists and is a named pipe.| A named pipe is a file in /dev/fd/ that can be read just once. See [my bash tutorial](http://www.linuxtutorialblog.com/post/tutorial-the-best-tips-tricks-for-bash#using-several-ways-of-substitution) for a case in which it's used.

if [ -p $file ]; then  
cp $file tmp.tmp # _Make sure we'll be able to read_  
file="tmp.tmp" # _the file as many times as we like_  
fi  
  
[ -r readablefile ]| file 'readablefile' exists and is readable to the script.| if [-r file ]; then  
content=$(cat file) # _Set $content to the content of the file  
_ fi  
[ -s nonemptyfile ]| file 'nonemptyfile' exists and has a size of more than 0 bytes.| if [ -s logfile ]; then  
gzip logfile # _Backup the old logfile_  
touch logfile # _before creating a fresh one._  
fi  
[ -S socket ]| file 'socket' exists and is a socket.| A socket file is used for inter-process communication, and features an interface similar to a network connection.

if [ -S /var/lib/mysql/mysql.sock ]; then  
mysql --socket=/var/lib/mysql/mysql.sock # _See[this MySQL tip](http://www.tech-recipes.com/mysql_tips762.html)  
_ fi  
  
[ -t openterminal ]| file descriptor 'openterminal' exists and refers to an open terminal.| Virtually everything is done using files on Linux/UNIX, and the terminal is no exception.

if [ -t /dev/pts/3 ]; then  
echo -e "\nHello there. Message from terminal $(tty) to you." > /dev/pts/3 # _Anyone using that terminal will actually see this message!_  
fi  
  
[ -u suidfile ]| file 'suidfile' exists and is set-user-ID.| Setting the suid-bit on a file causes execution of that file to be done with the credentials of the owner of the file, not of the executing user.

if [ -u executable ]; then echo "Running program executable as user $(ls -l executable | awk '{ print $3 }')."

fi  
  
[ -w writeablefile ]| file 'writeablefile' exists and is writeable to the script.| if [ -w /dev/hda ]; then grub-install /dev/hda

fi  
  
[ -x executablefile ]| file 'executablefile' exists and is executable for the script.| Note that the execute permission on a directory means that it's searchable (you can see which files it contains).

if [ -x /root ]; then echo "You can view the contents of the /root directory."

fi  
  
[ newerfile -nt olderfile ]| file 'newerfile' was changed more recently than 'olderfile', or if 'newerfile' exists and 'olderfile' doesn't.| if [ story.txt1 -nt story.txt ]; then echo "story.txt1 is newer than story.txt; I suggest continuing with the former."

fi  
  
[ olderfile -ot newerfile ]| file 'olderfile' was changed longer ago than 'newerfile', or if 'newerfile' exists and 'olderfile' doesn't.| if [ /mnt/remote/remotefile -ot localfile ]; then  
cp -f localfile /mnt/remote/remotefile # _Make sure the remote location has the newest version of the file, too_  
fi  
[ same -ef file ]| file 'same' and file 'file' refer to the same device/inode number.| if [ /dev/cdrom -ef /dev/dvd ]; then echo "Your primary cd drive appears to read dvd's, too."

fi  
  
Condition| True if| Example/explanation  
[ STRING1 == STRING2 ]| STRING1 is equal to STRING2.| if [ "$1" == "moo" ]; then  
echo $cow # _Ever tried executing 'apt-get moo'?  
_ fi

Note: you can also use a single "=" instead of a double one.  
  
[ STRING1 != STRING2 ]| STRING1 is not equal to STRING2.| if [ "$userinput" != "$password" ]; then echo "Access denied! Wrong password!"

exit 1 # _Stops script execution right here_

  
fi  
[ STRING1 \> STRING2 ]| STRING1 sorts after STRING2 in the current locale (lexographically).| The backslash before the angle bracket is there because the bracket needs to be escaped to be interpreted correctly. As an example we have a basic [bubble sort](http://en.wikipedia.org/wiki/Sorting_algorithm#Bubble_sort):

 _(Don't feel ashamed if you don't understand this, it is a more complex example)_ array=( linux tutorial blog )swaps=1while (( swaps > 0 )); do swaps=0 for (( i=0; i < (( ${#array[@]} - 1 )) ; i++ )); do

if [ "${array[$i]}" \> "${array[$(( i + 1 ))]}" ]; then # _Here is the sorting condition_

tempstring=${array[$i]} array[$i]=${array[$(( i + 1 ))]} array[$(( i + 1 ))]=$tempstring (( swaps=swaps + 1 )) fi donedone

echo ${array[@]} # _Returns "blog linux tutorial"_  
  
[ STRING1 \< STRING2 ]| STRING1 sorts before STRING2 in the current locale (lexographically).  
[ -n NONEMPTYSTRING ]| NONEMPTYSTRING has a length of more than zero.| This condition only accepts valid strings, so be sure to quote anything you give to it.

if [ -n "$userinput" ]; then  
userinput=parse($userinput) # _Only parse if the user actually gave some input._  
fi

Note that you can also omit the "-n", as brackets with just a string in it behave the same.  
  
[ -z EMPTYSTRING ]| EMPTYSTRING is an empty string.| This condition also accepts non-string input, like an uninitialized variable:

if [ -z $uninitializedvar ]; then  
uninitializedvar="initialized" # _-z returns true on an uninitialized variable, so we initialize it here._  
fi  
  
 _Double-bracket syntax only:  
_ [[ STRING1 =~ REGEXPATTERN ]]| STRING1 matches REGEXPATTERN.| If you are familiar with Regular Expressions, you can use this conditions to perform a regex match.

if [[ "$email" =~ "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}\b" ]]; then echo "\$email contains a valid e-mail address."

fi  
  
Condition| True if| Example/explanation  
[ NUM1 -eq NUM2 ]| NUM1 is **EQ** ual to NUM2.| These conditions only accept integer numbers. Strings will be converted to integer numbers, if possible. Some random examples:

if [ $? -eq 0 ]; then # _$? returns the exit status of the previous command_ echo "Previous command ran succesfully."

fi

if [ $(ps -p $pid -o ni=) -ne $(nice) ]; then echo "Process $pid is running with a non-default nice value"

fi

if [ $num -lt 0 ]; then echo "Negative numbers not allowed; exiting..." exit 1

fi  
  
[ NUM1 -ne NUM2 ]| NUM1 is **N** ot **E** qual to NUM2.  
[ NUM1 -gt NUM2 ]| NUM1 is **G** reater **T** han NUM2.  
[ NUM1 -ge NUM2 ]| NUM1 is **G** reater than or **E** qual to NUM2.  
[ NUM1 -lt NUM2 ]| NUM1 is **L** ess **T** han NUM2.  
[ NUM1 -le NUM2 ]| NUM1 is **L** ess than or **E** qual to NUM2.  
Condition| True if| Example/explanation  
[ -o shelloption ]| shell option 'shelloption' is enabled.| Shell options modify the behaviour of bash, except a few unmodifiable ones that indicate the shell status.

if [ ! -o checkwinsize ] # _An exclamation mark inverts the outcome of the condition following it_ echo "Shell option checkwinsize is disabled; enabling it so you can resize you terminal window without problems."

shopt -s checkwinsize # _This shell option is modifiable_

  
fi

if [ -o login_shell ]; then  
echo "This a a login shell." # _This shell option is not modifiable  
_  
fi  
  
With the double-parenthesis syntax, you can use the following conditions:  
  
---  
Condition| True if| Example/explanation  
(( NUM1 == NUM2 ))| NUM1 is equal to NUM2.| These conditions only accept integer numbers. Strings will be converted to integer numbers, if possible. Some random examples:

if (( $? == 0 )); then # _$? returns the exit status of the previous command_ echo "Previous command ran succesfully."

fi

if (( $(ps -p $pid -o ni=) != $(nice) )); then echo "Process $pid is running with a non-default nice value"

fi

if (( $num < 0 )); then echo "Negative numbers not allowed; exiting..." exit 1

fi  
  
(( NUM1 != NUM2 ))| NUM1 is not equal to NUM2.  
(( NUM1 > NUM2 ))| NUM1 is greater than NUM2.  
(( NUM1 >= NUM2 ))| NUM1 is greater than or equal to NUM2.  
(( NUM1 < NUM2 ))| NUM1 is less than NUM2.  
(( NUM1 <= NUM2 ))| NUM1 is less than or equal to NUM2.  
  
After this dry information load, here's a bit of explanation for those who want to know more...

## Diving a little deeper

I said I'd tell more about the fact that _if_ essentially checks the exit status of commands. And so I will. The basic rule of bash when it comes to conditions is _0 equals true, >0 equals false_.  
That's pretty much the opposite of many programming languages where 0 equals false and 1 (or more) equals true. The reason behind this is that shells like bash deal with programs a lot. By UNIX convention, programs use an exit status for indicating whether execution went alright or an error occured. As a succesful execution doesn't require any explanation, it needs only one exit status. If there was a problem, however, it is useful to know what went wrong. Therefore, 0 is used for a succesful execution, and 1-255 to indicate what kind of error occured. The meaning of the numbers 1-255 differs depending on the program returning them.

Anyway, _if_ executes the block after _then_ when the command returns 0. Yes, conditions are commands. The phrase [ $foo -ge 3 ] returns an exit status, and the other two syntaxes as well! Therefore, there's a neat trick you can use to quickly test a condition:

> [ $foo -ge 3 ] && echo true

In this example, "echo true" is only executed if "[ $foo -ge 3 ]" returns 0 (true). Why is that, you might ask. It's because bash only evaluates a condition when needed. When using the _and_ combining expression, both conditions need to be true to make the combining expression return true. If the first condition returns false, it doesn't matter what the second one returns; the result will be false. Therefore, bash doesn't evaluate the second condition, and that's the reason why "echo true" is not executed in the example. This is the same for the _or_ operator ("||"), where the second condition is not evaluated if the first one is true.

Well, so much for the diving. If you want to know even more, I'd like to point you to the [Advanced Bash-Scripting Guide](http://www.tldp.org/LDP/abs/html/tests.html) and maybe the [Bash Reference Manual](http://www.gnu.org/software/bash/manual/bashref.html#Conditional-Constructs).

## Conclusion

In this tutorial, you've been able to make a start at understanding the many possibilities of conditions in bash scripting. You've been able to read about the basic rules of writing and using conditions, about the three syntaxes and their properties, and maybe you took the opportunity to dive a little deeper. I hope you enjoyed the reading as much as I enjoyed the writing. You can always return here to look up conditions in [the table](http://www.linuxtutorialblog.com/post/tutorial-conditions-in-bash-scripting-if-statements#table-of-conditions) (bookmark that link to see the table directly), or to refresh your knowledge. If you have any suggestions, additions or other feedback, feel free to comment. Thanks for reading and happy scripting!

