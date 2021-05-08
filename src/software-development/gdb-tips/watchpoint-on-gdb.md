# [Watchpoint on GDB](http://www.unknownroad.com/rtfm/gdbtut/gdbwatch.html)

[[contents](http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html)] [[usage](http://www.unknownroad.com/rtfm/gdbtut/gdbuse.html)] [[execution](http://www.unknownroad.com/rtfm/gdbtut/gdbstep.html)] [[stack](http://www.unknownroad.com/rtfm/gdbtut/gdbstack.html)] [[breakpoints](http://www.unknownroad.com/rtfm/gdbtut/gdbbreak.html)] [watchpoints] [[advanced](http://www.unknownroad.com/rtfm/gdbtut/gdbadvanced.html)]

Watchpoints are similar to breakpoints. However, watchpoints are not set for functions or lines of code. Watchpoints are set on variables. When those variables are read or written, the watchpoint is triggered and program execution stops.

It is difficult to understand watchpoint commands by themselves, so the following simple example program will be used in the command usage examples.

>
>     #include <stdio.h>
>
>     int main(int argc, char **argv)
>     {
>       int x = 30;
>       int y = 10;
>
>       x = y;
>
>       return 0;
>     }
>

### 5.1 How do I set a write watchpoint for a variable?[[top]](http://www.unknownroad.com/rtfm/gdbtut/gdbwatch.html#HOW) [[toc]](http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html)

Use the **watch** command. The argument to the watch command is an expression that is evaluated. This implies that the variabel you want to set a watchpoint on must be in the current scope. So, to set a watchpoint on a non-global variable, you must have set a breakpoint that will stop your program when the variable is in scope. You set the watchpoint after the program breaks.

*NOTE* You may notice in the example below that the line of code printed doesn't match with the line that changes the variable x. This is because the store instruction that sets off the watchpoint is the last in the sequence necessary to do the 'x=y' assignment. So the debugger has already gone on to the next line of code. In the examples, a breakpoint has been set on the 'main' function and has been triggered to stop the program.

>
>     (gdb) watch x
>     Hardware watchpoint 4: x
>     (gdb) c
>     Continuing.
>     Hardware watchpoint 4: x
>
>     Old value = -1073743192
>     New value = 11
>     main (argc=1, argv=0xbffffaf4) at test.c:10
>     10      return 0;
>




### 5.2 How do I set a read watchpoint for a variable? [[top]](http://www.unknownroad.com/rtfm/gdbtut/gdbwatch.html#HOW) [[toc]](http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html)

Use the **rwatch** command. Usage is identical to the watch command.

>
>     (gdb) rwatch y
>     Hardware read watchpoint 4: y
>     (gdb) continue
>     Continuing.
>     Hardware read watchpoint 4: y
>
>     Value = 1073792976
>     main (argc=1, argv=0xbffffaf4) at test.c:8
>     8         x = y;
>




### 5.3 How do I set a read/write watchpoint for a variable? [[top]](http://www.unknownroad.com/rtfm/gdbtut/gdbwatch.html#HOW) [[toc]](http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html)

Use the **awatch** command. Usage is identical to the watch command.




### 5.4 How do I disable watchpoints? [[top]](http://www.unknownroad.com/rtfm/gdbtut/gdbwatch.html#HOW) [[toc]](http://www.unknownroad.com/rtfm/gdbtut/gdbtoc.html)

Active watchpoints show up the breakpoint list. Use the **info breakpoints** command to get this list. Then use the **disable** command to turn off a watchpoint, just like disabling a breakpoint.

>
>     (gdb) info breakpoints
>     Num Type           Disp Enb Address    What
>     1   breakpoint     keep y   0x080483c6 in main at test.c:5
>             breakpoint already hit 1 time
>     4   hw watchpoint  keep y   x
>             breakpoint already hit 1 time
>     (gdb) disable 4
