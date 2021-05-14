# [Performing Math calculation in Bash](https://www.shell-tips.com/2010/06/14/performing-math-calculation-in-bash/)

I use math in bash scripts a lot, from simple crontab reports to Nagios monitoring plugins… Here is few small examples on how to do some maths in Bash with integers or float.

 **Integer Math
**

First way to do math with integer (and only integer) is to use the command “ _expr — evaluate expression_ “.

```
Mac-n-Cheese:~ nicolas$ expr 1 + 1
2
Mac-n-Cheese:~ nicolas$ myvar=$(expr 1 + 1)
Mac-n-Cheese:~ nicolas$ echo $myvar
2
Mac-n-Cheese:~ nicolas$ expr $myvar + 1
3
Mac-n-Cheese:~ nicolas$ expr $myvar / 3
1
Mac-n-Cheese:~ nicolas$ expr $myvar \* 3
9
```

When doing a “multiply by” make sure to backslash the “asterisk” as it’s a wildcard in Bash used for expansion.

Another alternative to _expr_ , is to use the bash builtin command _let_.

```
Mac-n-Cheese:~ nicolas$ echo $myvar
6
Mac-n-Cheese:~ nicolas$ let myvar+=1
Mac-n-Cheese:~ nicolas$ echo $myvar
7
Mac-n-Cheese:~ nicolas$ let myvar+1
Mac-n-Cheese:~ nicolas$ echo $myvar
7
Mac-n-Cheese:~ nicolas$ let myvar2=myvar+1
Mac-n-Cheese:~ nicolas$ echo $myvar2
8
```

Also, you can simply use the parentheses or square brackets :

```
Mac-n-Cheese:~ nicolas$ echo $myvar
3
Mac-n-Cheese:~ nicolas$ echo $((myvar+2))
5
Mac-n-Cheese:~ nicolas$ echo $[myvar+2]
5
Mac-n-Cheese:~ nicolas$ myvar=$((myvar+3))
```

This allow you to use C-style programming :

```
Mac-n-Cheese:~ nicolas$ echo $myvar
3
Mac-n-Cheese:~ nicolas$ echo $((myvar++))
3
Mac-n-Cheese:~ nicolas$ echo $myvar
4
Mac-n-Cheese:~ nicolas$ echo $((++myvar))
5
Mac-n-Cheese:~ nicolas$ echo $myvar
5
```

 **Floating point arithmetic**

If you need to do floating point arithmetic, you will have to use a command line tool, the most common one is “ _bc – An arbitrary precision calculator language_ “.

```
Mac-n-Cheese:~ nicolas$ bc
bc 1.06
Copyright 1991-1994, 1997, 1998, 2000 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
3*5.2+7/8
15.6
15.6+299.33*2.3/7.4
108.6
```

Of course you can use the STDIN to send your formula to “ _bc_ ” then get the output on STDOUT.

```
Mac-n-Cheese:~ nicolas$ echo "3.4+7/8-(5.94*3.14)" | bc
-15.25
```

I encourage you too take a look at the man pages to get more detail on how it works ( _man bc_ ).

> There are four special variables, scale, ibase, obase, and last. scale defines how some operations use digits after the decimal point. The default value of scale is 0. ibase and obase define the conver-
> sion base for input and output numbers. The default for both input and output is base 10. last (an extension) is a variable that has the value of the last printed number.

The “scale” variable is really important for the precision of your results, especially when using integers only (Note: you can also use “bc -l” to use mathlib and see the result at max scale) .

```
Mac-n-Cheese:~ nicolas$ echo "2/3" | bc
0
Mac-n-Cheese:~ nicolas$ echo "scale=2; 2/3" | bc
.66
Mac-n-Cheese:~ nicolas$ echo "(2/3)+(7/8)" | bc
0
Mac-n-Cheese:~ nicolas$ echo "scale=2;(2/3)+(7/8)" | bc
1.53
Mac-n-Cheese:~ nicolas$ echo "scale=4;(2/3)+(7/8)" | bc
1.5416
Mac-n-Cheese:~ nicolas$ echo "scale=6;(2/3)+(7/8)" | bc
1.541666
Mac-n-Cheese:~ nicolas$ echo "(2/3)+(7/8)" | bc -l
1.54166666666666666666
```

You can also use the here-doc notation to pass your formula to bc :

```
Mac-n-Cheese:~ nicolas$ bc -l <<< "(2/3)+(7/8)"
1.54166666666666666666
```
