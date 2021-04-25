# [Install Oracle for ruby-oci8 on Ubuntu](http://2muchtea.wordpress.com/2007/12/23/installing-ruby-oci8-on-ubuntu/)

Here is the very nice page describing all the details:

[http://2muchtea.wordpress.com/2007/12/23/installing-ruby-oci8-on-ubuntu/](http://2muchtea.wordpress.com/2007/12/23/installing-ruby-oci8-on-ubuntu/)

In short, download the below packages to somewhere on your system

 **_instantclient-basic-linux-11.2.0.3.0.zip_**

 **_instantclient-sdk-linux-11.2.0.3.0.zip_**

 **_instantclient-sqlplus-linux-11.2.0.3.0.zip_**

and unzip them, say, in /opt/oracle/instantclient_11_2.

Then append the following lines into your .profile or .bashrc:

```
export PATH=$PATH:/opt/oracle/instantclient_11_2:

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/oracle/instantclient_11_2

export ORACLE_HOME=/opt/oracle/instantclient_11_2

export TNS_ADMIN=/opt/oracle/instantclient_11_2
```
Note the orignal post was wrong about envrionment variable TNS_ADMIN. It should be TNS_ADMIN, not TNSADMIN.

Create your tnsnames.ora in /opt/oracle/instantclient_11_2. That's all.

Assume you it looks like this:

```
dbhost=

 (DESCRIPTION =

 (ADDRESS_LIST =

 (ADDRESS = (PROTOCOL = TCP)(HOST = 10.216.21.75)(PORT = 1521))

 )

 (CONNECT_DATA =

 (SERVICE_NAME = DP9A)

 )

 )
```

Now you connect with

`sqlplus username/password@dbhost`

That's all.

---
