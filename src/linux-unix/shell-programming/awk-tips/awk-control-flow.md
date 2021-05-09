# [Control Statements of AWK](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_11.html)

Control statements such as `if`, `while`, and so on control the flow of execution in `awk` programs. Most of the control statements in `awk` are patterned on similar statements in C.

All the control statements start with special keywords such as `if` and `while`, to distinguish them from simple expressions.

Many control statements contain other statements; for example, the `if` statement contains another statement which may or may not be executed. The contained statement is called the body. If you want to include more than one statement in the body, group them into a single compound statement with curly braces, separating them with newlines or semicolons.

## [The `if` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC72)

The `if`-`else` statement is `awk`'s decision-making statement. It looks like this:


    if (condition) then-body [else else-body]


Here condition is an expression that controls what the rest of the statement will do. If condition is true, then-body is executed; otherwise, else-body is executed (assuming that the `else` clause is present). The `else` part of the statement is optional. The condition is considered false if its value is zero or the null string, true otherwise.

Here is an example:


    if (x % 2 == 0)
        print "x is even"
    else
        print "x is odd"


In this example, if the expression `x % 2 == 0` is true (that is, the value of `x` is divisible by 2), then the first `print` statement is executed, otherwise the second `print` statement is performed.

If the `else` appears on the same line as then-body, and then-body is not a compound statement (i.e., not surrounded by curly braces), then a semicolon must separate then-body from `else`. To illustrate this, let's rewrite the previous example:


    awk '{ if (x % 2 == 0) print "x is even"; else
            print "x is odd" }'


If you forget the `;', `awk` won't be able to parse the statement, and you will get a syntax error.

We would not actually write this example this way, because a human reader might fail to see the `else` if it were not the first thing on its line.

## [The `while` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC73)

In programming, a loop means a part of a program that is (or at least can be) executed two or more times in succession.

The `while` statement is the simplest looping statement in `awk`. It repeatedly executes a statement as long as a condition is true. It looks like this:


    while (condition) body


Here body is a statement that we call the body of the loop, and condition is an expression that controls how long the loop keeps running.

The first thing the `while` statement does is test condition. If condition is true, it executes the statement body. (Truth, as usual in `awk`, means that the value of condition is not zero and not a null string.) After body has been executed, condition is tested again, and if it is still true, body is executed again. This process repeats until condition is no longer true. If condition is initially false, the body of the loop is never executed.

This example prints the first three fields of each record, one per line.


    awk '{ i = 1
           while (i <= 3) {
               print $i
               i++
           }
    }'


Here the body of the loop is a compound statement enclosed in braces, containing two statements.

The loop works like this: first, the value of `i` is set to 1. Then, the `while` tests whether `i` is less than or equal to three. This is the case when `i` equals one, so the `i`-th field is printed. Then the `i++` increments the value of `i` and the loop repeats. The loop terminates when `i` reaches 4.

As you can see, a newline is not required between the condition and the body; but using one makes the program clearer unless the body is a compound statement or is very simple. The newline after the open-brace that begins the compound statement is not required either, but the program would be hard to read without it.

## [The `do`-`while` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC74)

The `do` loop is a variation of the `while` looping statement. The `do` loop executes the body once, then repeats body as long as condition is true. It looks like this:


    do body
    while (condition)


Even if condition is false at the start, body is executed at least once (and only once, unless executing body makes condition true). Contrast this with the corresponding `while` statement:


    while (condition) body


This statement does not execute body even once if condition is false to begin with.

Here is an example of a `do` statement:


    awk '{ i = 1
           do {
              print $0
              i++
           } while (i <= 10)
    }'


prints each input record ten times. It isn't a very realistic example, since in this case an ordinary `while` would do just as well. But this reflects actual experience; there is only occasionally a real use for a `do` statement.

## [The `for` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC75)

The `for` statement makes it more convenient to count iterations of a loop. The general form of the `for` statement looks like this:


    for (initialization; condition; increment) body


This statement starts by executing initialization. Then, as long as condition is true, it repeatedly executes body and then increment. Typically initialization sets a variable to either zero or one, increment adds 1 to it, and condition compares it against the desired number of iterations.

Here is an example of a `for` statement:


    awk '{ for (i = 1; i <= 3; i++)
              print $i
    }'


This prints the first three fields of each input record, one field per line.

In the `for` statement, body stands for any statement, but initialization, condition and increment are just expressions. You cannot set more than one variable in the initialization part unless you use a multiple assignment statement such as `x = y = 0`, which is possible only if all the initial values are equal. (But you can initialize additional variables by writing their assignments as separate statements preceding the `for` loop.)

The same is true of the increment part; to increment additional variables, you must write separate statements at the end of the loop. The C compound expression, using C's comma operator, would be useful in this context, but it is not supported in `awk`.

Most often, increment is an increment expression, as in the example above. But this is not required; it can be any expression whatever. For example, this statement prints all the powers of 2 between 1 and 100:


    for (i = 1; i <= 100; i *= 2)
      print i


Any of the three expressions in the parentheses following `for` may be omitted if there is nothing to be done there. Thus, `for (;x > 0;)' is equivalent to `while (x > 0)'. If the condition is omitted, it is treated as true, effectively yielding an infinite loop.

In most cases, a `for` loop is an abbreviation for a `while` loop, as shown here:


    initialization
    while (condition) { body increment
    }


