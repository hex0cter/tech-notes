# [Korn Shell Arrays](http://docstore.mik.ua/orelly/unix/ksh/ch06_03.htm)

So far we have seen two types of variables: character strings and integers. The third type of variable the Korn shell supports is an _array_. As you may know, an array is like a list of things; you can refer to specific elements in an array with integer _indices_ , so that _a[i]_ refers to the _i_ th element of array _a_.

The Korn shell provides an array facility that, while useful, is much more limited than analogous features in conventional programming languages. In particular, arrays can be only one-dimensional (i.e., no arrays of arrays), and they are limited to 1024 elements. Indices can start at 0.

There are two ways to assign values to elements of an array. The first is the most intuitive: you can use the standard shell variable assignment syntax with the array index in brackets ( **[]** ). For example:

>
>     nicknames[2]=bob
>     nicknames[3]=ed

puts the values **bob** and **ed** into the elements of the array **nicknames** with indices 2 and 3, respectively. As with regular shell variables, values assigned to array elements are treated as character strings unless the assignment is preceded by **let**.

The second way to assign values to an array is with a variant of the **set** statement, which we saw in [Chapter 3, Customizing Your Environment](http://docstore.mik.ua/orelly/unix/ksh/ch03_01.htm). The statement:

>
>     set -A _aname val1 val2 val3_ ...

creates the array _aname_ (if it doesn't already exist) and assigns _val1_ to _aname[0]_ , _val2_ to _aname[1]_ , etc. As you would guess, this is more convenient for loading up an array with an initial set of values.

To extract a value from an array, use the syntax **${** _aname_ **[** _i_ **]}**. For example, **${nicknames[2]}** has the value "bob". The index _i_ can be an arithmetic expression-see above. If you use `*` in place of the index, the value will be all elements, separated by spaces. Omitting the index is the same as specifying index 0.

Now we come to the somewhat unusual aspect of Korn shell arrays. Assume that the only values assigned to **nicknames** are the two we saw above. If you type **print** `"` **${nicknames[**`*` **]}"** , you will see the output:

>
>     bob ed

In other words, **nicknames[0]** and **nicknames[1]** don't exist. Furthermore, if you were to type:

>
>     nicknames[9]=pete
>     nicknames[31]=ralph

and then type **print** `"` **${nicknames[**`*` **]}"** , the output would look like this:

>
>     bob ed pete ralph

This is why we said "the elements of **nicknames** with indices 2 and 3" earlier, instead of "the 2nd and 3rd elements of **nicknames** ". Any array elements with unassigned values just don't exist; if you try to access their values, you will get null strings.

You can preserve whatever whitespace you put in your array elements by using `"` **$** { _aname_ **[@]** } `"` (with the double quotes) instead of **$** { _aname_ **[**`*` **]** }`"`, just as you can with `"` **$@**`"` instead of **$**`*`.

The shell provides an operator that tells you how many elements an array has defined: **${#** _aname_ **[**`*`] **}**. Thus **${#nicknames[**`*`] **}** has the value 4. Note that you need the **[**`*` **]** because the name of the array alone is interpreted as the 0th element. This means, for example, that **${#nicknames}** equals the length of **nicknames[0]** (see [Chapter 4](http://docstore.mik.ua/orelly/unix/ksh/ch04_01.htm)). Since **nicknames[0]** doesn't exist, the value of **${#nicknames}** is 0, the length of the null string.

To be quite frank, we feel that the Korn shell's array facility is of little use to shell programmers. This is partially because it is so limited, but mainly because shell programming tasks are much more often oriented toward character strings and text than toward numbers. If you think of an array as a mapping from integers to values (i.e., put in a number, get out a value), then you can see why arrays are "number-dominated" data structures.

Nevertheless, we can find useful things to do with arrays. For example, here is a cleaner solution to Task 5-4, in which a user can select his or her terminal type ( **TERM** environment variable) at login time. Recall that the "user-friendly" version of this code used **select** and a **case** statement:

>
>     print 'Select your terminal type:'
>     PS3='terminal? '
>     select term in
>         'Givalt GL35a' \
>         'Tsoris T-2000' \
>         'Shande 531' \
>         'Vey VT99'
>     do
>         case $REPLY in
>             1 ) TERM=gl35a ;;
>             2 ) TERM=t2000 ;;
>             3 ) TERM=s531 ;;
>             4 ) TERM=vt99 ;;
>             * ) print "invalid." ;;
>         esac
>         if [[ -n $term ]]; then
>             print "TERM is $TERM"
>             break
>         fi
>     done

