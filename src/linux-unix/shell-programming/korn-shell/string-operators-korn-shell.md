
date: None  
author(s): None  

# [String Operators (Korn Shell) - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/korn-shell/string-operators-korn-shell)

The basic idea behind the syntax of string operators is that special characters that denote operations are inserted between the variable's name and the right curly brackets. Any argument that the operator may need is inserted to the operator's right.

The first group of string-handling operators tests for the existence of variables and allows substitutions of default values under certain conditions. These are listed in [Table 4.1](http://docstore.mik.ua/orelly/unix2.1/ksh/ch04_03.htm#KSH-CH-4-TAB-0). [6]

> [6] The colon (`:`) in each of these operators is actually optional. If the colon is omitted, then change "exists and isn't null" to "exists" in each definition, i.e., the operator tests for existence only. 

> [7] Pascal, Modula, and Ada programmers may find it helpful to recognize the similarity of this to the assignment operators in those languages.

The first two of these operators are ideal for setting defaults for command-line arguments in case the user omits them. We'll use the first one in our first programming task.

> You have a large album collection, and you want to write some software to keep track of it. Assume that you have a file of data on how many albums you have by each artist. Lines in the file look like this:
>
>> 
>>     14	Bach, J.S.
>>     1	Balachander, S.
>>     21	Beatles
>>     6	Blakey, Art
> 
> Write a program that prints the _N_ highest lines, i.e., the _N_ artists by whom you have the most albums. The default for _N_ should be 10. The program should take one argument for the name of the input file and an optional second argument for how many lines to print.

By far the best approach to this type of script is to use built-in UNIX utilities, combining them with I/O redirectors and pipes. This is the classic "building-block" philosophy of UNIX that is another reason for its great popularity with programmers. The building-block technique lets us write a first version of the script that is only one line long:

> 
>     sort -nr $1 | head -${2:-10}

Here is how this works: the _sort_ (1) program sorts the data in the file whose name is given as the first argument ( **$1** ). The **-n** option tells _sort_ to interpret the first word on each line as a number (instead of as a character string); the **-r** tells it to reverse the comparisons, so as to sort in descending order.

The output of _sort_ is piped into the _head_ (1) utility, which, when given the argument **-** _N_ , prints the first _N_ lines of its input on the standard output. The expression **-${2:-10}** evaluates to a dash ( **-** ) followed by the second argument if it is given, or to -10 if it's not; notice that the variable in this expression is **2** , which is the second positional parameter.

Assume the script we want to write is called _highest_. Then if the user types **highest myfile** , the line that actually runs is:

> 
>     sort -nr myfile | head -10

Or if the user types **highest myfile 22** , the line that runs is:

> 
>     sort -nr myfile | head -22

Make sure you understand how the **:-** string operator provides a default value.

This is a perfectly good, runnable script-but it has a few problems. First, its one line is a bit cryptic. While this isn't much of a problem for such a tiny script, it's not wise to write long, elaborate scripts in this manner. A few minor changes will make the code more readable. 

First, we can add comments to the code; anything between # and the end of a line is a comment. At a minimum, the script should start with a few comment lines that indicate what the script does and what arguments it accepts. Second, we can improve the variable names by assigning the values of the positional parameters to regular variables with mnemonic names. Finally, we can add blank lines to space things out; blank lines, like comments, are ignored. Here is a more readable version:

> 
>     #
>     #	highest filename [howmany]
>     #
>     #	Print howmany highest-numbered lines in file filename.
>     #	The input file is assumed to have lines that start with
>     #	numbers.  Default for howmany is 10.
>     #
>     
>     filename=$1
>     
>     howmany=${2:-10}
>     sort -nr $filename | head -$howmany

The square brackets around **howmany** in the comments adhere to the convention in UNIX documentation that square brackets denote optional arguments.

The changes we just made improve the code's readability but not how it runs. What if the user were to invoke the script without any arguments? Remember that positional parameters default to null if they aren't defined. If there are no arguments, then **$1** and **$2** are both null. The variable **howmany** ( **$2** ) is set up to default to 10, but there is no default for **filename** ( **$1** ). The result would be that this command runs:

> 
>     sort -nr | head -10

As it happens, if _sort_ is called without a filename argument, it expects input to come from standard input, e.g., a pipe (|) or a user's terminal. Since it doesn't have the pipe, it will expect the terminal. This means that the script will appear to hang! Although you could always type ` [CTRL-D]` or `[CTRL-C]` to get out of the script, a naive user might not know this.

Therefore we need to make sure that the user supplies at least one argument. There are a few ways of doing this; one of them involves another string operator. We'll replace the line:

> 
>     filename=$1

with:

> 
>     filename=${1:?"filename missing."}

This will cause two things to happen if a user invokes the script without any arguments: first the shell will print the somewhat unfortunate message:

> 
>     highest: 1: filename missing.

to the standard error output. Second, the script will exit without running the remaining code.

With a somewhat "kludgy" modification, we can get a slightly better error message. Consider this code:

> 
>     filename=$1
>     filename=${filename:?"missing."}

This results in the message:

> 
>     highest: filename: missing.

(Make sure you understand why.) Of course, there are ways of printing whatever message is desired; we'll find out how in [Chapter 5](http://docstore.mik.ua/orelly/unix2.1/ksh/ch05_01.htm).

Before we move on, we'll look more closely at the two remaining operators in [Table 4.1](http://docstore.mik.ua/orelly/unix2.1/ksh/ch04_03.htm#KSH-CH-4-TAB-0) and see how we can incorporate them into our task solution. The **:=** operator does roughly the same thing as **:-** , except that it has the "side effect" of setting the value of the variable to the given word if the variable doesn't exist.

Therefore we would like to use **:=** in our script in place of **:-** , but we can't; we'd be trying to set the value of a positional parameter, which is not allowed. But if we replaced:

> 
>     howmany=${2:-10}

with just:

> 
>     howmany=$2

and moved the substitution down to the actual command line (as we did at the start), then we could use the **:=** operator:

> 
>     sort -nr $filename | head -${howmany:=10}

Using **:=** has the added benefit of setting the value of **howmany** to 10 in case we need it afterwards in later versions of the script.

The final substitution operator is **:+**. Here is how we can use it in our example: Let's say we want to give the user the option of adding a header line to the script's output. If he or she types the option **-h** , then the output will be preceded by the line:

> 
>     ALBUMS  ARTIST

Assume further that this option ends up in the variable **header** , i.e., **$header** is **-h** if the option is set or null if not. (Later we will see how to do this without disturbing the other positional parameters.)

The expression: 

> 
>     ${header:+"ALBUMS  ARTIST\n"}

yields null if the variable **header** is null, or **ALBUMS══ARTIST \n** if it is non-null. This means that we can put the line:

> 
>     print -n ${header:+"ALBUMS  ARTIST\n"}

right before the command line that does the actual work. The **-n** option to **print** causes it _not_ to print a LINEFEED after printing its arguments. Therefore this **print** statement will print nothing-not even a blank line-if **header** is null; otherwise it will print the header line and a LINEFEED (\n).

