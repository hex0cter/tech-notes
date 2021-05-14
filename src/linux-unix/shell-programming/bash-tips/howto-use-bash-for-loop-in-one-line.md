# [HowTo: Use bash For Loop In One Line](http://www.cyberciti.biz/faq/linux-unix-bash-for-loop-one-line-command/)

How do I use bash for loop in one line under UNIX or Linux operating systems?

The syntax is as follows to run for loop from the command prompt.

## Run Command 5 Times


     
    for i in {1..5}; do COMMAND-HERE; done
     

OR


      for((i=1;i<=10;i+=2)); do echo "Welcome $i times"; done
     

## Work On Files


     
    for i in *; do echo $i; done
     

OR


     
    for i in /etc/*.conf; do cp $i /backup; done
