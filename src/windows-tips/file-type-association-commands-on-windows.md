# File type association commands on Windows

Checking whether the association is already configured:


    C:\MyRuby>assoc .rb
    File association not found for extension .rb


Assuming that the association is not already configured, take the following steps to complete the configuration:


    C:\MyRuby>assoc .rb=rbFile



Check to see if the file type _rbfile_ already exists:


    C:\MyRuby>ftype rbfile
    File type 'rbfile' not found or no open command associated with it.


Assuming it does not already exist (be sure to substitute the path to your Ruby installation in the following command):


    C:\MyRuby>ftype rbfile="D:\Ruby\bin\ruby.exe" "%1" %*


Verify the setting:


    C:\MyRuby>ftype rbfile
    rbfile="D:\ruby\bin\ruby.exe" "%1" %*


Add .rb to the PATHEXT environment variable as follows:


    C:\MyRuby>set PATHEXT=.rb;%PATHEXT%


Once the above settings are configured simply run the program by typing the filename at the command prompt (the .rb filename extension is not required), e.g."


    C:\MyRuby> hello
    Hello Ruby


The above steps can be placed in your Autoexec.bat file if you would like this association made every time you reboot your system.

---
