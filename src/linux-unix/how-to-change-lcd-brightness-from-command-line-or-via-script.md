# [How to change LCD brightness from command line (or via script)?](hhttp://askubuntu.com/questions/149054/how-to-change-lcd-brightness-from-command-line-or-via-script)

http://askubuntu.com/questions/149054/how-to-change-lcd-brightness-from-command-line-or-via-script

one more way we have to do this is with another new program named as xbacklight , open your terminal and type this


    sudo apt-get install xbacklight


then type this `xbacklight -set 50`

there 50 stands for brightness range we can get it upto 100 from 0 .

you can also increase and decrease the brightness from present value to specified level.as you mentioned if you want to increase to 10% from current value of brightness then you can give this


    xbacklight -inc 10


and to decrease 10% you can give this


    xbacklight -dec 10

---
