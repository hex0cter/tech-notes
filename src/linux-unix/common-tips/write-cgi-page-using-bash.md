
date: None  
author(s): None  

# [Write CGI page using BASH - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/write-cgi-page-using-bash)

<http://www.yolinux.com/TUTORIALS/BashShellCgi.html>

| 

Web CGI programs can be written in any language which can process standard input (stdin), environment variables and write to standard output (stdout). The web server will interact with all CGI programs using the "Common Gateway Interface" (CGI) standard as set by [RFC 3875](http://www.ietf.org/rfc/rfc3875). This capability is possessed by most modern computer programming and scripting languages, including the bash shell.

Other related YoLinux.com CGI Tutorials:

  * [Introduction Guide to XHTML](http://www.yolinux.com/TUTORIALS/XHTML_Intro.html)
  * [Web scripting languages](http://www.yolinux.com/TUTORIALS/WebPageScripting.html)
  * [ISINDEX CGI](http://www.yolinux.com/TUTORIALS/LinuxTutorialCgiShellScript.html)

  
---  
  
CGI programs typically perform the following:

  * All CGI scripts must write out a header used by the browser to identify the content.
  * They typically process some input. (URL, form data or ISINDEX)
  * CGI can access environment variables set by the web server.
  * CGI scripts will write out HTML content to be viewed. This typically has the structure of the "head" which contains non-viewable content and "body" which provides the viewable content.



Hello World Example:

    File: `/var/www/cgi-bin/hello.sh`

| `03`| `echo` `"Content-type: text/html"`  
---|---  
  
`08`| `echo` `'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'`  
---|---  
  
`09`| `echo` `'<title>Hello World</title>'`  
---|---  
  
#### Script Location:

Various distributions of Linux locate the CGI directory in different directory paths. The path is set by the web server configuration file. For the Apache web server, the "ScriptAlias" directive defines the CGI path:

    Linux Distribution| Path  
---|---  
Red Hat Enterprise, 7.x-9, Fedora core, CentOS| `/var/www/cgi-bin/`  
Red Hat 6.x and older| `/home/httpd/cgi-bin/`  
SuSe| `/srv/www/cgi-bin/`  
Ubuntu/Debian| `/usr/lib/cgi-bin/`  
  
#### Script Permissions:

The script will require system executable permissions: `chmod +x /var/www/cgi-bin/hello.sh`

If using SELinux, the security context must also permit execution: `chcon -t httpd_sys_content_t /var/www/cgi-bin/hello.sh`

### Executing Shell Commands:

Typically one will want to process shell or system commands:

    Add the paths required to find the commands:File: `/var/www/cgi-bin/uptime.sh`

| `03`| `echo` `"Content-type: text/html"`  
---|---  
  
`08`| `echo` `'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'`  
---|---  
  
`12`| `PATH=``"/bin:/usr/bin:/usr/ucb:/usr/opt/bin"`  
---|---  
  
`15`| `echo` `'<title>System Uptime</title>'`  
---|---  
  
This example will print the "hostname" and "uptime" of the system.
 **Processing Bash CGI Input:**  
---  
  
#### Accessing Environment Variables:

The web server will pass environment variables to the CGI which it can access and use. This is very simple for bash.

    File: `/var/www/cgi-bin/env.sh`

| `03`| `echo` `"Content-type: text/html"`  
---|---  
  
`08`| `echo` `'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'`  
---|---  
  
`09`| `echo` `'<title>Environment Variables</title>'`  
---|---  
  
`12`| `echo` `'Environment Variables:'`  
---|---  
  
List of environment variables for the following URL: `http://localhost/cgi-bin/env.sh?namex=valuex&namey=valuey&namez=valuez`

Environment Variables:

`SERVER_SIGNATURE= HTTP_KEEP_ALIVE=300 HTTP_USER_AGENT=Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20050922 Fedora/1.7.12-1.3.1 SERVER_PORT=80 HTTP_HOST=localhost DOCUMENT_ROOT=/var/www/html HTTP_ACCEPT_CHARSET=ISO-8859-1,utf-8;q=0.7,*;q=0.7 SCRIPT_FILENAME=/var/www/cgi-bin/env.sh REQUEST_URI=/cgi-bin/env.sh?namex=valuex&namey=valuey&namez=valuez SCRIPT_NAME=/cgi-bin/env.sh HTTP_CONNECTION=keep-alive REMOTE_PORT=37958 PATH=/sbin:/usr/sbin:/bin:/usr/bin PWD=/var/www/cgi-bin SERVER_ADMIN=root@localhost HTTP_ACCEPT_LANGUAGE=en-us,en;q=0.5 HTTP_ACCEPT=text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5 REMOTE_ADDR=198.168.93.176 SHLVL=1 SERVER_NAME=localhost SERVER_SOFTWARE=Apache/2.2.3 (CentOS) QUERY_STRING=namex=valuex&namey=valuey&namez=valuez SERVER_ADDR=192.168.93.42 GATEWAY_INTERFACE=CGI/1.1 SERVER_PROTOCOL=HTTP/1.1 HTTP_ACCEPT_ENCODING=gzip,deflate REQUEST_METHOD=GET 

_=/usr/bin/env

`  
---  
Example for CentOS 5

Typically one will want to process input from the URL "QUERY_STRING" such as "namex=valuex&namey=valuey&namez=valuez" extracted from the following URL:`http://localhost/cgi-bin/env.sh?namex=valuex&namey=valuey&namez=valuez`

    Script Description:

  * Script will loop through all of the arguments in environment variable "QUERY_STRING" as separated by the delimiter "&". Thus the script loops three times with the following "Args":
    * namex=valuex
    * namey=valuey
    * namez=valuez
  * For each "Args" line, look for each token separated by the delimeter "=". Component 1 ($1) and component 2 ($2).
  * Use "sed" to parse and substitute characters. A blank space is substituted for all %20's.



| `03`| `echo` `"Content-type: text/html"`  
---|---  
  
`08`| `echo` `'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'`  
---|---  
  
`09`| `echo` `'<title>Environment Variables</title>'`  
---|---  
  
`12`| `echo` `'Parse Variables:'`  
---|---  
  
`14`| `# Save the old internal field separator.`  
---|---  
  
`17`| `# Set the field separator to & and parse the QUERY_STRING at the ampersand.`  
---|---  
  
`23`| `# Next parse the individual "name=value" tokens.`  
---|---  
  
`31`| `# Set the field separator to =`  
---|---  
  
`37`| ` ``# Don't allow "/" changed to " ". Prevent hacker problems.`  
---|---  
  
`38`| ` ``namex) ARGX=``"`echo $2 | sed 's|[\]||g' | sed 's|%20| |g'`"`  
---|---  
  
`40`| ` ``# Filter for "/" not applied here`  
---|---  
  
`41`| ` ``namey) ARGY=``"`echo $2 | sed 's|%20| |g'`"`  
---|---  
  
`43`| ` ``namez) ARGZ=``"${2/\// /}"`  
---|---  
  
`45`| ` ``*) ``echo` `"<hr>Warning:"``\`  
---|---  
  
`46`| ` ``"<br>Unrecognized variable \'$1\' passed by FORM in QUERY_STRING.<hr>"`  
---|---  
  
Output:
    
    
    Parsed Values:
    valuex
    valuey
    valuez
      
  
---  
You will get the same results for: `http://node1.megawww.com/cgi-bin/env.sh?namex=valuex&namez=valuez&namey=valuey`
Typically one will also want to produce and process input from an HTML form:

    URL: `http://localhost/cgi-bin/exampleForm.sh`   
![Bash shell script form example](http://www.yolinux.com/TUTORIALS/images/BashShellCGIexampleForm.gif)   
File: `/var/www/cgi-bin/exampleForm.sh`

| `03`| `echo` `"Content-type: text/html"`  
---|---  
  
`08`| `echo` `'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'`  
---|---  
  
`09`| `echo` `'<title>Form Example</title>'`  
---|---  
  
`13`| ` ``echo` `"<form method=GET action=\"${SCRIPT}\">"``\`  
---|---  
  
`15`| ` ``'<tr><td>Input</TD><TD><input type="text" name="val_x" size=12></td></tr>'``\`  
---|---  
  
`16`| ` ``'<tr><td>Section</td><td><input type="text" name="val_y" size=12 value=""></td>'``\`  
---|---  
  
`19`| ` ``echo` `'<input type="radio" name="val_z" value="1" checked> Option 1<br>'``\`  
---|---  
  
`20`| ` ``'<input type="radio" name="val_z" value="2"> Option 2<br>'``\`  
---|---  
  
`21`| ` ``'<input type="radio" name="val_z" value="3"> Option 3'`  
---|---  
  
`23`| ` ``echo` `'<br><input type="submit" value="Process Form">'``\`  
---|---  
  
`24`| ` ``'<input type="reset" value="Reset"></form>'`  
---|---  
  
`26`| ` ``# Make sure we have been invoked properly.`  
---|---  
  
`28`| ` ``if` `[ ``"$REQUEST_METHOD"` `!= ``"GET"` `]; ``then`  
---|---  
  
`29`| ` ``echo` `"<hr>Script Error:"``\`  
---|---  
  
`30`| ` ``"<br>Usage error, cannot complete request, REQUEST_METHOD!=GET."``\`  
---|---  
  
`31`| ` ``"<br>Check your FORM declaration and be sure to use METHOD=\"GET\".<hr>"`  
---|---  
  
`35`| ` ``# If no search arguments, exit gracefully now.`  
---|---  
  
`37`| ` ``if` `[ -z ``"$QUERY_STRING"` `]; ``then`  
---|---  
  
`40`| ` ``# No looping this time, just extract the data you are looking for with sed:`  
---|---  
  
`41`| ` ``XX=```echo` `"$QUERY_STRING"` `| ``sed` `-n ``'s/^.*val_x=\([^&]*\).*$/\1/p'` `| ``sed` `"s/%20/ /g"````  
---|---  
  
`42`| ` ``YY=```echo` `"$QUERY_STRING"` `| ``sed` `-n ``'s/^.*val_y=\([^&]*\).*$/\1/p'` `| ``sed` `"s/%20/ /g"````  
---|---  
  
`43`| ` ``ZZ=```echo` `"$QUERY_STRING"` `| ``sed` `-n ``'s/^.*val_z=\([^&]*\).*$/\1/p'` `| ``sed` `"s/%20/ /g"````  
---|---  
  
Note that the environment variables $REQUEST_METHOD and $QUERY_STRING can be processed by the shell directly.
    

    

You can string together more "sed" translators as needed (depending on your content): `| sed "s/%20/ /g" | sed "s/%3A/:/g" | sed "s/%2F/\//g"`

Filling out the form with the following values:

    ![Bash shell script form example](http://www.yolinux.com/TUTORIALS/images/BashShellCGIexampleForm_Input.gif)
Selecting the button "Process Form" will result in the URL: `http://localhost/cgi-bin/exampleForm.sh?val_x=AAA&val_y=BBB&val_z=3`   
which will be processed to result in the following display:
    
    
    val_x: AAA
    val_y: BBB
    val_z: 3
      
  
---  
  
One must filter the input to avoid cross site scripting. Filter out "<>&*?./" to avoid trouble from hackers.

