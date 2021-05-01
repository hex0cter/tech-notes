# [display ^M in vim](http://stackoverflow.com/questions/3852868/how-to-make-vim-show-m-and-substitute-it)


## Display CRLF as ^M:
```
:e ++ff=unix
```
## Substitute CRLF for LF:
```
:setlocal ff=unix
:w
:e
```
