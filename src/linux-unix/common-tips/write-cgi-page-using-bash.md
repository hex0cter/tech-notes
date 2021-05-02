# [Write CGI page using BASH](http://www.yolinux.com/TUTORIALS/BashShellCgi.html)

## Introduction to CGI:

Web CGI programs can be written in any language which can process standard input (stdin), environment variables and write to standard output (stdout). The web server will interact with all CGI programs using the "Common Gateway Interface" (CGI) standard as set by [RFC 3875](http://www.ietf.org/rfc/rfc3875). This capability is possessed by most modern computer programming and scripting languages, including the bash shell.

Other related YoLinux.com CGI Tutorials:

  * [Introduction Guide to XHTML](http://www.yolinux.com/TUTORIALS/XHTML_Intro.html)
  * [Web scripting languages](http://www.yolinux.com/TUTORIALS/WebPageScripting.html)
  * [ISINDEX CGI](http://www.yolinux.com/TUTORIALS/LinuxTutorialCgiShellScript.html)

## Basic Bash CGI Example:

CGI programs typically perform the following:

  * All CGI scripts must write out a header used by the browser to identify the content.
  * They typically process some input. (URL, form data or ISINDEX)
  * CGI can access environment variables set by the web server.
  * CGI scripts will write out HTML content to be viewed. This typically has the structure of the "head" which contains non-viewable content and "body" which provides the viewable content.



Hello World Example:

    File: `/var/www/cgi-bin/hello.sh`
```
#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Hello World</title>'
echo '</head>'
echo '<body>'
echo 'Hello World'
echo '</body>'
echo '</html>'

exit 0
```

#### Script Location:

Various distributions of Linux locate the CGI directory in different directory paths. The path is set by the web server configuration file. For the Apache web server, the "ScriptAlias" directive defines the CGI path:

Linux Distribution| P|---
Red Hat Enterprise, 7.x-9, Fedora core, CentOS | `/var/www/cgi-bin/`
Red Hat 6.x and older | `/home/httpd/cgi-bin/`
SuSe | `/srv/www/cgi-bin/`
Ubuntu/Debian | `/usr/lib/cgi-bin/`

#### Script Permissions:

The script will require system executable permissions: `chmod +x /var/www/cgi-bin/hello.sh`

If using SELinux, the security context must also permit execution: `chcon -t httpd_sys_content_t /var/www/cgi-bin/hello.sh`

### Executing Shell Commands:

Typically one will want to process shell or system commands:

    Add the paths required to find the commands:File: `/var/www/cgi-bin/uptime.sh`

```
#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<link rel="SHORTCUT ICON" href="http://www.megacorp.com/favicon.ico">'
echo '<link rel="stylesheet" href="http://www.megacorp.com/style.css" type="text/css">'

PATH="/bin:/usr/bin:/usr/ucb:/usr/opt/bin"
export $PATH

echo '<title>System Uptime</title>'
echo '</head>'
echo '<body>'

echo '<h3>'
hostname
echo '</h3>'

uptime

echo '</body>'
echo '</html>'

exit 0
```

This example will print the "hostname" and "uptime" of the system.
 **Processing Bash CGI Input:**
---

#### Accessing Environment Variables:

The web server will pass environment variables to the CGI which it can access and use. This is very simple for bash.

    File: `/var/www/cgi-bin/env.sh`

```
#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Environment Variables</title>'
echo '</head>'
echo '<body>'
echo 'Environment Variables:'
echo '<pre>'
/usr/bin/env
echo '</pre>'

echo '</body>'
echo '</html>'

exit 0

```

List of environment variables for the following URL: `http://localhost/cgi-bin/env.sh?namex=valuex&namey=valuey&namez=valuez`

Environment Variables:

```
Environment Variables:

SERVER_SIGNATURE=
HTTP_KEEP_ALIVE=300
HTTP_USER_AGENT=Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.12) Gecko/20050922 Fedora/1.7.12-1.3.1
SERVER_PORT=80
HTTP_HOST=localhost
DOCUMENT_ROOT=/var/www/html
HTTP_ACCEPT_CHARSET=ISO-8859-1,utf-8;q=0.7,*;q=0.7
SCRIPT_FILENAME=/var/www/cgi-bin/env.sh
REQUEST_URI=/cgi-bin/env.sh?namex=valuex&namey=valuey&namez=valuez
SCRIPT_NAME=/cgi-bin/env.sh
HTTP_CONNECTION=keep-alive
REMOTE_PORT=37958
PATH=/sbin:/usr/sbin:/bin:/usr/bin
PWD=/var/www/cgi-bin
SERVER_ADMIN=root@localhost
HTTP_ACCEPT_LANGUAGE=en-us,en;q=0.5
HTTP_ACCEPT=text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
REMOTE_ADDR=198.168.93.176
SHLVL=1
SERVER_NAME=localhost
SERVER_SOFTWARE=Apache/2.2.3 (CentOS)
QUERY_STRING=namex=valuex&namey=valuey&namez=valuez
SERVER_ADDR=192.168.93.42
GATEWAY_INTERFACE=CGI/1.1
SERVER_PROTOCOL=HTTP/1.1
HTTP_ACCEPT_ENCODING=gzip,deflate
REQUEST_METHOD=GET
_=/usr/bin/env
```

Example for CentOS 5

Typically one will want to process input from the URL "QUERY_STRING" such as "namex=valuex&namey=valuey&namez=valuez" extracted from the following URL:`http://localhost/cgi-bin/env.sh?namex=valuex&namey=valuey&namez=valuez`

    Script Description:

  * Script will loop through all of the arguments in environment variable "QUERY_STRING" as separated by the delimiter "&". Thus the script loops three times with the following "Args":
    * namex=valuex
    * namey=valuey
    * namez=valuez
  * For each "Args" line, look for each token separated by the delimeter "=". Component 1 ($1) and component 2 ($2).
  * Use "sed" to parse and substitute characters. A blank space is substituted for all %20's.

```
#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Environment Variables</title>'
echo '</head>'
echo '<body>'
echo 'Parse Variables:'

# Save the old internal field separator.
  OIFS="$IFS"

# Set the field separator to & and parse the QUERY_STRING at the ampersand.
  IFS="${IFS}&"
  set $QUERY_STRING
  Args="$*"
  IFS="$OIFS"

# Next parse the individual "name=value" tokens.

  ARGX=""
  ARGY=""
  ARGZ=""

  for i in $Args ;do

        # Set the field separator to =
        IFS="${OIFS}="
        set $i
        IFS="${OIFS}"

        case $1 in
                # Don't allow "/" changed to " ". Prevent hacker problems.
                namex) ARGX="`echo $2 | sed 's|[\]||g' | sed 's|%20| |g'`"
                       ;;
                # Filter for "/" not applied here
                namey) ARGY="`echo $2 | sed 's|%20| |g'`"
                       ;;
                namez) ARGZ="${2/\// /}"
                       ;;
                *)     echo "<hr>Warning:"\
                            "<br>Unrecognized variable \'$1\' passed by FORM in QUERY_STRING.<hr>"
                       ;;

        esac
  done

  echo 'Parsed Values:'
  echo '<br>'
  echo $ARGX
  echo '<br>'
  echo $ARGY
  echo '<br>'
  echo $ARGZ

echo '</body>'
echo '</html>'

exit 0

```

Output:

    Parsed Values:
    valuex
    valuey
    valuez


You will get the same results for: `http://node1.megawww.com/cgi-bin/env.sh?namex=valuex&namez=valuez&namey=valuey`
Typically one will also want to produce and process input from an HTML form:

    URL: `http://localhost/cgi-bin/exampleForm.sh`
![Bash shell script form example](http://www.yolinux.com/TUTORIALS/images/BashShellCGIexampleForm.gif)
File: `/var/www/cgi-bin/exampleForm.sh`
```
#!/bin/bash

echo "Content-type: text/html"
echo ""

echo '<html>'
echo '<head>'
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
echo '<title>Form Example</title>'
echo '</head>'
echo '<body>'

  echo "<form method=GET action=\"${SCRIPT}\">"\
       '<table nowrap>'\
          '<tr><td>Input</TD><TD><input type="text" name="val_x" size=12></td></tr
          '<tr><td>Section</td><td><input type="text" name="val_y" size=12 value=""></td
          '</tr></table>'

  echo '<input type="radio" name="val_z" value="1" checked> Option 1<br>'\
       '<input type="radio" name="val_z" value="2"> Option 2<br>'\
       '<input type="radio" name="val_z" value="3"> Option 3'
  echo '<br><input type="submit" value="Process Form">'\
       '<input type="reset" value="Reset"></form>'

  # Make sure we have been invoked properly.

  if [ "$REQUEST_METHOD" != "GET" ]; then
        echo "<hr>Script Error:"\
             "<br>Usage error, cannot complete request, REQUEST_METHOD!=GET."\
             "<br>Check your FORM declaration and be sure to use METHOD=\"GET\".<hr>"
        exit 1
  fi

  # If no search arguments, exit gracefully now.

  if [ -z "$QUERY_STRING" ]; then
        exit 0
  else
     # No looping this time, just extract the data you are looking for with sed:
     XX=`echo "$QUERY_STRING" | sed -n 's/^.*val_x=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     YY=`echo "$QUERY_STRING" | sed -n 's/^.*val_y=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     ZZ=`echo "$QUERY_STRING" | sed -n 's/^.*val_z=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
     echo "val_x: " $XX
     echo '<br>'
     echo "val_y: " $YY
     echo '<br>'
     echo "val_z: " $ZZ
  fi
echo '</body>'
echo '</html>'

exit 0

```

Note that the environment variables $REQUEST_METHOD and $QUERY_STRING can be processed by the shell directly.


You can string together more "sed" translators as needed (depending on your content): `| sed "s/%20/ /g" | sed "s/%3A/:/g" | sed "s/%2F/\//g"`

Filling out the form with the following values:

    ![Bash shell script form example](http://www.yolinux.com/TUTORIALS/images/BashShellCGIexampleForm_Input.gif)
Selecting the button "Process Form" will result in the URL: `http://localhost/cgi-bin/exampleForm.sh?val_x=AAA&val_y=BBB&val_z=3`
which will be processed to result in the following display:


    val_x: AAA
    val_y: BBB
    val_z: 3

## CGI Security:

One must filter the input to avoid cross site scripting. Filter out "<>&*?./" to avoid trouble from hackers.
