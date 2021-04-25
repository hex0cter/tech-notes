
date: None  
author(s): None  

# [KSH 笔记 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/korn-shell/ksh-1)

Korn Shell 1.语法 特殊的文件 /etc/profile 在登录时首先自动执行。 $HOME/.profile 在登录时第二个自动执行。 $ENV 在创建一个新的KShell时指定要读的一个文件。

**文件名元字符**

* 匹配有零或零个以上字符的字符串 ? 匹配任何单个字符 [abc…] 匹配括号内任何一个字符，也可用连字符指定一个范围（例如，a-z,A-Z,0-9） [!abc…] 匹配任何不包括在括号内的字符 ?(pattern) 匹配模式的零个或一个实例 *(pattern) 匹配指定模式的零个或多个实例 ＋(pattern) 匹配指定模式的一个或多个实例 ＠(pattern) 只匹配指定模式的一个实例 ！(pattern) 匹配任何不匹配模式的字符串 \n 匹配与(…)中的第n个子模式匹配的文本。 ～ 当前用户的主目录 ～name 用户name的主目录 这个模式pattern可能是由分隔符“|”或“＆”分隔的模式的序列， 例：pr !(*.o|core) | lp

**引用**

; 命令分隔符 ＆ 后台执行 ( ) 命令分组 | 管道 & 重定向符号 * ? [ ] ~ + - @ ! 文件名元字符 ““ 中间的字符会逐字引用，除了`` 替换命令和$ 替换变量. ‘’ 中间的所有字符都会逐字引用 \ 在其后的字符会按其原来的意义逐字采用.如在””中使用 \”,\\`,\$ \a 警告，\b退格,\f 换页,\n 换行,\r 回车,\ 制表符,\v 垂直制表符, \nnn 八进制值,\xnn 十六进制值,\’ 单引号,\” 双引号,\\\ 反斜线, `` 命令的替换 $ 变量的替换

**命令形式**

Cmd & 在后台执行 Cmd1;cmd2 命令序列，依次执行 {cmd1;cmd2;} 将命令做为一组来执行 (cmd1;cmd2) 在子shell中，将命令做为一组执行 Cmd1|cmd2 管道;将cmd1的输出作为cmd2的输入 Cmd1 `cmd2` 命令替换;用cmd2的输出作为cmd1的参数 Cmd1$(cmd2) 命令替换，可以嵌套 Cmd$((expression)) 运算替换。用表达式结果作为参数 Cmd1&&cmd2 逻辑与。如果cmd1成功才执行cmd2 Cmd1||cmd2 逻辑或。如果cmd1成功则不会执行cmd2

**重定向形式**

文件描述符： 0 标准输入 stdin 默认为键盘 1 标准输出 stdout 2 标准错误 stderr Cmd > file 将cmd的结果输出到file(覆盖) Cmd >> file 将cmd的结果输出到file(追加) Cmd 从file中获取cmd 的输入 Cmd 将shell脚本的内容（直到遇见一个和text一样的标记为止）作为cmd的输入 Cmd file 在标准输入上打开文件以便读写 Cmd >&n 将输出发送到文件描述符n。ll >&1 Cmd m>&n 将本来输出的m中的内容转发到n中。Ll 3>&2 Cmd >&- 关闭标准输出 Cmd 获取输入 Cmd m Cmd 关闭标准输入 在文件描述符和一个重定向符号间不允许有空格。 Cmd 2>file 将标准错误发到file中 Cmd > file 2>&1 将标准错误和标准输出都发到file Cmd > f1 2>f2 将标准输出发到f1,标准错误发到f2 Cmd | tee files 将输出发送到标准输出和files中 Cmd 2>&1 | tee files 将输出和错误同时发到标准输出和files中

**2.变量**

  
**变量替换** 下列表达式中不允许使用空格。冒号是可选的，如果用冒号那么变量必须是非空的并设置了初始值。 Var=value… 将变量var 设为value ${var} 使用变量var的值;如果变量和其后面的文本是分开的则可以不加大括号。 ${var:-value} 如果变量var已设置则使用它，否则使用值value ${var:=value} 如果变量var已设置则使用它，否则使用值value并将value赋给变量var ${var:+value} 如果变量var已设置则使用value，否则什么也不使用 例:echo ${u-$d};echo ${tmp-`date`}如果没设tmp,则执行date;

**内置变量**

$# 命令行参数的个数 $? 上一条命令执行后返回的值 $$ 当前进程的进程号(PID), 通常用于在shell脚本中创建临时文件的名称 $0 第一个参数即命令名 $n 命令行上的第n个参数 $* 将命令行上所有参数作为一个字符串 $@ 命令行上所有参数，但每个参数都被引号引起来 LINENO 脚本或函数内正在执行的命令的行号 OLDPWD 前一个工作目录（由CD设置） PPID 当前SHELL的父进程的进程号 PWD 当前工作目录（由CD设置） RANDOM[=n] 每次引用时产生一个随机数，如果给定n则以整数n开始 SECONDS 这个整型变量的值是指从这个shell会话启动算起所过去的秒数。但它更有用的是用脚本中的计时。 例：start=$SECONDS read answer finish=$SECONDS TMOUT 如果设置了该变量，则在没有输入的情况下经过TMOUT变量所指定的秒数后，shell退出。值为0时无效。 CDPATH 允许用户使用简单文件名作为CD的参数，从而快速改变目录。设置方法与PATH类似，通常在启动文件中设置。如果CD的参数是一个绝对路径，则不会查询CDPATH. 例：CDPATH=:/u1/nr:/u1/progs: export CDPATH cd nr 就会进到nr中去。 注意：变量必须大写，定义后必须导出.

**数组**

Kshell支持一维数组，最多支持1024个元素。第一个元素为０。 Set –A name value0 value1 … 声明数组，指定的值就成为name的元素。 

${name _} i为0至1023的值，可以是表达式。返回数组元素i ${name} 返回数组元素０

${name

_

*  _},${name[@]} 返回所有元素  
下标_
*  _和[@]都可以提取整个数组的内容。但当它们在引号中使用时其行为是不同的。使用@可生成一个数组，这个数组是原始数组的副本，而使用*，则生成的仅仅是具有单一元素的数组(或者是一个普通变量)。  
例：set -A a "${names_
*  _}" set -A b "${names[@]}" set|head -5 a[0]='alex helen jenny scott' b[0]=alex b[1]=helen b[2]=jenny b[3]=scott

${#name

_
*  _} 返回数组元素个数  
**运算符** Kshell使用C语言中的运算符。 \+ 加;- 减;! 逻辑非;~ 按进制取反;* 乘;/ 除;% 求余;左移;>> 右移;小于等于;>= 大于等于;小于; > 大于;== 相等;!= 不等;&& 逻辑与;|| 逻辑或;

**3.内置命令**

# 注释后面的一行 Break [n] 从for while select until循环中退出或从n次循环中退出 Case value in Pattern1) cmds1;; Pattern2) cmds2;; … … Esac 类似于select case.例: Case $1 in No|yea) response=1 break;; -[tT]) table=TRUE;; *) echo “unknown option”;exit 1;; Esac Continue [n] 在for while select until循环中跳过余下的命令，继续下一次循环(或跳过n次循环) Eval args args是一行包含shell变量的代码.eval首先进行变量扩展，并且运行由此产生的命令。在shell变量包括了重定向符号，别名或其他变量时是有用的。 例: For option Do Case “$option” in Save) out=’ > $newfile’;; Show) out=’ | more’;; Esac Done Eval sort $file $out Exit [n] 退出脚本，退出状态为n. Export [name=[value]…] 定义全局变量，让其它shell脚本也可以使用。无参数时输出当前定义的全局变量。 For x [in list] Do Commands Done 使变量x(在可选的值列表中)执行commands，省略时假定为”$@”位置参数 例: For item in `cat program_list` Do Grep –c “$item.[co]” chap* Done Function name{commands;} 定义一个函数 If condition1 Then commands1 [elif condition2 Then commands2] … … [else commands3] Fi 条件执行语句。 Let expressions 执行一个或多个表达式。表达式中的变量前不必有$.如果表达式中包含了空格或其他特殊字符，则必须引起来。 例：let “I = I + 1” 或 let i=i+1 Read [var1[?string]] [var2 …] 从标准输入读入一行给相应的变量，并把剩余的单词给最后一个变量。String为相应的提示信息.无参时只等待一次输入。 Readonly [var1[=value] var2[=value] …] 设置只读变量,无参时显示所有只读变量 Return [n] 用于一个函数里面返回状态 repeat word do commands done 指定一个命令序列执行的次数。 例： repeat 3 do echo "bye" done Select x [in list] Do Commands Done 显示一列按list中顺序编号的菜单项。让用户键入行号选择或按return重新显示。 例: Ps3=”select thd item number:” Select event in format page view exit Do Case “event” in Format) nroff $file | lp;; Page) pr $file | lp;; View) more $file;; Exit) exit 0;; *) echo “invalid selection”;; Esac Done 输出为: 1\. format 2\. page 3\. view 4\. exit select the item number: set [options arg1 arg2 …] 无参时输出所有已知变量的值。 Shift [n] 交换位置参数（如将$2变为$1）.如果给出n,则向左移动n个位置。通常用于在while循环中迭代命令行参数。N可以是一个整数表达式。 Sleep [n] 睡眠n秒钟 Test condition 或[ condition ] 判断条件，为真返回0,否则返回非0. 文件： -a filename 如果该文件存在而为真 -d filename 如果该文件存在且为一个目录，则为真 -f filename 如果该文件存在且为一个常规文件，则为真 -L filename 如果该文件存在且为一个符号链接，为真 -r filename 如果该文件存在且用户对其有读取权限，真 -s filename 如果该文件存在且包含信息(大于0字节)，真 -w filename 如果该文件存在且对其有写入权，真 -x filename 如果该文件存在且对其有执行权，真 File1 -nt file2 如果file1存在且在file2后修改则值为真(指修改时间) File1 -ot file2 如果file1存在且在file2前修改则值为真(指修改时间) 字符串： string 如果string不为空字符串则值为真 -n string 如果string字符长度大于0则值为真 -z string 如果string字符长度等于0则值为真 string1=sting2 如果string1等于string2则值为真 string1!=string2 如果string1不等于string2则值为真 string2可以是通配符模式。 整数比较： -gt 大于；-ge 大于或等于；-eq 等于；-ne 不等于; -le 小于或等于; -lt 小于 组合： ! condition 如果condition为假则为真 condition1 –a condition2 如果两个条件都为真则为真 condition1 –o condition2 如果两个条件有一个为真则为真 trap [[commands] signals] 如果接收到任何的信号signals则执行命令commands.如果完全忽略commands则会重新设置由默认行为处理指定的信号。 例： Trap “” 2 ;忽略信号2（中断，通常是ctrl+c） Trap 2 ;恢复中断2 Trap “rm –f $tmp;exit” 0 1 2 15 ;当shell程序退出，用户退出，按ctrl+c或执行kill时删除$tmp. Typeset [options] [var [var]…]设置变量属性 -u 将变量值中所有字母全部转换成大写 -l 将变量值中所有字母全部转换成小写 -i 将变量值设为整数类型.-ix x为相应的进制，表示时为x#变量值，可用于进制转换。 例：typeset -i2 vv vv=2 echo $vv 2#10 typeset -i 相当于integer -L width 在width宽度之内左对齐 -R width 在width宽度之内右对齐，前面空位用空格填充 -Z width 在width宽度之内右对齐，变量如果是数字，则前面空位用零填充 如果忽略width,将使用赋给这个变量的第一个值的宽度。 -x 设置一个变量全局。typeset -x 相当于 export -r 设置一个变量具有只读属性，在设置的同时或之前，要先给这些变量赋值。 例：typeset -r PATH FPATH=/usr/local/funcs typeset -r 相当于 readonly 不带参数的typeset可以列出变量和变量的属性。查看指定的变量属性可用type|grep day 使用带有某一选项的typeset来看看哪一个变量具有特定的属性：typeset -z Unset var 删除一个变量，将它置为空 Until condition Do Commands Done 执行命令command直到满足条件condition. While condition Do Commands Done 如果满足条件condition则执行commands 

**本文来自ChinaUnix博客，如果查看原文请点：**<http://blog.chinaunix.net/u1/56521/showart_1094921.html>

_  
  
---