We can eliminate the entire **case** construct by taking advantage of the fact that the **select** construct stores the user's number choice in the variable **REPLY**. We just need a line of code that stores all of the possibilities for **TERM** in an array, in an order that corresponds to the items in the **select** menu. Then we can use **$REPLY** to index the array. The resulting code is:

>
>     set -A termnames gl35a t2000 s531 vt99
>     print 'Select your terminal type:'
>     PS3='terminal? '
>     select term in
>         'Givalt GL35a' \
>         'Tsoris T-2000' \
>         'Shande 531' \
>         'Vey VT99'
>     do
>         if [[ -n $term ]]; then
>             TERM=${termnames[REPLY-1]}
>             print "TERM is $TERM"
>             break
>         fi
>     done

This code sets up the array **termnames** so that **${termnames[0]}** is "gl35a", **${termnames[1]}** is "t2000", etc. The line **TERM=${termnames[REPLY-1]}** essentially replaces the entire **case** construct by using **REPLY** to index the array.

Notice that the shell knows to interpret the text in an array index as an arithmetic expression, as if it were enclosed in **((** and **))** , which in turn means that variable need not be preceded by a dollar sign ( **$** ). We have to subtract 1 from the value of **REPLY** because array indices start at 0, while **select** menu item numbers start at 1.

The final Korn shell feature that relates to the kinds of values that variables can hold is the **typeset** command. If you are a programmer, you might guess that **typeset** is used to specify the _type_ of a variable (integer, string, etc.); you'd be partially right.

**typeset** is a rather _ad hoc_ collection of things that you can do to variables that restrict the kinds of values they can take. Operations are specified by options to **typeset** ; the basic syntax is:

>
>     typeset _-o varname_ [= _value_ ]

Options can be combined; multiple _varname_ s can be used. If you leave out _varname_ , the shell prints a list of variables for which the given option is turned on.

The options available break down into two basic categories:

  1. String formatting operations, such as right- and left-justification, truncation, and letter case control.

  2. Type and attribute functions that are of primary interest to advanced programmers.




**typeset** without options has an important meaning: if a **typeset** statement is inside a function definition, then the variables involved all become _local_ to that function (in addition to any properties they may take on as a result of **typeset** options). The ability to define variables that are local to "subprogram" units (procedures, functions, subroutines, etc.) is necessary for writing large programs, because it helps keep subprograms independent of the main program and of each other.

If you just want to declare a variable local to a function, use **typeset** without any options. For example:

>
>     function afunc {
>         typeset diffvar
>         samevar=funcvalue
>         diffvar=funcvalue
>         print "samevar is $samevar"
>         print "diffvar is $diffvar"
>     }
>
>     samevar=globvalue
>     diffvar=globvalue
>     print "samevar is $samevar"
>     print "diffvar is $diffvar"
>     afunc
>     print "samevar is $samevar"
>     print "diffvar is $diffvar"

This code will print the following:

>
>     samevar is globvalue
>     diffvar is globvalue
>     samevar is funcvalue
>     diffvar is funcvalue
>     samevar is funcvalue
>     diffvar is globvalue

