# [vim+gdb](http://blog.csdn.net/easwy/archive/2007/10/17/1828678.aspx)

本节所用命令的帮助入口：
```
:help vimgdb
```

在UNIX系 统最初设计时，有一个非常重要的思想：每个程序只实现单一的功能，通过管道等方式把多个程序连接起来，使之协同工作，以完成更强大的功能。程序只实现单一 功能，一方面降低了程序的复杂性，另一方面，也让它专注于这一功能，把这个功能做到最好。就好像搭积木一样，每个积木只提供简单的功能，但不同的积木垒在 一起，就能搭出大厦、汽车等等复杂的东西。

从UNIX系统(及其变种)的命令行就可以看出这一点，每个命令只专注于单一的功能，但通过管道、脚本等把这些命令揉合起来，就能完成复杂的任务。

VI/VIM的设计也遵从这一思想，它只提供了文本编辑功能(与Emacs的大而全刚好相反)，而且正如大家所看到的，它在这一领域做的是如此的出色。

也正因为如此，VIM自身并不提供集成开发环境所需的全部功能(它也不准备这样做，VIM只想成为一个通用的文本编辑器)。它把诸如编译、调试这样功能，交给更专业的工具去实现，而VIM只提供与这些工具的接口。

我们在前面已经介绍过VIM与编译器的接口(见quickfix主题)，VIM也提供了与调试器的接口，这一接口就是netbeans。除此之外，还可以给VIM打一个补丁，以使其支持GDB调试器。我们在本篇以及下一篇分别介绍这两种方式。

由于netbeans接口只能在gvim中使用，而打上vimgdb补丁后，无论在终端的vim，还是gvim，都可以调试。所以我更喜欢打补丁的方式，本篇先介绍这种方法。

