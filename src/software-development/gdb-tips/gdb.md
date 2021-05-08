# [GDB 入门](http://blog.chinaunix.net/u/9483/showart.php?id=57476)

Debug 是大家常常用到的东西.不管是自己写程式也好,还是想改改别人写好的东西, 又或者帮人家捉捉虫.总之呢,绝对是个常常用的到的东西.Dos, windows 底下,通常大家都在用 softice. 这里我就不介绍了,因为在前面的 "学习程式"中的"Assembly"里面已经有了很详细的介绍了.这里我来说说 linux 底下的 GDB 吧.

GDB 的全称是 GNU Debuger. 是 linux 底下的一种免费的 debug 程式.随然介面不像 SoftIce 那麽好,但是功能也绝对强大.要使用 gdb 那麽首先,在你 compile 程式的时候, 要加上 -g 的选项. （可以用-g, -g2, -g3具体请看 man gcc）通常如果程式不会很大,在 compile 的时候我都是用 -g3 的,因为如果你用到了 inline 的 function, 用 -g 去 compile 就无法去 debug inline function了.这时候就用到 -g2, -g3了,g後面的数字越大,也就是说可以 debug 的级别越高.最高级别就是 -g3.

既然是入门篇,就从最简单的来做啦.先写个小程式,我们用来学习 gdb. 用你喜爱的 editor 编辑一个叫做 test.c 的文件,内容如下∶

```
int main()
{
	int a, b, c;
	a=5;
	b=10;
	b+=a;
	c=b+a;
	return 0;
}
```

然後用下面的指令去编辑这个程式∶
```
gcc -Wall -g -o test test.c
```

这样 gcc 就会 compile 一个叫做 test 的小程式.现在我们来用 gdb 看看这个小程式∶

```
gdb -q test
```

