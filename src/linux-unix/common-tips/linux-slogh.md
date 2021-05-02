# How to change Linux login slogan/greeting

Here is one of the places where login slogans are stored:

 **/etc/ssh/sshd_config: Banner <filename>** (where filename includes all the information to be displayed before use login)

> This is printed out before password is prompted (sshd may need to be restarted). It applies to both ssh and scp.

 **/etc/motd**

> This is printed after user has been successfully logged in, i.e., the password is correct.
