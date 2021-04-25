
date: None  
author(s): None  

# [How to schedule tasks on Linux using the 'at' command - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/at/how-to-schedule-tasks-on-linux-using-the-at-command)

http://www.simplehelp.net/2009/05/04/how-to-schedule-tasks-on-linux-using-the-at-command/

by SUKRIT DHANDHANIA on MAY 4, 2009

![Linux](http://www.simplehelp.net/wp-images/icons/topic_linux.jpg)

Scheduling jobs is an essential part of administering Linux servers. We took a look at how to schedule jobs on Linux machine using the [cron](http://www.simplehelp.net/2008/11/17/increase-your-linuxunix-productivity-how-to-use-crontab/) command earlier. Here’s an alternative to **cron** – **at**. The primary difference between the two is that when you schedule a task using cron it execute repeatedly without the need for rescheduling. With **at** , on the other hand, the scheduling of a task is only for a single execution. Both of these commands have their use, and I would suggest that you get a good understanding of them both.

Let’s look at how to schedule a task to execute only once using the **at** command. First make sure that the **at daemon** is running using a command like this:

 **# ps -ef | grep atdroot 8231 1 0 18:10 ? 00:00:00 /usr/sbin/atd**

If you don’t see **atd** running start it with this command:

 **# /etc/init.d/atd start**

Once the daemon has been started successfully you can schedule an **at** task using the two options **-f** , for the file to be executed, and **-v** , for the time at which it should be executed. So if you want to execute the shell script **shellscript.sh** at 6:30 PM you would run the following command:

 **# at -f shellscript.sh -v 18:30**

Remember that with the **at** command the script **shellscript.sh** will execute at 6:30 PM and then the scheduling will disappear. So if this is not what you desire, you are better off using **cron**.

The **at** command is pretty clever in that it can take some orders in English if you like. For example, you can schedule jobs using the following syntax as well:

 **# at -f shellscript.sh 10pm tomorrow**

 **# at -f shellscript.sh 2:50 tuesday**

 **# at -f shellscript.sh 6:00 july 11**

 **# at -f shellscript.sh 2:00 next week**  
  
---

