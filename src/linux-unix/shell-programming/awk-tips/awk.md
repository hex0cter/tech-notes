
date: None  
author(s): None  

# [awk 命令 - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/awk-tips/awk)

### 用途

在文件中查找与模式匹配的行，然后在它们上面执行特定的操作。

### 语法

awk [ [-F ](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a1049967)Ere ] [ [-v ](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a170c13f9)Assignment ] ... { [-f ](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a1049966)ProgramFile | ['Program' ](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a170c13fd)} [ [ [File ](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a170c13fc)... | [Assignment ](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a170c13fb)... ] ] ...

### 描述

awk 命令利用一组用户提供的指令来将一组文件和用户提供的扩展正则表达式比较，一次一行。然后在任何与扩展正则表达式匹配的行上执行操作。awk 处理的最大记录大小为 10KB。

awk 命令的模式搜索比 grep 命令的搜索更常用，且它允许用户在输入文本行上执行多个操作。awk 命令编程语言不需要编译，并允许用户使用变量、数字函数、字符串函数和逻辑运算符。

awk 命令受到 LANG、LC_ALL、LC_COLLATE、LC_CTYPE、LC_MESSAGES、LC_NUMERIC、NLSPATH 和 PATH 环境变量的影响。

本章中包括以下主题：

  * [awk 命令的输入](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a158c1360)
  * [awk 命令的输出](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a170c13c7)
  * [通过记录和字段的文件处理](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a158c1368)
  * [awk 命令编程语言](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a158c1371)
  * [标志](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a1049965)
  * [示例](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a1049968)



### awk 命令的输入

awk 命令采取两种类型的输入：输入文本文件和程序指令。

#### 输入文本文件

搜索和操作在输入文本文件上执行。文件如下指定：

  * 在命令行指定 File 变量。 
  * 修改特殊变量 ARGV 和 ARGC。 
  * 在未提供 File 变量的情况下提供标准输入。



如果用 File 变量指定多个文件，则文件以指定的顺序处理。

#### 程序指令

用户提供的指令控制 awk 命令的操作。这些指令来自命令行的‘Program’变量或来自用 -f 标志和 ProgramFile 变量一起指定的文件。如果指定多个程序文件，这些文件以指定的顺序串联，且使用指令的生成的顺序。

### awk 命令的输出

awk 命令从输入文本文件中的数据产生三种类型的输出：

  * 选定的数据可以打印至标准输出，此输出完全同于输入文件。 
  * 输入文件的选定部分可以更改。 
  * 选定数据可以更改并可打印至标准输出，此输出可以同于或不同于输入文件的内容。



可以在同一个文件上执行所有三种类型的输出。awk 命令识别的编程语言允许用户重定向输出。

### 通过记录和字段的文件处理

文件以下列方式处理：

  1. awk 命令扫描它的指令，并执行任何指定为在读取输入文件前发生的操作。 

awk 编程语言中的 BEGIN 语句允许用户指定在读取第一个记录前要执行的一组指令。这对于初始化特殊变量特别有用。

  2. 从输入文件读取一个记录。 

记录是由记录分隔符隔开的一组数据。记录分隔符的缺省值是换行字符，它使文件中的每一行成为一个单独的记录。记录分隔符可以通过设置 RS 特殊变量来更改。

  3. 记录是相对于 awk 命令的指令指定的每种模式比较。 

命令指令可以指定应比较记录内的特定字段。缺省情况下，字段由空白区（空格或跳格）隔开。每个字段由一个字段变量表示。记录中的第一个字段指定为 $1 变量，第二个字段指定为 $2 变量，以此类推。整个记录指定为 $0 变量。字段分隔符可以通过在命令行使用 -F 标志或通过设置 [FS 特殊变量](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a170c13eb)来更改。FS 特殊变量可以设置为下列值：空格、单个字符或[扩展正则表达式](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a10498fe)。

  4. 如果一个记录与一个模式相匹配，则任何与该模式相关的操作都在该记录上执行。 
  5. 在记录和每个模式比较且执行了所有指定操作以后，从输入读取下一个记录；在从输入文件读取所有的记录之前，该进程重复。 
  6. 如果已经指定了多个输入文件，则下一个文件打开，且在读取所有的输入文件之前，该进程重复。 
  7. 在读取了最后一个文件中的最后一个记录后，awk 命令执行任何指定为在输入处理后发生的指令。 

awk 编程语言中的 END 语句允许用户指定在读取最后一个记录后要执行的操作。这对于发送有关 awk 命令完成了什么工作的消息特别有用。




### awk 命令编程语言

awk 命令编程语言由以下格式的语句构成：

Pattern { Action }

