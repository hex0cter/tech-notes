# [Browse source code with emacs plus cscope on Linux](http://lifegoo.pluskid.org/wiki/EmacsCscope.html)

1. install emacs and cscope.

E.g., on Ubuntu, run
```
sudo apt-get install cscope
```

2. add
```
(require 'xcscope)
```

into `~/.emacs`. Also make sure the file **xcscope.el** is under load-path.

2. cd source code path.

E.g.,
```
cd /home/daniel/Desktop/linux-2.6.31.5
```

3. Generate the symbol tables with the following commands:
```
 find . -name "*.h" -o -name "*.c" -o -name "*.cpp" | xargs etags
 find . -name "*.h" -o -name "*.c" -o -name "*.cpp" > cscope.files
 cscope -Rbkq -i cscope.files 2>/dev/null
```

4. Start emacs with a file name to open it directly. Or

Set default editor to emacs:
```
export EDITOR=emacs
```

then start cscope:
```
cscope -d
```

**TIPS:**

1) Use CTRL+d to exit cscope; CTRL+X CTRL+C to exist emacs.

2) Use Meta+. to find the definition of the symbol currently under cursor.

3) You can ignore above steps and run the following in emacs to build symbol tables:
```
C-c s a 设定初始化的目录，一般是代码的根目录
C-s s I 对目录中的相关文件建立列表并进行索引

C-c s s Find symbol.

C-c s d Find global definition.

C-c s g Find global definition (alternate binding).

C-c s G Find global definition without prompting.

C-c s c Find functions calling a function.

C-c s C Find called functions (list functions called from a function).

C-c s t Find text string.

C-c s e Find egrep pattern.

C-c s f Find a file.

C-c s i Find files #including a file.

C-c s b Display *cscope* buffer.

C-c s B Auto display *cscope* buffer toggle.

C-c s n Next symbol.

C-c s N Next file.

C-c s p Previous symbol.

C-c s P Previous file.

C-c s u Pop mark.

C-x o Switch from one window to another.
```
_RET=Select, SPC=Show, o=SelectOneWin, n=ShowNext, p=ShowPrev, q=Quit, h=Help_