`(gdb) l`			(这里用 l 指令,是 list 的简写）

```
1       int main()
2       {
3               int a, b, c;
4               a=5;
5               b=10;
6               b+=a;
7               c=b+a;
8               return 0;
9       }
```

（这时候你就可以看到程式的 source 了）

我们现在下一个 breakpoint,这个 breakpoint 将会在第二行,也就是 2 { 这里.这样程式运行完 int main()以後,就会停下来.

```
(gdb) b 2	(b 就是 breakpoint 的简写啦)
Breakpoint 1 at 0x80483a0: file test.c, line 2.
```

现在来运行这个程式:
```
gdb) r		(r是 run 的简写)
Starting program: /home/goldencat/study-area/goldencat/gdb/test
Breakpoint 1, main () at test.c:2
```
2       {
程式运行到这里,就停下来了.因为我们在这里设下了 breakpoint.
```
(gdb)n		(n = next)
main () at test.c:4
```
4               a=5; (这里就跑到了第四行了)
```
(gdb) n
```
5               b=10;
```
(gdb) n
```
6               b+=a;
```
(gdb) n
```
7               c=b+a;
这时候我们来看看 b 的 value 是多少∶
```

(gdb) p b	(p是print的简写,这里实际写成print b)
$1 = 15		(这里显示的就是 b 的 value, 以後要看 b, 直接用 p $1 也是一样的)
		(这里的 $1 就是指向 b 的)

(gdb) n
```
8               return 0;
```
(gdb) p c
$2 = 20		(这里看到 c 的 value 是 20)
(gdb) c		(c 是 continue 的意思,也就是说执行到程式的结束)
Continuing.

Program exited normally.
(gdb) q		(这就结束 gdb 了 )
```
跟 n (next) 不同的,还有一个用法就是 step. step 很有用的就是,当你追到一个call 的时候,（如 my_function(value1)）如果用 next 会只接跑过这个 call,而不会跑到这个 call里面, step 就不同了. step 会跑到这个 call 的里面去,让你能追到 call 里面.
这里在顺便说说如何改变一个 value. 当你下指令 p 的时候,例如你用 p b, 这时候你会看到 b 的 value, 也就是上面的 $1 = 15. 你也同样可以用 p 来改变一个 value, 例如下指令 p b = 100 试试看,这时候你会发现, b 的 value 就变成 100 了∶$1 = 100.
利用display这个命令,你可以在每一次的 next 时,都显示其中一个的 value,看看下面的范例也许容易明白些∶
```
[goldencat@goldencat gdb]$ gdb -q test
(gdb) l
1       int main()
2       {
3               int a, b, c;
4               a=5;
5               b=10;
6               b+=a;
7               c=b+a;
8               return 0;
9       }
(gdb) b 2
Breakpoint 1 at 0x80483a0: file test.c, line 2.
(gdb) r
Starting program: /home/goldencat/study-area/goldencat/gdb/test

Breakpoint 1, main () at test.c:2
2       {
(gdb) n
main () at test.c:4
4               a=5;
(gdb) display a		(set display on)
1: a = 134517840
(gdb) n
5               b=10;
1: a = 5		(display a)
(gdb) n
6               b+=a;
1: a = 5		(display a)
(gdb) n
7               c=b+a;
1: a = 5		(display a)
(gdb) n
8               return 0;
1: a = 5		(display a)
(gdb) c
Continuing.

Program exited normally.
(gdb) q
```
当然你要 display 多少个 value 并没有甚麽限制.你完全可以把 a, b, c全部都display出来. 利用 info 这个指令,你可以看到目前的状况.如∶ info display 就能看到目前的display 的状况∶
```
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
1:   y  b	（这里的 y 就是说, display b 是 enable 的)
```
用 info break 就可以看到 breakpoint 的状况∶
```

(gdb) info break
Num Type           Disp Enb Address    What
1   breakpoint     keep y   0x080483a0 in main at test.c:2
        breakpoint already hit 1 time
(gdb)
```

	利用 disable 和 enable 命令,可以赞时开启和这关闭一些命令.例如∶
```

(gdb) disable display 1
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
1:   n  b		(这里看到个 n, 也就是说, display b 已经被关闭了)
(gdb)


(gdb) disable break 1
(gdb) info break
Num Type           Disp Enb Address    What
1   breakpoint     keep n   0x080483a0 in main at test.c:2
        breakpoint already hit 1 time
(gdb) 		(这里看到,breakpoint也被用 disable break 1 给关闭了)
```

如果你问我为甚麽要用 1 (disable break/display 1),看看上面的 Num 那几个字就知道了. 这里的 1 就是说关闭第一个 value. 因为当你真正 debug 的是侯,可能有很多的 break,你只要关闭你想要关闭的就好了,看看下面∶
```
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
3:   y  c
2:   y  b
1:   y  a

```
这里 display 中有三个 value, 现在我想赞时关闭对 b 的 display,可以从 Num 看出, b 的 Num 是 2,所以我们要用 disable display 2
```

(gdb) disable display 2
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
3:   y  c
2:   n  b		(这里看到, b 已经关闭了)
1:   y  a
```
如果你用 disable display 而後面没有任何的 number 的话,那麽就是 disable all 的意思∶
```
(gdb) disable display
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
3:   n  c
2:   n  b
1:   n  a
(gdb)
```
接下来说说 enable 吧, 知道了 disable, enable 就简单多了. enable 就是跟 disable 相反的意思.也就是说重新开启被关闭的东西.用法跟 disable 一样.
```
(gdb) enable display 2
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
3:   n  c
2:   y  b
1:   n  a
(gdb) enable display
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
3:   y  c
2:   y  b
1:   y  a
(gdb)
```
再来讲讲 delete 的用法啦. delete 跟 disable 不太一样,一旦被 delete, 那麽是没有办法用 enable 之类的东西找回来的.假设你 disable 一个 breakpoint,那麽就是说,你赞时不需要用到这个 break point,当你要用到的时候,只要 enable 就好.可是如果你去 delete 一个 breakpoint.就是说你将用远不需要这个 breakpoint 了.如果你下次还需要, 那麽你就给重新用 break 指令去下 breakpoint 了.
```
(gdb) delete display 1
(gdb) info display
Auto-display expressions now in effect:
Num Enb Expression
3:   y  c
2:   y  b		(1 消失了)
(gdb) delete display	(全部 delete )
Delete all auto-display expressions? (y or n) y		(要求确定一下)
(gdb) info display
There are no auto-display expressions now.	(全部的 display 都被 delete 了)
(gdb)
```
顺便说说如何去 debug 一个已经在 run 的程式∶
利用 attach process-id 和 detach 就可以去 debug 一个已经在 run 的程式了.
先用 ps aux 找出你要 debug 的程式的 process it.

```
[goldencat@goldencat gdb]$ ps aux | grep ssh
root       600  0.0  0.0  2248    0 ?        SW   11:13   0:00 [sshd]
goldenca  1182  0.0  0.7  2448  188 tty2     S    11:40   0:00 ssh 127.0.0.1
goldenca  2802  0.0  1.9  1904  528 pts/1    S    13:45   0:00 grep ssh
```

这里我们去 debug ssh 127.0.0.1 这个程式,这这程式的 process id 是 1182
```
[root@goldencat /root]# gdb -q		进入gdb

(gdb) attach 1182			截入 process 1182 到 gdb 里面
Attaching to Pid 1182
0x401b615e in ?? ()
......
......
......					进行 debug
......
......

(gdb) detach				debug 完毕以後,记得要用 detach 这个命令
Detaching from program: , Pid 1182	这个命令就把刚刚 debug 的那个程式 release
(gdb) q					掉了.
```
好啦,入门篇嘛,就写这麽多了.我写的慢,这些就写了我一个早上啦.不敢说能教了大家甚麽东西,但 也算是给没有玩过的人一个入门的概念啦.简单的,常用到的break,print, display,disable,enable,delete,run,next,step,continue好像也都说到了. 如果你有心想学,可以看看 man gdb 和进入 gdb 後,用 help 指令. GDB 里面的 help 是很好用的.
如果你是个 debug 的高手,那麽希望你也能抽点时间,跟大家分享一下你的心得.独乐乐不如众乐乐嘛. ∶）
下面是个如何使用 gdb 中的 help 的范例∶

```
[goldencat@goldencat gdb]$ gdb -q
(gdb) help
List of classes of commands:

aliases -- Aliases of other commands
breakpoints -- Making program stop at certain points
data -- Examining data
files -- Specifying and examining files
internals -- Maintenance commands
obscure -- Obscure features
running -- Running the program
stack -- Examining the stack
status -- Status inquiries
support -- Support facilities
tracepoints -- Tracing of program execution without stopping the program
user-defined -- User-defined commands

Type "help" followed by a class name for a list of commands in that class.
Type "help" followed by command name for full documentation.
Command name abbreviations are allowed if unambiguous.
(gdb) help breakpoints
Making program stop at certain points.

List of commands:

awatch -- Set a watchpoint for an expression
break -- Set breakpoint at specified line or function
catch -- Set catchpoints to catch events
clear -- Clear breakpoint at specified line or function
commands -- Set commands to be executed when a breakpoint is hit
condition -- Specify breakpoint number N to break only if COND is true
delete -- Delete some breakpoints or auto-display expressions
disable -- Disable some breakpoints
enable -- Enable some breakpoints
hbreak -- Set a hardware assisted  breakpoint
ignore -- Set ignore-count of breakpoint number N to COUNT
rbreak -- Set a breakpoint for all functions matching REGEXP
rwatch -- Set a read watchpoint for an expression
tbreak -- Set a temporary breakpoint
tcatch -- Set temporary catchpoints to catch events
thbreak -- Set a temporary hardware assisted breakpoint
txbreak -- Set temporary breakpoint at procedure exit
watch -- Set a watchpoint for an expression
xbreak -- Set breakpoint at procedure exit

Type "help" followed by command name for full documentation.
Command name abbreviations are allowed if unambiguous.
(gdb) help clear
Clear breakpoint at specified line or function.
Argument may be line number, function name, or "*" and an address.
If line number is specified, all breakpoints in that line are cleared.
If function is specified, breakpoints at beginning of function are cleared.
If an address is specified, breakpoints at that address are cleared.

With no argument, clears all breakpoints in the line that the selected frame
is executing in.

See also the "delete" command which clears breakpoints by number.
(gdb) q
```
