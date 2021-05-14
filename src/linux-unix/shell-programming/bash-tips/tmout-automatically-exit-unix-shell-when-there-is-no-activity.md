# [TMOUT – Automatically Exit Unix Shell When there is No Activity](http://www.thegeekstuff.com/2010/05/tmout-exit-bash-shell-when-no-activity/)



 **Question** : I would like to terminate my Unix command line shell, when I don’t execute any command for N number of seconds. i.e How to automatically log out if there is no activity in a Linux shell ?

 **Answer** : TMOUT variable in bash will terminate the shell if there is no activity for N seconds as explained below.



    # export TMOUT=N


  * N is in seconds. When there is no activity for N seconds, the shell will be terminated.



 **Example** : Terminate the shell if there is no activity for 5 minutes.


    # export TMOUT=300


If there is no activity in a particular shell for more than 5 minutes, then it will terminate that shell. You cannot use this technique to logout from a GUI session.

From man bash:


           TMOUT  If  set  to  a  value greater than zero, TMOUT is treated as the
                  default timeout for the read builtin.  The select command termi‐
                  nates if input does not arrive after TMOUT seconds when input is
                  coming from a terminal.  In an interactive shell, the  value  is
                  interpreted  as  the  number  of seconds to wait for input after
                  issuing the primary prompt.  Bash terminates after  waiting  for
                  that number of seconds if input does not arrive.


TMOUT is useful when you are ssh-ing to a remote server and would like to log out from the remote server when you don’t perform any activity for x number of seconds. Add the export command to your [.bash_profile or .bashrc](http://www.thegeekstuff.com/2008/10/execution-sequence-for-bash_profile-bashrc-bash_login-profile-and-bash_logout/) on the remote-server.

---
