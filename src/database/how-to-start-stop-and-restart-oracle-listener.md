
date: None  
author(s): None  

# [How To Start, Stop and Restart Oracle Listener - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/database/how-to-start-stop-and-restart-oracle-listener)

Starting up and shutting down the oracle listener is a routine task for a database administrator. However a Linux system administrator or programmer may end-up doing some basic DBA operations on development database. It is critical for non-DBAs to understand the basic database admin activities. 

In this article, let us review how to start, stop, check status of an oracle listener using **Oracle listener control utility LSNRCTL**.

Also refer to our earlier article about [how to start and stop the Oracle database](http://www.thegeekstuff.com/2009/01/oracle-database-startup-and-shutdown-procedure/)

## How To Start, Stop and Restart Oracle Listener

### 1\. Display Oracle Listener Status

Before starting, stopping or restarting make sure to execute lsnrctl status command to check the oracle listener status as shown below. Apart from letting us know whether the listener is up or down, you can also find the following valuable information from the lsnrctl status command output.

  * Listner Start Date and Time.
  * Uptime of listner – How long the listener has been up and running.
  * Listener Parameter File – Location of the listener.ora file. Typically located under $ORACLE_HOME/network/admin
  * Listener Log File – Location of the listener log file. i.e log.xml



  
If the Oracle listener is not running, you’ll get the following message.
    
    
    $ **lsnrctl status**
    LSNRCTL for Linux: Version 11.1.0.6.0 - Production on 04-APR-2009 16:27:39
    
    Copyright (c) 1991, 2007, Oracle.  All rights reserved.
    
    Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.2)(PORT=1521)))
    TNS-12541: TNS:no listener
     TNS-12560: TNS:protocol adapter error
      TNS-00511: No listener
       Linux Error: 111: Connection refused
    Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=EXTPROC)))
    TNS-12541: TNS:no listener
     TNS-12560: TNS:protocol adapter error
      TNS-00511: No listener
       Linux Error: 2: No such file or directory

  
If the Oracle listener is running, you’ll get the following message.
    
    
    $ **lsnrctl status**
    LSNRCTL for Linux: Version 11.1.0.6.0 - Production on 04-APR-2009 16:27:02
    
    Copyright (c) 1991, 2007, Oracle.  All rights reserved.
    
    Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.2)(PORT=1521)))
    STATUS of the LISTENER
    ------------------------
    Alias                     LISTENER
    Version                   TNSLSNR for Linux: Version 11.1.0.6.0 - Production
    Start Date                29-APR-2009 18:43:13
    Uptime                    6 days 21 hr. 43 min. 49 sec
    Trace Level               off
    Security                  ON: Local OS Authentication
    SNMP                      OFF
    Listener Parameter File   /u01/app/oracle/product/11.1.0/network/admin/listener.ora
    Listener Log File         /u01/app/oracle/diag/tnslsnr/devdb/listener/alert/log.xml
    Listening Endpoints Summary...
      (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=192.168.1.2)(PORT=1521)))
      (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC)))
    Services Summary...
    Service "devdb" has 1 instance(s).
      Instance "devdb", status UNKNOWN, has 1 handler(s) for this service...
    Service "devdb.thegeekstuff.com" has 1 instance(s).
      Instance "devdb", status READY, has 1 handler(s) for this service...
    Service "devdbXDB.thegeekstuff.com" has 1 instance(s).
      Instance "devdb", status READY, has 1 handler(s) for this service...
    Service "devdb_XPT.thegeekstuff.com" has 1 instance(s).
      Instance "devdb", status READY, has 1 handler(s) for this service...
    The command completed successfully

### 2\. Start Oracle Listener