打补丁的方式，需要重新编译VIM，刚好借这个机会，介绍一下VIM的编译方法。我只介绍Linux上编译方法，如果你想在windows上编译vim，可以参考这篇文档：[Vim: Compiling HowTo: For Windows](http://users.skynet.be/antoine.mechelynck/vim/compile.htm)。

**[** **下载 VIM** **源代码 ]**

首先我们需要下载VIM的源码。到<http://www.vim.org/sources.php>下载当前最新的VIM 7.1的源代码，假设我们把代码放到~/install/目录，文件名为vim-7.1.tar.bz2。

**[** **下载 vimgdb** **补丁 ]**

接下来，我们需要下载vimgdb补丁，下载页面在：

<http://sourceforge.net/project/showfiles.php?group_id=111038&package_id=120238>

在这里，选择vim 7.1的补丁，把它保存到~/install/vimgdb71-1.12.tar.gz。

**[** **打补丁 ]**

运行下面的命令，解压源码文件，并打上补丁：

```
cd ~/install/
tar xjf vim-7.1.tar.bz2
tar xzf vimgdb71-1.12.tar.gz
patch -d vim71 --backup -p0 < vimgdb/vim71.diff
```

**[** **定制 VIM** **的功能 ]**

缺省的VIM配置已经适合大多数人，但有些时候你可能需要一些额外的功能，这时就需要自己定制一下VIM。定制VIM很简单，进入~/install/vim71/src文件，编辑Makefile文件。这是一个注释很好的文档，根据注释来选择：

* 如果你不想编译gvim，可以打开\--disable-gui选项；

* 如果你想把perl, python, tcl, ruby等接口编译进来的话，打开相应的选项，例如，我打开了--enable-tclinterp选项；

* 如果你想在VIM中使用cscope的话，打开\--enable-cscope选项；

* 我们刚才打的vimgdb补丁，自动在Makefile中加入了\--enable-gdb选项；

* 如果你希望在vim使用中文，使能\--enable-multibyte和\--enable-xim选项；

* 可以通过\--with-features=XXX选项来选择所编译的VIM特性集，缺省是\--with-features=normal；

* 如果你没有root权限，可以把VIM装在自己的home目录，这时需要打开prefix = $(HOME)选项；

编辑好此文件后，就可以编辑安装vim了。如果你需要更细致的定制VIM，可以修改config.h文件，打开/关闭你想要的特性。

**[** **编译安装 ]**

编译和安装VIM非常简单，使用下面两个命令：
```
make
make install
```

你不需要手动运行./configure命令，make命令会自动调用configure命令。

上面的命令执行完后，VIM就安装成功了。

我在编译时打开了prefix = $(HOME)选项，因此我的VIM被安装在~/bin目录。这时需要修改一下PATH变量，以使其找到我编辑好的VIM。在~/.bashrc文件中加入下面这两句话：
```
PATH=$HOME/bin:$PATH
export PATH
```

退出再重新登录，现在再敲入vim命令，发现已经运行我们编译的VIM了。

**[** **安装 vimgdb** **的 runtime** **文件 ]**

运行下面的命令，解压vimgdb的runtime文件到你的~/.vim/目录：
```
cd ~/install/vimgdb/
tar zxf vimgdb_runtime.tgz –C~/.vim/
```

现在启动VIM，在VIM中运行下面的命令以生成帮助文件索引：
```
:helptags ~/.vim/doc
```

现在，你可以使用“:help vimgdb”命令查看vimgdb的帮助了。

至此，我们重新编译了VIM，并为之打上了vimgdb补丁。下面我以一个例子来说明如何在VIM中完成“编码—编译—调试”一条龙服务。

**[** **在 VIM** **中调试 ]**

首先确保你的计算机上安装了GDB ，Vimgdb支持5.3以上的GDB版本，不过最好使用GDB 6.0以上的版本。

我使用下面这个简单的例子，来示例一下如何在VIM中使用GDB调试。先来看示例代码：

文件~/tmp/sample.c内容如下，这是主程序，调用函数计算某数的阶乘并打印：

```
/* ~/tmp/sample.c */

#include <stdio.h>

extern int factor(int n, int *rt);

int main(int argc, char **argv)
{
    int i;
    int result = 1;

    for (i = 1; i < 6; i++)
    {
        factor(i, &result);
        printf("%d! = %d\n", i, result);
    }

    return 0;
}
```

文件~/tmp/factor/factor.c内容如下，定义了子函数factor()。之所以把它放到子目录factor/，是为了演示vim可以自动根据调试位置打开文件，不管该文件在哪个目录下：

```
/* ~/tmp/factor/factor.c */

int factor(int n, int *r)
{
    if (n <= 1)
        *r =  n;
    else
    {
        factor(n - 1, r);
        *r *= n;
    }

    return 0;
}
```

Makefile文件，用来编译示例代码，最终生成的可执行文件名为sample。
```
# ~/tmp/Makefile
sample: sample.c factor/factor.c
    gcc -g -Wall -o sample sample.c factor/factor.c
gcc -g -Wall -o sample sample.c factor/factor.c
```

假设vim的当前工作目录是~/tmp(使用“:cd ~/tmp”命令切换到此目录)。我们编辑完上面几个文件后，输入命令“:make”，vim就会根据Makefile文件进行编译。如果编译出错，VIM会跳到第一个出错的位置，改完后，用“:cnext”命令跳到下一个错误，以此类推。这种开发方式被称为quickfix，我们已经在前面的文章中讲过，不再赘述。

现在，假设已经完成链接，生成了最终的sample文件，我们就可以进行调试了。

Vimgdb补丁已经定义了一些键绑定，我们先加载这些绑定：
```
:run macros/gdb_mappings.vim
```
加载后，一些按键就被绑定为调试命令(Vimgdb定义的键绑定见“:help gdb-mappings”)。按<F7>键可以在按键的缺省定义和调试命令间切换。

好了，我们现在按空格键，在当前窗口下方会打开一个小窗口(command-line窗口)，这就是vimgdb的命令窗口，可以在这个窗口中输入任何合法的gdb命令，输入的命令将被送到gdb执行。现在，我们在这个窗口中输入“gdb”，按回车后，command-line窗口自动关闭，而在当前窗口上方又打开一个窗口，这个窗口是gdb输出窗口。现在VIM的窗口布局如下(我又按空格打开了command-line窗口)：


**_Tips_** _: command-line_ _窗口是一个特殊的窗口，在这种窗口中，你可以像编辑文本一样编辑命令，完成编辑后，按回车，就会执行此命令。你要重复执行某条命令，可以把光标移到该命令所在的行，然后按回车即可；你也可以对历史命令进行修改后再执行。详见“ :help cmdline-window_ _”。_

接下来，在command-line窗口中输入以下命令：
```
cd ~/tmp
file sample
```
这两条命令切换gdb的当前工作目录，并加载我们编译的sample程序准备调试。

现在使用VIM的移动命令，把光标移动到sample.c的第7行和14行，按“CTRL-B”在这两处设置断点，然后按“R”，使gdb运行到我们设置的第一个断点处(“CTRL-B”和“R”都是gdb_mappings.vim定义的键绑定，下面介绍的其它调试命令相同)。现在VIM看起来是这样：

断点所在的行被置以蓝色，并在行前显示标记1和2表明是第几个断点；程序当前运行到的行被置以黄色，行前以“=>”指示，表明这是程序执行的位置(显示的颜色用户可以调整)。

接下来，我们再按“C”，运行到第2个断点处，现在，我们输入下面的vim命令，在右下方分隔出一个名为gdb-variables的窗口：
```
:bel 20vsplit gdb-variables
```
然后用“v”命令选中变量i，按“CTRL-P”命令，把变量i加入到监视窗口，用同样的方式把变量result也加入到监视窗口，这里可以从监视窗口中看到变量i和result的值。

现在我们按“S”步进到factor函数，VIM会自动打开factor/factor.c文件并标明程序执行的位置。我们再把factor()函数中的变量n加入到监视窗口；然后按空格打开command-line窗口，输入下面的命令，把变量*r输入到变量窗口：
```
createvar *r
```
现在，VIM看起来是这样的：

现在，你可以用“S”、“CTRL-N”或“C”来继续执行，直至程序运行结束。

如果你是单步执行到程序结束，那么VIM最后可能会打开一个汇编窗口。是的，vimgdb支持汇编级的调试。这里我们不用进行汇编级调试，忽略即可。

如果你发现程序有错误，那么可以按“Q”退出调试(gdb会提示是否退出，回答y即可)，然后修改代码、编译、调试，直到最终完成。在修改代码时，你可能并不喜欢vimgdb的键映射(例如，它把CTRL-B映射为设置断点，而这个键又是常用的翻页功能)，你可以按<F7>取消vimgdb的键映射，或者你直接修改gdb_mappings.vim文件中定义的映射。

看，用VIM + GDB调试是不是很简单?!

我们可以再定制一下，使调试更加方便。

打开~/.vim/macros/ gdb_mappings.vim文件，在“let s:gdb_k = 0”这一行下面加上这段内容：

```
        " easwy add
        if ! exists("g:vimgdb_debug_file")
            let g:vimgdb_debug_file = ""
        elseif g:vimgdb_debug_file == ""
            call inputsave()
            let g:vimgdb_debug_file = input("File: ", "", "file")
            call inputrestore()
        endif
        call gdb("file " . g:vimgdb_debug_file)
        " easwy end
```

在“let s:gdb_k = 1”这一行下面加上这段内容：

```
       " easwy add
        call gdb("quit")
        " end easwy
```

注释掉最后一行的“call s:Toggle()”。

然后在你的vimrc中增加这段内容：

```
   """"""""""""""""""""""""""""""
   " vimgdb setting
   """"""""""""""""""""""""""""""
   let g:vimgdb_debug_file = ""
    run macros/gdb_mappings.vim
```

现在，在启动vim后，按<F7>，就进入调试模式、定义调试的键映射。在第一次进入调试模式时，会提示你输入要调试的文件名，以后就不必再输入了。再按一次<F7>，就退出调试模式，取消调试的键映射。

利用VIM的键映射机制，你可以把你喜欢的GDB命令映射为VIM的按键，方便多了。映射的例子可以参照~/.vim/macros/ gdb_mappings.vim。

再附上一张抓图，这是使用putty远程登录到linux上，在终端vim中进行调试。这也是我为什么喜欢vimgdb的原因，因为它可以在终端vim中调试，而clewn只支持gvim：

因为我不常使用GDB调试，所以本文仅举了个简单的例子，以抛砖引玉。欢迎大家共享自己的经验和心得。

最后，让我们感谢vimgdb作者xdegaye的辛勤劳动，我们下一篇会介绍clewn，这是VIM与GDB结合的另外一种形式，它和vimgdb同属一个项目。
