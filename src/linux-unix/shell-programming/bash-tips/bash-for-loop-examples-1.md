# [Bash For Loop Examples](http://www.cyberciti.biz/faq/bash-for-loop/)

How do I use bash for loop to repeat certain task under Linux / UNIX operating system? How do I set infinite loops using for statement? How do I use three-parameter for loop control expression?

A 'for loop' is a bash programming language statement which allows code to be repeatedly executed. A for loop is classified as an iteration statement i.e. it is the repetition of a process within a bash script.


For example, you can run UNIX command or task 5 times or read and process list of files using a for loop. A for loop can be used at a shell prompt or within a shell script itself.

Numeric ranges for syntax is as follows:


    for VARIABLE in 1 2 3 4 5 .. N
    do command1 command2 commandN
    done

OR


    for VARIABLE in file1 file2 file3
    do command1 on $VARIABLE command2 commandN
    done

OR


    for OUTPUT in $(Linux-Or-Unix-Command-Here)
    do command1 on $OUTPUT command2 on $OUTPUT commandN
    done

## Examples


This type of for loop is characterized by counting. The range is specified by a beginning (#1) and ending number (#5). The for loop executes a sequence of commands for each member in a list of items. A representative example in BASH is as follows to display welcome message 5 times with for loop:


```bash
    #!/bin/bash
    for i in 1 2 3 4 5
    do echo "Welcome $i times"
    done
```

Sometimes you may need to set a step value (allowing one to count by two's or to count backwards for instance). Latest **bash version 3.0+** has inbuilt support for setting up ranges:


```bash
     #!/bin/bash
    for i in {1..5}
    do echo "Welcome $i times"
    done
```

Bash v4.0+ has inbuilt support for setting up a step value using {START **..** END **..** INCREMENT} syntax:


```bash
    #!/bin/bash
    echo "Bash version ${BASH_VERSION}..."
    for i in {0..10..2} do echo "Welcome $i times" done
```

Sample outputs:


    Bash version 4.0.33(0)-release...
    Welcome 0 times
    Welcome 2 times
    Welcome 4 times
    Welcome 6 times
    Welcome 8 times
    Welcome 10 times

### The seq command (outdated)

![](http://figs.cyberciti.biz/warning-40px.png)**WARNING!** The seq command print a sequence of numbers and it is here due to historical reasons. The following examples is only recommend for older bash version. All users (bash v3.x+) are recommended to use the above syntax.

The [seq command](http://www.cyberciti.biz/tips/how-to-generating-print-range-sequence-of-numbers.html) can be used as follows. A representative example in seq is as follows:


```bash
    #!/bin/bash
    for i in $(seq 1 2 20)
    do echo "Welcome $i times"
    done
```

There is no good reason to use an external command such as seq to count and increment numbers in the for loop, hence it is recommend that you avoid using seq. The builtin command are fast.

## Three-expression bash for loops syntax

This type of for loop share a common heritage with the C programming language. It is characterized by a three-parameter loop control expression; consisting of an initializer (EXP1), a loop-test or condition (EXP2), and a counting expression (EXP3).


    for (( EXP1; EXP2; EXP3 ))
    do command1 command2 command3
    done

A representative three-expression example in bash as follows:


```bash
    #!/bin/bash
    for (( c=1; c<=5; c++ ))
    do echo "Welcome $c times"
    done
```

Sample output:

    Welcome 1 times
    Welcome 2 times
    Welcome 3 times
    Welcome 4 times
    Welcome 5 times

## How do I use for as infinite loops?

Infinite for loop can be created with empty expressions, such as:


```bash
    #!/bin/bash
    for (( ; ; ))
    do echo "infinite loops [ hit CTRL+C to stop]"
    done
```

## Conditional exit with break

You can do early exit with break statement inside the for loop. You can exit from within a FOR, WHILE or UNTIL loop using break. General break statement inside the for loop:


```bash
    for I in 1 2 3 4 5
    do statements1 #Executed for all values of ''I'', up to a disaster-condition if any. statements2 if (disaster-condition) then break #Abandon the loop. fi statements3 #While good and, no disaster-condition.
    done
```

Following shell script will go though all files stored in /etc directory. The for loop will be abandon when /etc/resolv.conf file found.

```bash
    #!/bin/bash
    for file in /etc/*
    do if [ "${file}" == "/etc/resolv.conf" ] then countNameservers=$(grep -c nameserver /etc/resolv.conf) echo "Total ${countNameservers} nameservers defined in ${file}" break fi
    done
```

### Early continuation with continue statement

To resume the next iteration of the enclosing FOR, WHILE or UNTIL loop use continue statement.

```bash
    for I in 1 2 3 4 5
    do statements1 #Executed for all values of ''I'', up to a disaster-condition if any. statements2 if (condition) then continue #Go to next iteration of I in the loop and skip statements3 fi statements3
    done
```

This script make backup of all file names specified on command line. If .bak file exists, it will skip the cp command.

```bash
    #!/bin/bash
    FILES="$@"
    for f in $FILES
    do # if .bak backup file exists, read next file if [ -f ${f}.bak ] then echo "Skiping $f file..." continue # read next file and skip cp command fi # we are hear means no backup file exists, just use cp command to copy file /bin/cp $f $f.bak
    done
```

## Check out related media

This tutorial is also available in a quick video format. The video shows some additional and practical examples such as converting all flac music files to mp3 format, all avi files to mp4 video format, unzipping multiple zip files or tar balls, gathering uptime information from multiple Linux/Unix servers, detecting remote web-server using domain names and much more.






[Video 01: 15 Bash For Loop Examples for Linux / Unix / OS X Shell Scripting ](http://youtu.be/ocXb3qeg7Es)


#### Recommended readings:

* See all sample for loop shell script in our bash shell directory.
* Bash for loop syntax and usage page from the Linux shell scripting wiki.
* man bash
* help for
* help {
* help break
* help continue
