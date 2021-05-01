# [Vim Tips](http://www.softpanorama.org/Editors/Vimorama/vim_tips.shtml)


1. <http://www.softpanorama.org/Editors/Vimorama/vim_tips.shtml>


2. Enable mouse support:
```
$ cat ~/.vimrc
set mouse=a
```
<http://vim.wikia.com/wiki/Using_the_mouse_for_Vim_in_an_xterm>

3. Enable/Disable syntax highlight
```
:syntax off
You can edit ~/.vimrc file and add command syntax on to it so that next you will start vim with color syntax highlighting option
$ cd
$ vi .vimrc
```
Append the following line:
```
syntax on
```
<http://www.cyberciti.biz/faq/turn-on-or-off-color-syntax-highlighting-in-vi-or-vim/>


 4. delete commands:

<http://www.devdaily.com/linux/vi-vim-delete-line-commands-to-end>
```
x   - delete current character
dw  - delete current word
dd  - delete current line
5dd - delete five lines

d$  - delete to end of line
d0  - delete to beginning of line

:1,.d
delete to beginning of file

:.,$d
delete to end of file
```
