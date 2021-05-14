# [Conditions in bash scripting (if statements)](http://www.linuxtutorialblog.com/post/tutorial-conditions-in-bash-scripting-if-statements)

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

```bash
if <condition>; then
<commands>
fi
```

The condition is, depending on its type, surrounded by certainbrackets, eg. [ ]. You can read about the different types further on

in the tutorial. You can add commands to be executed when the condition is false using the _else_ keyword, and use the _elif_ (elseif) keyword to execute commands on another condition if the primary condition is false. The _else_ keyword always comes last. Example:

```bash
if [ -r somefile ]; then
  content=$(cat somefile)
elif [ -f somefile ]; then
  echo "The file 'somefile' exists but is not readable to the script."
else
  echo "The file 'somefile' does not exist."
fi
```

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

Check out here: <https://carnet-classic.danielhan.dev/home/technical-tips/linux-unix/shell-programming/bash-tips/conditions-in-bash-scripting-if-statements.html>
## Diving a little deeper

I said I'd tell more about the fact that _if_ essentially checks the exit status of commands. And so I will. The basic rule of bash when it comes to conditions is _0 equals true, >0 equals false_.
That's pretty much the opposite of many programming languages where 0 equals false and 1 (or more) equals true. The reason behind this is that shells like bash deal with programs a lot. By UNIX convention, programs use an exit status for indicating whether execution went alright or an error occured. As a succesful execution doesn't require any explanation, it needs only one exit status. If there was a problem, however, it is useful to know what went wrong. Therefore, 0 is used for a succesful execution, and 1-255 to indicate what kind of error occured. The meaning of the numbers 1-255 differs depending on the program returning them.

Anyway, _if_ executes the block after _then_ when the command returns 0. Yes, conditions are commands. The phrase [ $foo -ge 3 ] returns an exit status, and the other two syntaxes as well! Therefore, there's a neat trick you can use to quickly test a condition:

> [ $foo -ge 3 ] && echo true

In this example, "echo true" is only executed if "[ $foo -ge 3 ]" returns 0 (true). Why is that, you might ask. It's because bash only evaluates a condition when needed. When using the _and_ combining expression, both conditions need to be true to make the combining expression return true. If the first condition returns false, it doesn't matter what the second one returns; the result will be false. Therefore, bash doesn't evaluate the second condition, and that's the reason why "echo true" is not executed in the example. This is the same for the _or_ operator ("||"), where the second condition is not evaluated if the first one is true.

Well, so much for the diving. If you want to know even more, I'd like to point you to the [Advanced Bash-Scripting Guide](http://www.tldp.org/LDP/abs/html/tests.html) and maybe the [Bash Reference Manual](http://www.gnu.org/software/bash/manual/bashref.html#Conditional-Constructs).

## Conclusion

In this tutorial, you've been able to make a start at understanding the many possibilities of conditions in bash scripting. You've been able to read about the basic rules of writing and using conditions, about the three syntaxes and their properties, and maybe you took the opportunity to dive a little deeper. I hope you enjoyed the reading as much as I enjoyed the writing. You can always return here to look up conditions in [the table](http://www.linuxtutorialblog.com/post/tutorial-conditions-in-bash-scripting-if-statements#table-of-conditions) (bookmark that link to see the table directly), or to refresh your knowledge. If you have any suggestions, additions or other feedback, feel free to comment. Thanks for reading and happy scripting!
