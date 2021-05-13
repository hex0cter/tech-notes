# Korn Shell file options (condition check)


               -r file              file exists and is readable.
               -w file              file exists and is writable.
               -x file              file   exists  and  is  exeÂ­
                                    cutable.
               -a file              file exists.
               -e file              file exists.
               -f file              file is a regular file.
               -d file              file is a directory.
               -c file              file is a character  special
                                    device.
               -b file              file   is  a  block  special
                                    device.
               -p file              file is a named pipe.
               -u file              file's mode has  setuid  bit
                                    set.
               -g file              file's  mode  has setgid bit
                                    set.
               -k file              file's mode has  sticky  bit
                                    set.
               -s file              file is not empty.
               -O file              file's  owner is the shell's
                                    effective user-ID.
               -G file              file's group is the  shell's
                                    effective group-ID.
               -h file              file is a symbolic link.
               -H file              file  is a context dependent
                                    directory  (only  useful  on
                                    HP-UX).
               -L file              file is a symbolic link.
               -S file              file is a socket.

               file -nt file        first  file  is  newer  than
                                    second file  or  first  file
                                    exists  and  the second file
                                    does not.
               file -ot file        first  file  is  older  than
                                    second  file  or second file
                                    exists and  the  first  file
                                    does not.
               file -ef file        first  file is the same file


From: `man ksh` on SUSE Linux.
