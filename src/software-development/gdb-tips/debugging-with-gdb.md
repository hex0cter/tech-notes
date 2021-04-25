
date: None  
author(s): None  

# [Debugging with GDB - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/gdb-tips/debugging-with-gdb)

<http://www.delorie.com/gnu/docs/gdb/gdb.1.html>

[](http://www.delorie.com/gnu/docs/gdb/gdb.1.html)Find more at: <http://www.delorie.com/gnu/docs/gdb/gdb.html>  


_Continuing_ means resuming program execution until your program completes normally. In contrast, _stepping_ means executing just one more "step" of your program, where "step" may mean either one line of source code, or one machine instruction (depending on what particular command you use). Either when continuing or when stepping, your program may stop even sooner, due to a breakpoint or a signal. (If it stops due to a signal, you may want to use `handle`, or use  `signal 0' to resume execution. See section [Signals](http://www.delorie.com/gnu/docs/gdb/gdb_39.html).)

`continue [ignore-count]`
    
`c [ignore-count]`
    
`fg [ignore-count]`
    Resume program execution, at the address where your program last stopped; any breakpoints set at that address are bypassed. The optional argument ignore-count allows you to specify a further number of times to ignore a breakpoint at this location; its effect is like that of `ignore` (see section [Break conditions](http://www.delorie.com/gnu/docs/gdb/gdb_34.html)).

The argument ignore-count is meaningful only when your program stopped due to a breakpoint. At other times, the argument to `continue` is ignored.

The synonyms `c` and `fg` (for _foreground_ , as the debugged program is deemed to be the foreground program) are provided purely for convenience, and have exactly the same behavior as `continue`.

To resume execution at a different place, you can use `return` (see section [Returning from a function](http://www.delorie.com/gnu/docs/gdb/gdb_121.html)) to go back to the calling function; or `jump` (see section [Continuing at a different address](http://www.delorie.com/gnu/docs/gdb/gdb_119.html)) to go to an arbitrary location in your program.

A typical technique for using stepping is to set a breakpoint (see section [Breakpoints; watchpoints; and catchpoints](http://www.delorie.com/gnu/docs/gdb/gdb_28.html)) at the beginning of the function or the section of your program where a problem is believed to lie, run your program until it stops at that breakpoint, and then step through the suspect area, examining the variables that are interesting, until you see the problem happen.

`step`
    Continue running your program until control reaches a different source line, then stop it and return control to GDB. This command is abbreviated `s`.

>  _Warning:_ If you use the `step` command while control is within a function that was compiled without debugging information, execution proceeds until control reaches a function that does have debugging information. Likewise, it will not step into a function which is compiled without debugging information. To step through functions without debugging information, use the `stepi` command, described below.

The `step` command only stops at the first instruction of a source line. This prevents the multiple stops that could otherwise occur in `switch` statements, `for` loops, etc. `step` continues to stop if a function that has debugging information is called within the line. In other words, `step` _steps inside_ any functions called within the line.

Also, the `step` command only enters a function if there is line number information for the function. Otherwise it acts like the `next` command. This avoids problems when using `cc -gl` on MIPS machines. Previously, `step` entered subroutines if there was any debugging information about the routine.

`step count`
    Continue running as in `step`, but do so count times. If a breakpoint is reached, or a signal not related to stepping occurs before count steps, stepping stops right away.
`next [count]`
    Continue to the next source line in the current (innermost) stack frame. This is similar to `step`, but function calls that appear within the line of code are executed without stopping. Execution stops when control reaches a different line of code at the original stack level that was executing when you gave the `next` command. This command is abbreviated `n`.

An argument count is a repeat count, as for `step`.

The `next` command only stops at the first instruction of a source line. This prevents multiple stops that could otherwise occur in `switch` statements, `for` loops, etc.

`set step-mode`
    
`set step-mode on`
    The `set step-mode on` command causes the `step` command to stop at the first instruction of a function which contains no debug line information rather than stepping over it.

This is useful in cases where you may be interested in inspecting the machine instructions of a function which has no symbolic info and do not want GDB to automatically skip over this function.

`set step-mode off`
    Causes the `step` command to step over any functions which contains no debug information. This is the default.
`finish`
    Continue running until just after function in the selected stack frame returns. Print the returned value (if any).

Contrast this with the `return` command (see section [Returning from a function](http://www.delorie.com/gnu/docs/gdb/gdb_121.html)).

`until`
    
`u`
    Continue running until a source line past the current line, in the current stack frame, is reached. This command is used to avoid single stepping through a loop more than once. It is like the `next` command, except that when `until` encounters a jump, it automatically continues execution until the program counter is greater than the address of the jump.

This means that when you reach the end of a loop after single stepping though it, `until` makes your program continue execution until it exits the loop. In contrast, a `next` command at the end of a loop simply steps back to the beginning of the loop, which forces you to step through the next iteration.

`until` always stops your program if it attempts to exit the current stack frame.

`until` may produce somewhat counterintuitive results if the order of machine code does not match the order of the source lines. For example, in the following excerpt from a debugging session, the `f` (`frame`) command shows that execution is stopped at line `206`; yet when we use `until`, we get to line `195`:

|  | 
    
    
    (gdb) f
    #0 main (argc=4, argv=0xf7fffae8) at m4.c:206
    206 expand_input();
    (gdb) until
    195 for ( ; argc > 0; NEXTARG) {
      
  
---|---  
  
This happened because, for execution efficiency, the compiler had generated code for the loop closure test at the end, rather than the start, of the loop--even though the test in a C `for`-loop is written before the body of the loop. The `until`command appeared to step back to the beginning of the loop when it advanced to this expression; however, it has not really gone to an earlier statement--not in terms of the actual machine code.

`until` with no argument works by means of single instruction stepping, and hence is slower than `until` with an argument.

`until location`
    
`u location`
    Continue running your program until either the specified location is reached, or the current stack frame returns. location is any of the forms of argument acceptable to `break` (see section [Setting breakpoints](http://www.delorie.com/gnu/docs/gdb/gdb_29.html)). This form of the command uses breakpoints, and hence is quicker than `until` without an argument.
`stepi`
    
`stepi arg`
    
`si`
    Execute one machine instruction, then stop and return to the debugger.

It is often useful to do `display/i $pc' when stepping by machine instructions. This makes GDB automatically display the next instruction to be executed, each time your program stops. See section [Automatic display](http://www.delorie.com/gnu/docs/gdb/gdb_57.html).

An argument is a repeat count, as in `step`.

`nexti`
    
`nexti arg`
    
`ni`
    Execute one machine instruction, but if it is a function call, proceed until the function returns.

An argument is a repeat count, as in `next`.

