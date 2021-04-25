
date: None  
author(s): None  

# [Log watching using tail or less - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/log-watching-using-tail-or-less)

http://linuxcommando.blogspot.se/2007/11/log-watching-using-tail-or-less.html

Log files typically grow in size, with the latest contents appended to the end of the log. I often need to watch a log file in live action, for error detection.

The command tail -f will display the last 10 lines of a file, and then continuously wait for new lines, and display them as they appear.

  

    
    
    $ tail -f /var/log/messages

If you want to see more than ten lines at the outset, specify the new number (say 50 lines) like this:

  

    
    
    $ tail -50 -f /var/log/messages

The tail command is fast and simple. But if you want more than just following a file (e.g., scrolling and searching), then less may be the command for you.

  

    
    
    $ less /var/log/messages

  
Press Shift-F. This will take you to the end of the file, and continuously display new contents. In other words, it behaves just like tail -f.

To start less in the tail mode (thanks to Seth Milliken for this tip), execute:

  

    
    
    $ less +F /var/log/messages

To scroll backwards, you must first exit the follow mode by pressing Control-c. Then, you can scroll back by pressing b. In fact, all the lesscommands are available to you once you are in the regular less mode. You can start a search by typing / followed by the string you want to search for. 

Happy Log Watching !!!

P.S.

  
Related articles on tailing files:  
[Tail multiple files](http://linuxcommando.blogspot.com/2007/11/tail-multiple-files.html)  
[Two additional ways to tail a log file](http://linuxcommando.blogspot.com/2008/11/two-additional-ways-to-tail-log-file.html)  
  
---