[Figure 6.1](http://docstore.mik.ua/orelly/unix/ksh/ch06_03.htm#KSH-CH-6-FIG-0) shows this graphically.

#### Figure 6.1: Local variables in functions

![Figure 6.1](http://docstore.mik.ua/orelly/unix/ksh/figs/korn0601.gif)

You will see several additional examples of local variables within functions in [Chapter 9](http://docstore.mik.ua/orelly/unix/ksh/ch09_01.htm).

Now let's look at the various options to **typeset**. [Table 6.5](http://docstore.mik.ua/orelly/unix/ksh/ch06_03.htm#KSH-CH-6-TAB-4) lists the string formatting options; the first three take an optional numeric argument.

Table 6.5: Typeset String Formatting Options Option | Operation
---|---
**-L** _n_ |

Left-justify. Remove leading blanks; if _n_ is given, fill with blanks or truncate on right to length _n_.

**-R** _n_ |

Right-justify. Remove trailing blanks; if _n_ is given, fill with blanks or truncate on left to length _n_.

**-Z** _n_ |

Same as above, except add leading 0's instead of blanks if needed.

**-l** |  Convert letters to lowercase.
**-u** |  Convert letters to uppercase.

Here are a few simple examples. Assume that the variable **alpha** is assigned the letters of the alphabet, in alternating case, surrounded by three blanks on each side:

>
>     alpha="   aBcDeFgHiJkLmNoPqRsTuVwXyZ   "

[Table 6.6](http://docstore.mik.ua/orelly/unix/ksh/ch06_03.htm#KSH-CH-6-TAB-5) shows some **typeset** statements and their resulting values (assuming that each of the statements are run "independently").

Table 6.6: Examples of typeset String Formatting Options Statement | Value of v
---|---
**typeset -L** v=$alpha | `"aBcDeFgHiJkLmNoPqRsTuVwXyZ "`
**typeset -L10** v=$alpha | `"aBcDeFgHiJ"`
**typeset -R** v=$alpha | `" aBcDeFgHiJkLmNoPqRsTuVwXyZ"`
**typeset -R16** v=$alpha | `"kLmNoPqRsTuVwXyZ"`
**typeset -l** v=$alpha | `" abcdefghijklmnopqrstuvwxyz"`
**typeset -uR5** v=$alpha | `"VWXYZ"`
**typeset -Z8** v=`"123.50"` | `"00123.50"`

When you run **typeset** on an existing variable, its effect is _cumulative_ with whatever **typeset** s may have been used previously. This has the obvious exceptions:

  * A **typeset -u** undoes a **typeset -l** , and vice versa.

  * A **typeset -R** undoes a **typeset -L** , and vice versa.

  * **typeset -Z** has no effect if **typeset -L** has been used.




You can turn off **typeset** options explicitly by typing **typeset +** _o_ , where _o_ is the option you turned on before. Of course, it is hard to imagine scenarios where you would want to turn multiple **typeset** formatting options on and off over and over again; you usually set a **typeset** option on a given variable only once.

An obvious application for the **-L** and **-R** options is one in which you need fixed-width output. The most ubiquitous source of fixed-width output in the UNIX system is reflected in the following programming task.

> Pretend that _ls_ doesn't do multicolumn output; write a shell script that does it.

For the sake of simplicity, we'll assume further that our version of UNIX is derived from AT&T System V, in which filenames are ( _still!_ ) limited to 14 characters.

Our solution to this task relies on many of the concepts we have seen earlier in this chapter. It also relies on the fact that **set -A** (for constructing arrays) can be combined with command substitution in an interesting way: each word (separated by blanks, TABs, or NEWLINESs) becomes an element of the array. For example, if the file _bob_ contains 50 words, then after the statement:

>
>     set -A fred $(< bob)

the array **fred** has 50 elements.

Our strategy is to get the names of all files in the given directory into an array variable. We use a **while** loop that mimics a **for** loop, as we saw earlier in this chapter, to get each filename into a variable whose length has been set to 14. We print that variable in five-column format, with two spaces between each column (for a total of 80 columns), using a counter to keep track of columns. Here is the code:

>
>     set -A filenames $(ls $1)
>     typeset -L14 fname
>     let count=0
>     let numcols=5
>
>     while (( $count < ${#filenames[*]} )); do
>         fname=${filenames[count]}
>         print -n "$fname  "
>         let count="count + 1"
>         if (( count % numcols == 0 )); then
>             print		# NEWLINE
>         fi
>     done
>
>     if (( count % numcols != 0 )); then
>         print
>     fi

The first line sets up the array **filenames** to contain all files in the directory given by the first argument (the current directory by default). The **typeset** statement sets up the variable **fname** to have a fixed width of 14 characters. The next line initializes a counter that counts elements in the array. **numcols** is the number of columns per line.

The **while** loop iterates once for every element in **filenames**. In the body of the loop, the first line assigns the next array element to the fixed-width variable. The **print** statement prints the latter followed by two spaces; the **-n** option suppresses **print** 's final NEWLINE.

The **let** statements increments the counter. Then there is the **if** statement, which determines when to start the next line. It checks the _remainder_ of **$count** divided by **$numcols** -remember that dollar signs aren't necessary within a **$((**... **))** construct-and if the result is 0, it's time to output a NEWLINE via a **print** statement without arguments. Notice that even though **$count** increases by 1 with every iteration of the loop, the remainder goes through a cycle of 1, 2, 3, 4, 0, 1, 2, 3, 4, 0,...

After the loop, an **if** construct outputs a final NEWLINE if necessary, i.e., if the **if** within the loop didn't just do it.

We can also use **typeset** options to clean up the code for our _dosmv_ function (Task 5-3), which translates filenames in a given directory from MS-DOS to UNIX format. The code for the function is:

>
>     dos_regexp='[^a-z]\{1,8\}\.[^a-z]\{0,3\}'
>     for filename in ${1:+$1/}* ; do
>         if print "$filename" | grep $dos_regexp > /dev/null; then
>             newfilename=$(print $filename | tr [A-Z] [a-z])
>             newfilename=${newfilename%.}
>             print "$filename -> $newfilename"
>             mv $filename $newfilename
>         fi
>     done

We can replace the call to _tr_ in the **for** loop with one to **typeset -l** before the loop:

>
>     typeset -l newfilename
>     dos_regexp='[^a-z]\{1,8\}\.[^a-z]\{0,3\}'
>     for filename in ${1:+$1/}* ; do
>         if print "$filename" | grep $dos_regexp > /dev/null; then
>             newfilename=${filename%.}
>             print "$filename -> $newfilename"
>             mv $filename $newfilename
>         fi
>     done

This way, the translation to lowercase letters is done automatically each time a value is assigned to **newfilename**. Not only is this code cleaner, but it is also more efficient because the extra processes created by _tr_ and command substitution are eliminated.

The other options to **typeset** are of more use to advanced shell programmers who are "tweaking" large scripts. These options are listed in [Table 6.7](http://docstore.mik.ua/orelly/unix/ksh/ch06_03.htm#KSH-CH-6-TAB-6).

Table 6.7: Typeset Type and Attribute Options Option | Operation
---|---
**-i** _n_ |

Represent the variable internally as an integer; improves efficiency of arithmetic. If _n_ is given, it is the base used for output.

**-r** |

Make the variable read-only: forbid assignment to it and disallow it from being **unset**.[6]

**-x** |

Export; same as **export** command.

**-f** |

Refer to function names only; see "Function Options" below.

> [6] The built-in command **readonly** does the same thing.

**-i** is the most useful of these. You can put it in a script when you are done writing and debugging it to make arithmetic run a bit faster, though the speedup will be apparent only if your script does a _lot_ of arithmetic. The more readable **integer** is a built-in alias for **typeset -i** , so that **integer x=5** is the same as **typeset -i x=5**.

The **-r** option is useful for setting up "constants" in shell scripts; constants are like variables except that you can't change their values once they have been initialized. Constants allow you to give names to values even if you don't want them changed; it is considered good programming practice to use constants in large programs.

The solution to Task 6-2 contains a good candidate for **typeset -r** : the variable **numcols** , which specifies the number of columns in the output. Since **numcols** is an integer, we could also use the **-i** option, i.e., replace **let numcols=5** with **typeset -ri numcols=5**. If we were to try assigning another value to **numcols** , the shell would respond with the error message **ksh: numcols: is read only**.

**-r** is also useful for system administrators who set up shell variables in _/etc/profile_ , the system-wide Korn shell initialization file. For example, if you wanted to tighten system security, one step you might take is to prevent the **PATH** environment variable from being changed. This helps prevent computer crackers from installing bogus executables. The statement **typeset -r PATH** does the trick.

These options are also useful without arguments, i.e., to see which variables exist that have those options turned on.

The **-f** option has various suboptions, all of which relate to functions. These are listed in [Table 6.8](http://docstore.mik.ua/orelly/unix/ksh/ch06_03.htm#KSH-CH-6-TAB-7).

Table 6.8: Typeset Function Options Option | Operation
---|---
**-f** |  With no arguments, prints all function definitions.
**-f** _fname_ |  Prints the definition of function _fname_.
**+f** |  Prints all function names.
**-ft** |  Turns on trace mode for named function(s). ([Chapter 9](http://docstore.mik.ua/orelly/unix/ksh/ch09_01.htm))
**+ft** |  Turns off trace mode for named function(s). ([Chapter 9](http://docstore.mik.ua/orelly/unix/ksh/ch09_01.htm))
**-fu** |  Defines given name(s) as autoloaded function(s). ([Chapter 4](http://docstore.mik.ua/orelly/unix/ksh/ch04_01.htm))

Two of these have built-in aliases that are more mnemonic: **functions** is an alias for **typeset -f** and **autoload** is an alias for **typeset -fu**.

Finally, if you type **typeset** without _any_ arguments, you will see a list of _all_ currently-defined variables (in no discernable order), preceded by appropriate keywords if they have one or more **typeset** options turned on. For example, typing **typeset** in an uncustomized shell gives you a listing of the shell's built-in variables and their attributes that looks like this: [7]

> [7] For some reason, this list excludes **PS1** and a few others.

>
>     export HZ
>     export PATH
>     integer ERRNO
>     integer OPTIND
>     function LINENO
>     export LOGNAME
>     export MAIL
>     function SECONDS
>     integer PPID
>     PS3
>     PS2
>     export TERMCAP
>     OPTARG
>     function RANDOM
>     export SHELL
>     integer TMOUT
>     export HOME
>     export _
>     FCEDIT
>     export TERM
>     export PWD
>     export TZ
>     integer MAILCHECK

<http://docstore.mik.ua/orelly/unix/ksh/ch06_03.htm>