If the Oracle listener is not running, start the listener as shown below. This will start all the listeners. If you want to start a specific listener, specify the listener name next to start. i.e lsnrctl start [listener-name]
    
    
    $ **lsnrctl start**
    LSNRCTL for Linux: Version 11.1.0.6.0 - Production on 04-APR-2009 16:27:42
    
    Copyright (c) 1991, 2007, Oracle.  All rights reserved.
    
    Starting /u01/app/oracle/product/11.1.0/bin/tnslsnr: please wait...
    
    TNSLSNR for Linux: Version 11.1.0.6.0 - Production
    System parameter file is /u01/app/oracle/product/11.1.0/network/admin/listener.ora
    Log messages written to /u01/app/oracle/diag/tnslsnr/devdb/listener/alert/log.xml
    Listening on: (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=192.168.1.2)(PORT=1521)))
    Listening on: (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC)))
    
    Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.2)(PORT=1521)))
    STATUS of the LISTENER
    ------------------------
    Alias                     LISTENER
    Version                   TNSLSNR for Linux: Version 11.1.0.6.0 - Production
    Start Date                04-APR-2009 16:27:42
    Uptime                    0 days 0 hr. 0 min. 0 sec
    Trace Level               off
    Security                  ON: Local OS Authentication
    SNMP                      OFF
    Listener Parameter File   /u01/app/oracle/product/11.1.0/network/admin/listener.ora
    Listener Log File         /u01/app/oracle/diag/tnslsnr/devdb/listener/alert/log.xml
    Listening Endpoints Summary...
      (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=192.168.1.2)(PORT=1521)))
      (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC)))
    Services Summary...
    Service "devdb" has 1 instance(s).
      Instance "devdb", status UNKNOWN, has 1 handler(s) for this service...
    The command completed successfully

### 3\. Stop Oracle Listener

If the Oracle listener is running, stop the listener as shown below. This will stop all the listeners. If you want to stop a specific listener, specify the listener name next to stop. i.e lsnrctl stop [listener-name]
    
    
    $ **lsnrctl stop**
    LSNRCTL for Linux: Version 11.1.0.6.0 - Production on 04-APR-2009 16:27:37
    
    Copyright (c) 1991, 2007, Oracle.  All rights reserved.
    
    Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.2)(PORT=1521)))
    The command completed successfully

### 4\. Restart Oracle Listener

To restart the listener use lsnrctl reload as shown below instead of lsnrctl stop and lsnrctl start. realod will read the listener.ora file for new setting without stop and start of the Oracle listener.  

    
    
    $ **lsnrctl reload**
    LSNRCTL for Linux: Version 11.1.0.6.0 - Production on 04-APR-2009 17:03:31
    
    Copyright (c) 1991, 2007, Oracle.  All rights reserved.
    
    Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.1.2)(PORT=1521)))
    The command completed successfully

## Oracle Listener Help

### 1\. View Available Listener Commands

lsnrctl help command will display all available listener commands. In Oracle 11g following are the available listener commands.

  * **start** \- Start the Oracle listener
  * **stop** \- Stop the Oracle listener
  * **status** \- Display the current status of the Oracle listener
  * **services** \- Retrieve the listener services information
  * **version** \- Display the oracle listener version information
  * **reload** \- This will reload the oracle listener SID and parameter files. This is equivalent to lsnrctl stop and lsnrctl start.
  * **save_config** – This will save the current settings to the listener.ora file and also take a backup of the listener.ora file before overwriting it. If there are no changes, it will display the message “No changes to save for LISTENER”
  * **trace** \- Enable the tracing at the listener level. The available options are ‘trace OFF’, ‘trace USER’, ‘trace ADMIN’ or ‘trace SUPPORT’
  * **spawn** \- Spawns a new with the program with the spawn_alias mentioned in the listener.ora file
  * **change_password** – Set the new password to the oracle listener (or) change the existing listener password.
  * **show** \- Display log files and other relevant listener information.


    
    
    $ **lsnrctl help**
    LSNRCTL for Linux: Version 11.1.0.6.0 - Production on 04-APR-2009 16:12:09
    
    Copyright (c) 1991, 2007, Oracle.  All rights reserved.
    
    The following operations are available
    An asterisk (*) denotes a modifier or extended command:
    
    start               stop                status
    services            version             reload
    save_config         trace               spawn
    change_password     quit                exit
    set*                show*

### 2\. Get More help on Specific Listener Command

You can get detailed help on a specific oracle listener command as shown below. In the following example, it gives all the available arguments/parameters that can be passed to the lsnrctl show command.
    
    
    $ **lsnrctl help show**
    LSNRCTL for Linux: Version 11.1.0.6.0 - Production on 04-APR-2009 16:22:28
    
    Copyright (c) 1991, 2007, Oracle.  All rights reserved.
    
    The following operations are available after show
    An asterisk (*) denotes a modifier or extended command:
    
    rawmode                     displaymode
    rules                       trc_file
    trc_directory               trc_level
    log_file                    log_directory
    log_status                  current_listener
    inbound_connect_timeout     startup_waittime
    snmp_visible                save_config_on_stop
    dynamic_registration

  