如果一个记录与指定模式相匹配，或包含与该模式匹配的字段，则执行相关的操作。可以指定没有操作的模式，这种情况下，包含该模式的整行写至标准输出。为每个输入记录执行指定的没有模式的操作。

### 模式

在 awk 命令语言语法中使用四种类型的模式：

  * [正则表达式](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a10498fe)
  * [关系表达式](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a170c13da)
  * [模式的组合](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a171c1252)
  * [BEGIN 和 END 模式](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a171c125b)



#### 正则表达式

awk 命令使用的扩展正则表达式类似于 [grep](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/cmds/aixcmds2/grep.htm#kxf1170fish) 或 [egrep](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/cmds/aixcmds2/egrep.htm#a167z9401d) 命令使用的表达式。扩展正则表达式的最简单的形式就是包括在斜杠中的一串字符。例如，假定一个名为 `testfile` 的文件具有以下内容：
    
    
    smawley, andy
    smiley, allen
    smith, alan
    smithern, harry
    smithhern, anne
    smitters, alexis

输入以下一行命令：
    
    
    awk '/smi/' testfile

将把包含 `smi` 字符串的具体值的所有记录打印至标准输出。在这个示例中，awk 命令的程序 `'/smi/'` 是一个没有操作的模式。输出是：
    
    
    smiley, allen
    smith, alan
    smithern, harry
    smithhern, anne
    smitters, alexis

以下特殊字符用于形成扩展正则表达式：

字符 | 功能  
---|---  
+ | 指定如果一个或多个字符或扩展正则表达式的具体值（在 +（加号）前）在这个字符串中，则字符串匹配。命令行： 
    
    
    awk '/smith+ern/' testfile

将包含字符 `smit`，后跟一个或多个 `h` 字符，并以字符` ern` 结束的字符串的任何记录打印至标准输出。此示例中的输出是：
    
    
    smithern, harry
    smithhern, anne  
  
? | 指定如果零个或一个字符或扩展正则表达式的具体值（在 ?（问号）之前）在字符串中，则字符串匹配。命令行： 
    
    
    awk '/smith?/' testfile

将包含字符 `smit`，后跟零个或一个 `h` 字符的实例的所有记录打印至标准输出。此示例中的输出是：
    
    
    smith, alan
    smithern, harry
    smithhern, anne
    smitters, alexis  
  
| | 指定如果以 |（垂直线）隔开的字符串的任何一个在字符串中，则字符串匹配。命令行： 
    
    
    awk '/allen 
    | 
    alan /' testfile

将包含字符串 `allen` 或 `alan` 的所有记录打印至标准输出。此示例中的输出是：
    
    
    smiley, allen
    smith, alan  
  
( ) | 在正则表达式中将字符串组合在一起。命令行： 
    
    
    awk '/a(ll)?(nn)?e/' testfile

将具有字符串 `ae` 或 `alle` 或 `anne` 或 `allnne` 的所有记录打印至标准输出。此示例中的输出是：
    
    
    smiley, allen
    smithhern, anne  
  
{m} | 指定如果正好有 m 个模式的具体值位于字符串中，则字符串匹配。命令行： 
    
    
    awk '/l{2}/' testfile

打印至标准输出
    
    
    smiley, allen  
  
{m,} | 指定如果至少 m 个模式的具体值在字符串中，则字符串匹配。命令行： 
    
    
    awk '/t{2,}/' testfile

打印至标准输出：
    
    
    smitters, alexis  
  
{m, n} | 指定如果 m 和 n 之间（包含的 m 和 n）个模式的具体值在字符串中（其中m <= n），则字符串匹配。命令行： 
    
    
    awk '/er{1, 2}/' testfile

打印至标准输出：
    
    
    smithern, harry
    smithern, anne
    smitters, alexis  
  
[String] | 指定正则表达式与方括号内 String 变量指定的任何字符匹配。命令行： 
    
    
    awk '/sm[a-h]/' testfile

将具有 `sm` 后跟以字母顺序从 `a` 到 `h` 排列的任何字符的所有记录打印至标准输出。此示例的输出是：
    
    
    smawley, andy  
  
[^ String] | 在 [ ]（方括号）和在指定字符串开头的 ^ (插入记号) 指明正则表达式与方括号内的任何字符不匹配。这样，命令行： 
    
    
    awk '/sm[^a-h]/' testfile

打印至标准输出：
    
    
    smiley, allen
    smith, alan
    smithern, harry
    smithhern, anne
    smitters, alexis  
  
~,!~ | 表示指定变量与正则表达式匹配（代字号）或不匹配（代字号、感叹号）的条件语句。命令行： 
    
    
    awk '$1 ~ /n/' testfile

将第一个字段包含字符 `n` 的所有记录打印至标准输出。此示例中的输出是：
    
    
    smithern, harry
    smithhern, anne  
  
^ | 指定字段或记录的开头。命令行： 
    
    
    awk '$2 ~ /^h/' testfile

将把字符 `h` 作为第二个字段的第一个字符的所有记录打印至标准输出。此示例中的输出是：
    
    
    smithern, harry  
  
$ | 指定字段或记录的末尾。命令行： 
    
    
    awk '$2 ~ /y$/' testfile

将把字符 `y` 作为第二个字段的最后一个字符的所有记录打印至标准输出。此示例中的输出是：
    
    
    smawley, andy
    smithern, harry  
  
. （句号） | 表示除了在空白末尾的终端换行字符以外的任何一个字符。命令行： 
    
    
    awk '/a..e/' testfile

将具有以两个字符隔开的字符 `a` 和 e 的所有记录打印至标准输出。此示例中的输出是：
    
    
    smawley, andy
    smiley, allen
    smithhern, anne  
  
*（星号） | 表示零个或更多的任意字符。命令行： 
    
    
    awk '/a.*e/' testfile

将具有以零个或更多字符隔开的字符 `a` 和 e 的所有记录打印至标准输出。此示例中的输出是：
    
    
    smawley, andy
    smiley, allen
    smithhern, anne
    smitters, alexis  
  
\ (反斜杠) | 转义字符。当位于在扩展正则表达式中具有特殊含义的任何字符之前时，转义字符除去该字符的任何特殊含义。例如，命令行： 
    
    
    /a\/\//

将与模式 a // 匹配，因为反斜杠否定斜杠作为正则表达式定界符的通常含义。要将反斜杠本身指定为字符，则使用双反斜杠。有关反斜杠及其使用的更多信息，请参阅以下关于转义序列的内容。  
  
##### 识别的转义序列

awk 命令识别大多数用于 C 语言约定中的转义序列，以及 awk 命令本身用作特殊字符的几个转义序列。转义序列是：

转义序列 | 表示的字符  
---|---  
\" | \"（双引号）标记  
\/ | /（斜杠）字符  
\ddd | 其编码由 1、2 或 3 位八进制整数表示的字符，其中 d 表示一个八进制数位  
\\\ | \ ( 反斜杠 ) 字符  
\a | 警告字符  
\b | 退格字符  
\f | 换页字符  
\n | 换行字符（请参阅以下的注）  
\r | 回车字符  
\t | 跳格字符  
\v | 垂直跳格  
  
> 注：除了在 gsub、match、split 和 sub 内置函数中，扩展正则表达式的匹配都基于输入记录。记录分隔符字符（缺省情况下为换行字符）不能嵌套在表达式中，且没与记录分隔符字符匹配的表达式。如果记录分隔符不是换行字符，则可与换行字符匹配。在指定的四个内置函数中，匹配基于文本字符串，且任何字符（包含记录分隔符）可以嵌套在模式中，这样模式与适当的字符相匹配。然而，用 awk 命令进行的所有正则表达式匹配中，在模式使用一个或多个 NULL（空）字符将生成未定义的结果。

#### 关系表达式

关系运算符 <（小于）、>（大于）、<=（小于或等于）、>=（大于或等于）、= =（等于）和 !=（不等于）可用来形成模式。例如，模式：
    
    
    $1 < $4

将与第一个字段小于第四个字段的记录匹配。关系运算符还和字符串值一起使用。例如：
    
    
    $1 =! "q"

将与第一个字段不是 `q` 的所有记录匹配。字符串值还可以根据校对值匹配。例如：
    
    
    $1 >= "d"

将与第一个字段以字符 `a`、`b`、`c` 或 `d` 开头的所有记录匹配。如果未给出其它信息，则字段变量作为字符串值比较。

#### 模式的组合

可以使用三种选项组合模式：

  * 范围由两种以 ,（逗号）隔开的模式指定。操作在每个以匹配第一个模式的记录开始的每个记录上执行，并通过匹配第二个模式的记录（包含此记录）继续。例如： 
    
        /begin/,/end/

与包含字符串 `begin` 的记录以及该记录和包含字符串 `end` 之间的所有记录（包含包括字符串 `end` 的记录）匹配。

  * 括号 ( ) 将模式组合在一起。 
  * 布尔运算符 ||（或）&&（和）以及 !（不）将模式组合成如果它们求值为真则匹配，否则不匹配的表达式。例如，模式： 
    
        $1 == "al" && $2 == "123"

与第一个字段是 `al` 且第二个字段是 `123` 的记录匹配。




#### BEGIN 和 END 模式

用 BEGIN 模式指定的操作在读取任何输入之前执行。用 END 模式指定的操作在读取了所有输入后执行。允许多个 BEGIN 和 END 模式，并以指定的顺序处理它们。在程序语句中 END 模式可以在 BEGIN 模式之前。如果程序仅由 BEGIN 语句构成，则执行操作且不读取输入。如果程序仅由 END 语句构成，则在任何操作执行前读取所有输入。

### 操作

有多种类型的操作语句：

  * [操作语句](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a171c1264)
  * [内置函数](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a171c1266)
  * [用户定义的函数](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a171c1334)
  * [条件语句](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a172c1f91)
  * [输出操作](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a172c1fa6)



#### 操作语句

操作语句括在 { } (花括号) 中。如果语句指定为没有模式，则它们在每个记录上执行。在括号里可以指定多个操作，但操作间必须以换行字符或 ;（分号）分隔，且语句以它们出现的顺序处理。操作语句包含：

算术语句  
---  
算术运算符 +（加号）, - （减号）, / （除号）, ^ (幂), * （乘号）, % （系数）用于格式： 
    
    
    表达式 运算符 表达式

这样，语句：
    
    
    $2 = $1 ^ 3

将第一个升为三次方的字段的值指定给第二个字段。  
  
一元语句  
---  
一元 -（减号）和一元 +（加号）如在 C 编程语言中操作： 
    
    
    +Expression 或 -Expression  
  
增量和减量语句  
---  
增量前语句和减量前语句如在 C 编程语言中操作： 
    
    
    ++Variable 或 --Variable

增量后语句和减量后语句如在 C 编程语言中操作：
    
    
    Variable++ 或 Variable--  
  
赋值语句  
---  
赋值运算符 +=（加）、-=（减）、/=（除）和 *=（乘）如在 C 编程语言中操作，格式为： 
    
    
    Variable += Expression
    
    
    Variable -= Expression
    
    
    Variable /= Expression
    
    
    Variable *= Expression

例如，语句：
    
    
    $1 *= $2

将字段变量 $1 乘以字段变量 $2，然后将新值指定给 $1。

赋值运算符 ^=（幂）和 %=（系数）具有以下格式：
    
    
    Variable1^=Expression1

和
    
    
    Variable2%=Expression2

并且它们等同于 C 编程语言语句：
    
    
    Variable1=pow(Variable1, Expression1)

和
    
    
    Variable2=fmod(Variable2, Expression2)

其中 `pow` 是 [pow](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/libs/basetrf1/powf.htm) 子例程而 `fmod` 是 [fmod](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/libs/basetrf1/fmodf.htm) 子例程。  
  
字符串串联语句  
---  
字符串值可以通过紧挨着陈述来串联。例如： 
    
    
    $3 = $1 $2

将字段变量 $1 和 $2 中的字符串的串联指定给字段变量 $3。  
  
#### 内置函数

awk 命令语言使用算术函数、字符串函数和一般函数。如果打算编写一个文件，且稍后在同一个程序里读取它，则 close 子例程语句是必需的。

##### 算术函数

以下算术函数执行与 C 语言中名称相同的子例程相同的操作：

atan2( y, x ) | 返回 y/x 的反正切。  
---|---  
cos( x ) | 返回 x 的余弦；x 是弧度。  
sin( x ) | 返回 x 的正弦；x 是弧度。  
exp( x ) | 返回 x 幂函数。  
log( x ) | 返回 x 的自然对数。  
sqrt( x ) | 返回 x 平方根。  
int( x ) | 返回 x 的截断至整数的值。  
rand( ) | 返回任意数字 n，其中 0 <= n < 1。  
srand( [Expr] ) | 将 rand 函数的种子值设置为 Expr 参数的值，或如果省略 Expr 参数则使用某天的时间。返回先前的种子值。  
  
##### 字符串函数

字符串函数是：

gsub( Ere, Repl, [ In ] ) | 除了正则表达式所有具体值被替代这点，它和 sub 函数完全一样地执行，。  
---|---  
sub( Ere, Repl, [ In ] ) | 用 Repl 参数指定的字符串替换 In 参数指定的字符串中的由 Ere 参数指定的扩展正则表达式的第一个具体值。sub 函数返回替换的数量。出现在 Repl 参数指定的字符串中的 &（和符号）由 In 参数指定的与 Ere 参数的指定的扩展正则表达式匹配的字符串替换。如果未指定 In 参数，缺省值是整个记录（$0 记录变量）。  
index( String1, String2 ) | 在由 String1 参数指定的字符串（其中有出现 String2 指定的参数）中，返回位置，从 1 开始编号。如果 String2 参数不在 String1 参数中出现，则返回 0（零）。  
length [(String)] | 返回 String 参数指定的字符串的长度（字符形式）。如果未给出 String 参数，则返回整个记录的长度（$0 记录变量）。  
blength [(String)] | 返回 String 参数指定的字符串的长度（以字节为单位）。如果未给出 String 参数，则返回整个记录的长度（$0 记录变量）。  
substr( String, M, [ N ] ) | 返回具有 N 参数指定的字符数量子串。子串从 String 参数指定的字符串取得，其字符以 M 参数指定的位置开始。M 参数指定为将 String 参数中的第一个字符作为编号 1。如果未指定 N 参数，则子串的长度将是 M 参数指定的位置到 String 参数的末尾 的长度。  
match( String, Ere ) | 在 String 参数指定的字符串（Ere 参数指定的扩展正则表达式出现在其中）中返回位置（字符形式），从 1 开始编号，或如果 Ere 参数不出现，则返回 0（零）。RSTART 特殊变量设置为返回值。RLENGTH 特殊变量设置为匹配的字符串的长度，或如果未找到任何匹配，则设置为 -1（负一）。  
split( String, A, [Ere] ) | 将 String 参数指定的参数分割为数组元素 A[1], A[2], . . ., A[n]，并返回 n 变量的值。此分隔可以通过 Ere 参数指定的扩展正则表达式进行，或用当前字段分隔符（FS 特殊变量）来进行（如果没有给出 Ere 参数）。除非上下文指明特定的元素还应具有一个数字值，否则 A 数组中的元素用字符串值来创建。  
tolower( String ) | 返回 String 参数指定的字符串，字符串中每个大写字符将更改为小写。大写和小写的映射由当前语言环境的 LC_CTYPE 范畴定义。  
toupper( String ) | 返回 String 参数指定的字符串，字符串中每个小写字符将更改为大写。大写和小写的映射由当前语言环境的 LC_CTYPE 范畴定义。  
sprintf(Format, Expr, Expr, . . . ) | 根据 Format 参数指定的 [printf](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/libs/basetrf1/printf.htm#a8zed0gaco) 子例程格式字符串来格式化 Expr 参数指定的表达式并返回最后生成的字符串。  
  
##### 一般函数

一般函数是：

close( Expression ) | 用同一个带字符串值的 Expression 参数来关闭由 print 或 printf 语句打开的或调用 getline 函数打开的文件或管道。如果文件或管道成功关闭，则返回 0；其它情况下返回非零值。如果打算写一个文件，并稍后在同一个程序中读取文件，则 close 语句是必需的。  
---|---  
system(Command ) | 执行 Command 参数指定的命令，并返回退出状态。等同于 [system](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/libs/basetrf2/system.htm#a181929c) 子例程。  
Expression | getline [ Variable ] | 从来自 Expression 参数指定的命令的输出中通过管道传送的流中读取一个输入记录，并将该记录的值指定给 Variable 参数指定的变量。如果当前未打开将 Expression 参数的值作为其命令名称的流，则创建流。创建的流等同于调用 [popen](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/libs/basetrf1/popen.htm#sk62b0shad) 子例程，此时 Command 参数取 Expression 参数的值且 Mode 参数设置为一个是 r 的值。只要流保留打开且 Expression 参数求得同一个字符串，则对 getline 函数的每次后续调用读取另一个记录。如果未指定 Variable 参数，则 $0 记录变量和 NF 特殊变量设置为从流读取的记录。  
getline [ Variable ] < Expression | 从 Expression 参数指定的文件读取输入的下一个记录，并将 Variable 参数指定的变量设置为该记录的值。只要流保留打开且 Expression 参数对同一个字符串求值，则对 getline 函数的每次后续调用读取另一个记录。如果未指定 Variable 参数，则 $0 记录变量和 NF 特殊变量设置为从流读取的记录。  
getline [ Variable ] | 将 Variable 参数指定的变量设置为从当前输入文件读取的下一个输入记录。如果未指定 Variable 参数，则 $0 记录变量设置为该记录的值，还将设置 NF、NR 和 FNR 特殊变量。  
  
> 注：所有 getline 函数的格式对于成功输入返回 1，对于文件结束返回零，对于错误返回 -1。

#### 用户定义的函数

用户定义的函数以下列格式说明：
    
    
    function Name (Parameter, Parameter,...)  { Statements }

函数可以指向 awk 命令程序中的任何位置，且它的使用可以优先于它的定义。此函数的作用域是全局的。

函数参数可以是标量或数组。参数名称对函数而言是本地的；所有其它变量名称都是全局的。同一个名称不应用作不同的实体；例如，一个参数名称不能用作函数名称又用作特殊变量。具有全局作用域的变量不应共享一个函数的名称。同个作用域中的标量和数组不应具有同一个名称。

函数定义中的参数数量不必和调用函数时使用的参数数量匹配。多余的形式参数可用作本地变量。额外的标量参数初始化后具有等同于空字符串和数字值为 0（零）的字符串值；额外的数组参数初始化为空数组。

当调用函数时，函数名称和左括号之间没有空格。函数调用可以是嵌套的或循环的。从任何嵌套的或循环函数函数调用返回时，所有调用函数的参数的值应保持不变，除了引用传送的数组参数。return 语句可用于返回一个值。

在函数定义内，在左 { ( 花括号 ) 之前和右 } ( 花括号 ) 之后的换行字符是可选的。

函数定义的一个示例是：
    
    
    function average ( g,n) 
      {
            for (i in g)
               sum=sum+g[i]
            avg=sum/n
            return avg
      } 

数组 `g` 和变量 `n` 以及数组中的元素个数传递给函数 average。然后函数获得一个平均值并返回它。

#### 条件语句

awk 命令编程语言中的大部分条件语句和 C 编程语言中的条件语句具有相同的语法和功能。所有条件语句允许使用｛ } (花括号) 将语句组合在一起。可以在条件语句的表达式部分和语句部分之间使用可选的换行字符，且换行字符或 ;（分号）用于隔离 { } (花括号) 中的多个语句。C 语言中的六种条件语句是：

if | 需要以下语法： 

if ( Expression ) { Statement } [ else Action ]  
  
---|---  
while | 需要以下语法： 

while ( Expression ) { Statement }  
  
for | 需要以下语法： 

for ( Expression ; Expression ; Expression ) { Statement }  
  
break | 当 break 语句用于 while 或 for 语句时，导致退出程序循环。  
continue | 当 continue 语句用于 while 或 for 语句时，使程序循环移动到下一个迭代。  
  
awk 命令编程语言中的五种不遵循 C 语言规则的条件语句是：

for...in | 需要以下语法： 

for ( Variable in Array ) { Statement }

for...in 语句将 Variable 参数设置为 Array 变量的每个索引值，一次一个索引且没有特定的顺序，并用每个迭代来执行 Statement 参数指定的操作。请参阅 delete 语句以获得 for...in 语句的示例。  
  
---|---  
if...in | 需要以下语法： 

if ( Variable in Array ) { Statement }

if...in 语句搜索是否存在的 Array 元素。如果找到 Array 元素，就执行该语句。  
  
delete | 需要以下语法： 

delete Array [ Expression ]

delete 语句删除 Array 参数指定的数组元素和 Expression 参数指定的索引。例如，语句：
    
    
    for (i in g)
       delete g[i];

将删除 `g[]` 数组的每个元素。  
  
exit | 需要以下语法： 

exit [Expression]

exit 语句首先调用所有 END 操作（以它们发生的顺序），然后以 Expression 参数指定的退出状态终止 awk 命令。如果 exit 语句在 END 操作中出现，则不调用后续 END 操作。  
  
# | 需要以下语法： 

# Comment

# 语句放置注释。注释应始终以换行字符结束，但可以在一行上的任何地方开始。  
  
next | 停止对当前输入记录的处理，从下一个输入记录继续。  
  
#### 输出语句

awk 命令编程语言的两种输出语句是：

print | 需要以下语法： 

print [ ExpressionList ] [ Redirection ] [ Expression ]

print 语句将 ExpressionList 参数指定的每个表达式的值写至标准输出。每个表达式由 OFS 特殊变量的当前值隔开，且每个记录由 ORS 特殊变量的当前值终止。

可以使用 Redirection 参数重定向输出，此参数可指定用 >（大于号）、>>（双大于号）和 |（管道）进行的三种输出重定向。Redirection 参数指定如何重定向输出，而 Expression 参数是文件的路径名称（当 Redirection 参数是 > 或 >> 时）或命令的名称（当 Redirection 参数是 | 时）。  
  
---|---  
printf | 需要以下语法： 

printf Format [ , ExpressionList ] [ Redirection ] [ Expression ]

printf 语句将 ExpressionList 参数指定的表达式以 Format 参数指定的格式写至标准输出。除了 `c` 转换规范（%c）不同外，printf 语句和 [printf](http://study.chyangwa.com/IT/AIX/aixcmds1/zh_CN/cmds/aixcmds4/printf.htm#a94c12) 命令起完全相同的作用。Redirection 和 Expression 参数与在 print 语句中起相同的作用。

对于 `c` 转换规范：如果自变量具有一个数字值，则编码是该值的字符将输出。如果值是零或不是字符集中的任何字符的编码，则行为未定义。如果自变量不具有数字值，则输出字符串值的第一个字符；如果字符串不包含任何字符，则行为未定义。  
  
> 注：如果 Expression 参数为 Redirection 参数指定一个路径名称，则 Expression 参数将括在双引号中以确保将它当作字符串对待。

### 变量

变量可以是标量、字段变量、数组或特殊变量。变量名称不能以数字开始。

变量可仅用于引用。除了函数参数以外，它们没有明确说明。未初始化的标量变量和数组元素具有一个为 0（零）的数字值和一个为空字符串（" "）的字符串值。

根据上下文，变量呈现出数字或字符串值。每个变量可以具有数字值和／或字符串值。例如：
    
    
    x = "4" + "8"

将值 `12` 指定给变量 `x`。对于字符串常量，表达式应括在 " "（双引号）标记中。

数字和字符串间没有显式转换。要促使将表达式当作一个数字，向它添加 0（零）。要促使将表达式当作一个字符串，则添加一个空字符串（" "）。

#### 字段变量

字段变量由 $（美元符号）后跟一个数字或数字表达式来表示。记录中的第一个字段指定为 $1 变量，第二个字段指定为 $2，以次类推。$0 字段变量指定给整个记录。新字段可以通过指定一个值给它们来创建。将一个值指定给不存在的字段（即任何大于 $NF 字段变量的当前值的字段）将促使创建任何干扰字段（指定为空字符串），增加 NF 特殊变量的值，并促使重新计算 $0 记录变量。新字段由当前字段分隔符（FS 特殊变量的值）隔开。空格和跳格是缺省字段分隔符。要更改字段分隔符，请使用 -F 标志或 在 awk 命令程序中为 FS 特殊变量指定另一个值。

#### 数组

数组初始为空且它们大小可动态更改。数组由一个变量和在 [ ]（方括号）中的下标来表示。下标或元素标识符可以是几个字符串，它们提供了一种相关数组能力。例如，程序：
    
    
    /red/  { x["red"]++ }
    /green/ { y["green"]++ }

增加 `red` 计数器和 `green` 计数器的计数。

数组可以用一个以上的下标来建立索引，类似于一些编程语言中的多维数组。因为 awk 命令的编程数组实际上是一维的，通过串联各独立表达式的字符串值（每个表达式由 SUBSEP 环境变量的值隔开）来将以逗号隔开的下标转换为单个字符串。所以，以下两个索引操作是等同的：
    
    
    x[expr1, expr2,...exprn]

和
    
    
    x[expr1SUBSEPexpr2SUBSEP...SUBSEPexprn]

当使用 in 运算符时，一个多维 Index 值应包含在圆括号之中。除了 in 运算符，任何对不存在数组元素的引用将自动创建该元素。

### 特殊变量

以下变量对于 awk 命令具有特殊含义：

ARGC | ARGV 数组中的元素个数。此值可以更改。  
---|---  
ARGV | 其每个成员包含 File 变量之一或 Assignment 变量之一的数组按序从命令行取出，并从 0（零）编号至 ARGC -1。当每个输入文件完成时，ARGV 数组的下一个成员提供下一个输入文件的名称，除非： 

  * 下一个成员是 Assignment 语句，这种情况下对赋值求值。 
  * 下一个成员具有空值，这种情况下跳过该成员。程序可以通过设置 ARGV 数组的包含该输入文件的成员设置为一个空值来跳过所选的输入文件。 
  * 下一个成员是 ARGV [ARGC -1] 的当前值，awk 命令将此成员解释为输入文件的末尾。

  
CONVFMT | 将数字转换为字符串的 printf 格式（除了使用 OFMT 特殊变量的输出语句）。缺省值为“%.6g”。  
ENVIRON | 表示运行 awk 命令的环境的数组。该数组的每个元素在以下格式中： 

ENVIRON [ "Environment VariableName" ] = EnvironmentVariableValue

当 awk 命令开始执行时设置这些值，且到执行结束前一直使用该环境，不考虑 ENVIRON 特殊变量的任何修改。  
  
FILENAME | 当前输入文件的路径名称。在执行 BEGIN 操作的过程中，FILENAME 的值未定义。在执行 END 操作的过程中，该值是处理的最后一个输入文件的名称。  
FNR | 当前文件中的当前输入记录的个数。  
FS | 输入字段分隔符。缺省值是空格。如果输入字段分隔符是空格，则任何数目的语言环境定义的空格可以分隔字段。FS 特殊变量可以有两种附加的值： 

  * 如果 FS 设置为单个字符，则字段由该字符的每个单个具体值隔开。 
  * 如果 FS 设置为一个[扩展正则表达式](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a10498fe)，则字段由与扩展正则表达式匹配的每个序列的具体值隔开。

  
NF | 当前记录中的字段个数，最大数 99 个。在 BEGIN 操作中，除非先前发出不带 Variable 参数的 getline 函数，否则 NF 特殊变量未定义。在 END 操作中，除非在输入 END 操作之前发出不带 Variable 参数的后续的、重定向的 getline 函数，否则 NF 特殊变量保留它为读取的最后一个记录而具有的值。  
NR | 当前输入记录的个数。在 BEGIN 操作中，NR 特殊变量的值是 0（零）。在 END 操作中，值是最后处理的记录的编号。  
OFMT | 在输出语句中将数字转换为字符串的 printf 格式。缺省值为“%.6g”。  
OFS | 输出字段分隔符（缺省值是空格）。  
ORS | 输出记录分隔符（缺省值是换行字符）。  
RLENGTH | 由 match 函数来匹配的字符串的长度。  
RS | 输入记录分隔符（缺省值是换行字符）。如果 RS 特殊变量为空，则记录以一个或多个空行的序列隔开；第一个空行或最后一个空行在输入的开始和结束都不会产生空记录；换行字符始终是一个字段分隔符，不考虑 FS 特殊变量的值。  
RSTART | 由 match 函数来匹配的字符串的起始位置，从 1 开始编号。等同于 match 函数的返回值。  
SUBSEP | 隔开多个下标。缺省值是 \031。  
  
### 标志

-f ProgramFile | 从 ProgramFile 变量指定的文件获取 awk 命令的指令。如果多次指定 -f 标志，则文件的串联（按指定的顺序）将用作指令集。  
---|---  
-F Ere | 请使用 Ere 变量指定的扩展正则表达式作为字段分隔符。缺省字段分隔符是空格。  
-v Assignment | 将值指定给 awk 命令编程语言的变量。Assignment 参数的格式是 Name = Value。Name 部分指定变量的名称并可以是任何下划线、数字或字母字符的组合，但它必须以字母字符或下划线开头。Value 部分也由下划线、数字和字母数字组成，且前面和后面都有一个 "（双引号字符，类似于字符串值）。如果 Value 部分是数字，则也将为变量指定数字值。 

-v 标志指定的赋值在执行 awk 命令程序的任何部分之前发生，包含 BEGIN 节。  
  
Assignment | 将值指定给 awk 命令编程语言的变量。该值和带有 -v 标志的 Assignment 变量具有相同的格式和功能（除了两者处理的时间不同以外）。Assignment 参数在处于命令行时跟在其后的输入文件（由 File 变量指定）之前处理。如果指定 Assignment 参数仅优先于多个输入文件的第一个，则赋值在 BEGIN 节后（如果有）就处理。如果 Assignment 参数出现在最后一个文件后，则在 END 节（如果有）之前处理赋值。如果不指定输入文件，则当读取了标准输入时处理赋值。  
File | 指定包含要处理的输入的文件的名称。如果不指定 File 变量，或指定了 -（减号），则处理标准输入。  
'Program' | 包含 awk 命令的指令。如果不指定 -f 标志，Program 变量应该是命令行上的第一个项。它应括在 ' '（单引号）中。  
  
### 退出状态

该命令返回以下出口值：

可以通过使用 [exit [ Expression ]](http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm#a172c1fa2) 条件语句来更改程序中的退出状态。

### 示例

  1. 要显示长于 72 个字符的文件的行，请输入： 
    
        awk  'length  >72'  chapter1

这选择 `chapter1` 文件中长于 72 个字符的每一行，并将这些行写至标准输出，因为未指定 Action。制表符以 1 个字符计数。

  2. 要显示字 `start` 和 `stop` 之间的所有行，包含`“start”`和`“stop”`，请输入： 
    
        awk  '/start/,/stop/'  chapter1

  3. 要运行一个处理文件 `chapter1` 的 awk 命令程序 `sum2.awk`，请输入： 
    
        awk  -f  sum2.awk  chapter1

以下程序 `sum2.awk`，计算了输入文件 `chapter1` 中的第二列的数字的总和与平均值：
    
            {
           sum += $2
        }
    END {
           print "Sum: ", sum;
           print "Average:", sum/NR;
        }

第一个操作将每行的第二个字段的值添加至变量 `sum`。当第一次被引用时，所有的变量都初始化为数字值 0（零）。第二个操作前的模式 END 使那些操作在读取了所有输入文件之后才执行。用于计算平均值的 NR 特殊变量是一个指定已经读取的记录的个数的特殊变量。

  4. 要以相反顺序打印前两个字段，请输入： 
    
        awk '{ print $2, $1 }' chapter1

  5. 以下 awk 程序 
    
        awk -f sum3.awk chapter2
    

打印文件 `chapter2` 的前两个字段（用逗号和／或空格和制表符隔开），然后合计第一列，并打印总和与平均值： 
    
        BEGIN  {FS = ",|[ \t]+"}
           {print $1, $2}
           {s += $1}
    END    {print "sum is",s,"average is", s/NR }               

<http://study.chyangwa.com/IT/AIX/aixcmds1/awk.htm>


