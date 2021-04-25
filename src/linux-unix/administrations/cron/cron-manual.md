# cron manual

```
CRONTAB(5)							    CRONTAB(5)

NAME
       crontab - tables for driving cron

DESCRIPTION
       A  crontab file contains instructions to the cron(8) daemon of the gen-
       eral form: ``run this command at this time on this date''.   Each  user
       has  their  own crontab, and commands in any given crontab will be exe-
       cuted as the user who owns the crontab.	Uucp  and  News	 will  usually
       have  their  own	 crontabs, eliminating the need for explicitly running
       su(1) as part of a cron command.

       Blank lines and leading spaces and tabs are ignored.  Lines whose first
       non-space  character is a pound-sign (#) are comments, and are ignored.
       Note that comments are not allowed on the same line as  cron  commands,
       since  they  will  be taken to be part of the command.  Similarly, com-
       ments are not allowed on the same line  as  environment	variable  set-
       tings.

       An  active line in a crontab will be either an environment setting or a
       cron command.  An environment setting is of the form,

	   name = value

       where the spaces around the equal-sign (=) are optional, and any subse-
       quent non-leading spaces in value will be part of the value assigned to
       name.  The value string may be placed in quotes (single or double,  but
       matching) to preserve leading or trailing blanks.

       Several	environment  variables are set up automatically by the cron(8)
       daemon.	SHELL is set to /bin/sh, and LOGNAME and HOME are set from the
       /etc/passwd  line  of the crontab's owner.  HOME and SHELL may be over-
       ridden by settings in the crontab; LOGNAME may not.

       (Another note: the LOGNAME variable is sometimes	 called	 USER  on  BSD
       systems...  on these systems, USER will be set also.)

       In addition to LOGNAME, HOME, and SHELL, cron(8) will look at MAILTO if
       it has any reason to send mail as  a  result  of	 running  commands  in
       ``this''	 crontab.   If MAILTO is defined (and non-empty), mail is sent
       to the user so named.  If MAILTO is defined but empty  (MAILTO=""),  no
       mail will be sent.  Otherwise mail is sent to the owner of the crontab.
       This  option  is	 useful	 if  you  decide  on  /bin/mail	  instead   of
       /usr/lib/sendmail  as  your  mailer  when you install cron -- /bin/mail
       doesn't do aliasing, and UUCP usually doesn't read its mail.

       The format of a cron command is very much the V7 standard, with a  num-
       ber  of upward-compatible extensions.  Each line has five time and date
       fields, followed by a user name if this is  the	system	crontab	 file,
       followed	 by  a	command.   Commands  are  executed by cron(8) when the
       minute, hour, and month of year fields match the current time, and when
       at least one of the two day fields (day of month, or day of week) match
       the current time (see ``Note'' below).  Note that this means that  non-
       existant times, such as "missing hours" during daylight savings conver-
       sion, will never match, causing	jobs  scheduled	 during	 the  "missing
       times"  not  to	be  run.   Similarly,  times that occur more than once
       (again, during daylight savings conversion) will cause matching jobs to
       be run twice.

       cron(8) examines cron entries once every minute.

       The time and date fields are:

	      field	     allowed values
	      -----	     --------------
	      minute         0-59
	      hour	         0-23
	      day of month   1-31
	      month	         1-12 (or names, see below)
	      day of week    0-7 (0 or 7 is Sun, or use names)

       A field may be an asterisk (*), which always stands for ``first-last''.

       Ranges of numbers are allowed.  Ranges are two numbers separated with a
       hyphen.	 The  specified	 range is inclusive.  For example, 8-11 for an
       ``hours'' entry specifies execution at hours 8, 9, 10 and 11.

       Lists are allowed.  A list is a set of numbers (or ranges) separated by
       commas.	Examples: ``1,2,5,9'', ``0-4,8-12''.

       Step  values can be used in conjunction with ranges.  Following a range
       with ``/<number>'' specifies skips of the number's  value  through  the
       range.  For example, ``0-23/2'' can be used in the hours field to spec-
       ify command execution every other hour (the alternative in the V7 stan-
       dard  is ``0,2,4,6,8,10,12,14,16,18,20,22'').  Steps are also permitted
       after an asterisk, so if you want to say ``every two hours'', just  use
       ``*/2''.

       Names  can  also	 be used for the ``month'' and ``day of week'' fields.
       Use the first three letters  of	the  particular	 day  or  month	 (case
       doesn't matter).	 Ranges or lists of names are not allowed.

       The  ``sixth'' field (the rest of the line) specifies the command to be
       run.  The entire command portion of the line, up	 to  a	newline	 or  %
       character, will be executed by /bin/sh or by the shell specified in the
       SHELL variable of the cronfile.	 Percent-signs	(%)  in	 the  command,
       unless escaped with backslash (\), will be changed into newline charac-
       ters, and all data after the first % will be sent  to  the  command  as
       standard input.

       Note: The day of a command's execution can be specified by two fields
```
