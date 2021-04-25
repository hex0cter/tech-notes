
date: None  
author(s): None  

# [How to use SimpleHTTPServer - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/software-development/python/how-to-use-simplehttpserver)


    In this post we will look at the built-in web server in Python.
    
    
    
    The SimpleHTTPServer module that comes with Python is a simple HTTP server that
    provides standard GET and HEAD request handlers.
    
    
    
    An advantage with the built-in HTTP server is that you don't have to install
    and configure anything. The only thing that you need, is to have Python installed.
    
    That makes it perfect to use when you need a quick web server running and you
    don't want to mess with setting up apache.
    
    You can use this to turn any directory in your system into your web server
    directory.
    
    
    
    To start a HTTP server on port 8000 (which is the default port), simple type:
    
    
    
    python -m SimpleHTTPServer [port]
    
    
    
    This will now show the files and directories which are in the current working
    directory.
    
    
    
    You can also change the port to something else:
    
    
    $ python -m SimpleHTTPServer 8080
    
    
    
    In your terminal, cd into whichever directory you wish to have accessible via
    browsers and HTTP.
    
    
    
    cd /var/www/
    
    $ python -m SimpleHTTPServer
    
    
    
    After you hit enter, you should see the following message:
    
    Serving HTTP on 0.0.0.0 port 8000 ...
    
    
    
    Open your favorite browser and put in any of the following addresses:
    
    
    
    http://your_ip_address:8000
     
    http://127.0.0.1:8000
    
    
    
    If you don't have an index.html file in the directory, then all files and
    directories will be listed.
    
    
    
    As long as the HTTP server is running, the terminal will update as data are
    loaded from the Python web server. 
    
    You should see standard http logging information (GET and PUSH), 404 errors,
    IP addresses, dates, times, and all that you would expect from a standard http
    log as if you were tailing an apache access log file.
    
    
    
    In this post we showed how you with minimal effort can setup a web server to
    serve content. 
    
    It's a great way of serve the contents of the current directory from the command
    line
    
    While there are many web server software out there (apache, nginx), using Python
    built-in HTTP server require no installation and configuration. 
    
    
    
    [http://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python
    ](http://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python)
    [osxdaily.com](http://osxdaily.com/2010/05/07/create-an-instant-web-server-via-terminal-command-line/)