The only exception is when the `continue` statement (see section [The `continue` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_11.html#SEC77)) is used inside the loop; changing a `for` statement to a `while` statement in this way can change the effect of the `continue` statement inside the loop.

There is an alternate version of the `for` loop, for iterating over all the indices of an array:


    for (i in array) do something with array[i]


See section [Arrays in `awk`](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_12.html#SEC80), for more information on this version of the `for` loop.

The `awk` language has a `for` statement in addition to a `while` statement because often a `for` loop is both less work to type and more natural to think of. Counting the number of iterations is very common in loops. It can be easier to think of this counting as part of looping rather than as something to do inside the loop.

The next section has more complicated examples of `for` loops.

## [The `break` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC76)

The `break` statement jumps out of the innermost `for`, `while`, or `do`-`while` loop that encloses it. The following example finds the smallest divisor of any integer, and also identifies prime numbers:


    awk '# find smallest divisor of num
         { num = $1
           for (div = 2; div*div <= num; div++)
             if (num % div == 0)
               break
           if (num % div == 0)
             printf "Smallest divisor of %d is %d\n", num, div
           else
             printf "%d is prime\n", num  }'


When the remainder is zero in the first `if` statement, `awk` immediately breaks out of the containing `for` loop. This means that `awk` proceeds immediately to the statement following the loop and continues processing. (This is very different from the `exit` statement (see section [The `exit` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_11.html#SEC79)) which stops the entire `awk` program.)

Here is another program equivalent to the previous one. It illustrates how the condition of a `for` or `while` could just as well be replaced with a `break` inside an `if`:


    awk '# find smallest divisor of num
         { num = $1
           for (div = 2; ; div++) {
             if (num % div == 0) {
               printf "Smallest divisor of %d is %d\n", num, div
               break
             }
             if (div*div > num) {
               printf "%d is prime\n", num
               break
             }
           }
    }'


## [The `continue` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC77)

The `continue` statement, like `break`, is used only inside `for`, `while`, and `do`-`while` loops. It skips over the rest of the loop body, causing the next cycle around the loop to begin immediately. Contrast this with `break`, which jumps out of the loop altogether. Here is an example:


    # print names that don't contain the string "ignore"

    # first, save the text of each line
    { names[NR] = $0 }

    # print what we're interested in
    END {
       for (x in names) {
           if (names[x] ~ /ignore/)
               continue
           print names[x]
       }
    }


If one of the input records contains the string `ignore', this example skips the print statement for that record, and continues back to the first statement in the loop.

This isn't a practical example of `continue`, since it would be just as easy to write the loop like this:


    for (x in names)
      if (names[x] !~ /ignore/)
        print names[x]


The `continue` statement in a `for` loop directs `awk` to skip the rest of the body of the loop, and resume execution with the increment-expression of the `for` statement. The following program illustrates this fact:


    awk 'BEGIN {
         for (x = 0; x <= 20; x++) {
             if (x == 5)
                 continue
             printf ("%d ", x)
         }
         print ""
    }'


This program prints all the numbers from 0 to 20, except for 5, for which the `printf` is skipped. Since the increment `x++` is not skipped, `x` does not remain stuck at 5. Contrast the `for` loop above with the `while` loop:


    awk 'BEGIN {
         x = 0
         while (x <= 20) {
             if (x == 5)
                 continue
             printf ("%d ", x)
             x++
         }
         print ""
    }'


This program loops forever once `x` gets to 5.

## [The `next` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC78)

The `next` statement forces `awk` to immediately stop processing the current record and go on to the next record. This means that no further rules are executed for the current record. The rest of the current rule's action is not executed either.

Contrast this with the effect of the `getline` function (see section [Explicit Input with `getline`](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_5.html#SEC28)). That too causes `awk` to read the next record immediately, but it does not alter the flow of control in any way. So the rest of the current action executes with a new input record.

At the grossest level, `awk` program execution is a loop that reads an input record and then tests each rule's pattern against it. If you think of this loop as a `for` statement whose body contains the rules, then the `next` statement is analogous to a `continue` statement: it skips to the end of the body of this implicit loop, and executes the increment (which reads another record).

For example, if your `awk` program works only on records with four fields, and you don't want it to fail when given bad input, you might use this rule near the beginning of the program:


    NF != 4 {
      printf("line %d skipped: doesn't have 4 fields", FNR) > "/dev/stderr"
      next
    }


so that the following rules will not see the bad record. The error message is redirected to the standard error output stream, as error messages should be. See section [Standard I/O Streams](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_6.html#SEC42).

The `next` statement is not allowed in a `BEGIN` or `END` rule.

## [The `exit` Statement](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_toc.html#SEC79)

The `exit` statement causes `awk` to immediately stop executing the current rule and to stop processing input; any remaining input is ignored.

If an `exit` statement is executed from a `BEGIN` rule the program stops processing everything immediately. No input records are read. However, if an `END` rule is present, it is executed (see section [`BEGIN` and `END` Special Patterns](http://www.cs.utah.edu/dept/old/texinfo/gawk/gawk_8.html#SEC55)).

If `exit` is used as part of an `END` rule, it causes the program to stop immediately.

An `exit` statement that is part an ordinary rule (that is, not part of a `BEGIN` or `END` rule) stops the execution of any further automatic rules, but the `END` rule is executed if there is one. If you don't want the `END` rule to do its job in this case, you can set a variable to nonzero before the `exit` statement, and check that variable in the `END` rule.

If an argument is supplied to `exit`, its value is used as the exit status code for the `awk` process. If no argument is supplied, `exit` returns status zero (success).

For example, let's say you've discovered an error condition you really don't know how to handle. Conventionally, programs report this by exiting with a nonzero status. Your `awk` program can do this using an `exit` statement with a nonzero argument. Here's an example of this:


    BEGIN {
        if (("date" | getline date_now) < 0) {
            print "Can't get system date" > "/dev/stderr"
            exit 4
        }
    }
