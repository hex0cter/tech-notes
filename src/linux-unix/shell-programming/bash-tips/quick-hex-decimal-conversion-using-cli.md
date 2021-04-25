
date: None  
author(s): None  

# [Quick hex / decimal conversion using CLI - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/shell-programming/bash-tips/quick-hex-decimal-conversion-using-cli)

<http://linuxcommando.blogspot.se/2008/04/quick-hex-decimal-conversion-using-cli.html>

Once in a while, you need to convert a number from hexadecimal to decimal notation, and vice versa.Say, you want to know the decimal equivalent of the hexadecimal 15A.You can convert in many different ways, all within bash, and relatively easy.To convert a number from hexadecimal to decimal:

  

    
    
     $ echo $((0x15a))  
    346
    
    
     $ printf '%d\n' 0x15a  
    346
    
    
     $ perl -e 'printf ("%d\n", 0x15a)'  
    346
    
    
     $ echo 'ibase=16;obase=A;15A' | bc  
    346

Note that ibase and obase specify the input and the output notation respectively.  
By default, the notation for both is decimal unless you change it using ibase or obase.

Because you change the notation to hex using ibase, your obase needs to be specified in hex (A in hex = 10 in decimal).

The input number (15A) needs to be in UPPER case. 15a will give you a parse error.

To convert from decimal to hex,

  

    
    
    $ printf '%x\n' 346  
    15a

  

    
    
     $ perl -e 'printf ("%x\n", 346)'  
    15a

  

    
    
     $ echo 'ibase=10;obase=16;346' | bc  
    15A  
  
---

