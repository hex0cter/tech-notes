# [How to schedule tasks using Linux at command](http://www.omnisecu.com/gnu-linux/redhat-certified-engineer-rhce/how-to-schedule-tasks-using-linux-at-command.php)

The Linux “at” command also can be used for scheduling jobs. But using Linux “at” command, you can set the job run only once. The “at” jobs are spooled in the “/var/spool/at” directory and run at the specified time.

The “at” daemon can be used to run a command or script of your choice. From the command line, you can run the “at” time command to start a job to be run at a specified time. That time can be now; in a specified number of minutes, hours, or days; or at the time of your choice.

To schedule a one-time job at a specific time, type the command at time, where time is the time to execute the command.

The Linux at command argument time can be one of the following:


• HH:MM format — For example, 04:00 specifies 4:00AM. If the time is already past, it is executed at the specified time the next day.

• midnight — Specifies 12:00AM.

• noon — Specifies 12:00PM.

• teatime — Specifies 4:00PM.

• month-name day year format — For example, January 15 2002 specifies the 15th day of January in the year 2002. The year is optional.


• MMDDYY, MM/DD/YY, or MM.DD.YY formats — For example, 011502 for the 15th day of January in the year 2002.


• now + time — time is in minutes, hours, days, or weeks. For example, now + 5 days specifies that the command should be executed at the same time in five days.

###  _Linux at command examples_

 **Command Example** | **Description**
---|---
at now + 10 minutes | Associated jobs will start in 10 minutes.
at now + 2 hours | Associated jobs will start in 2 hours.
at now + 1 day | Associated jobs will start in 1 day (24 hours).
at now + 1 week | Associated jobs will start in 7 days.
at teatime | Associated jobs will start at 4:00 P.M.
at 3:00 6/13/07 | Associated jobs will start on June 13, 2007, at 3:00 A.M.

###  _The Linux at command permission files (/etc/at.allow and /etc/at.deny)_

For normal users, permission to use at command is determined by the files /etc/at.allow and /etc/at.deny.

If the file /etc/at.allow exists, only usernames mentioned in it are allowed to use at.

If /etc/at.allow does not exist, /etc/at.deny is checked, every user name not mentioned in it is then allowed to use at.

If neither exists, only the superuser is allowed use of at.

An empty /etc/at.deny means that every user is allowed use these commands, this is the default configuration.


###  _The Linux atq and atrm commands_

The Linux atq command lists the user’s pending jobs, unless the user is the superuser; in that case, everybody’s jobs are listed. The format of the output lines (one for each job) is: Job number, date, hour, job class.

The Linux atrm command deletes the scheduled jobs, identified by their job number.
