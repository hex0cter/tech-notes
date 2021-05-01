# [Embed sqlplus inside a shell script](https://forums.oracle.com/thread/480329)

```
sqlplus system/passwd <<EOF
CONNECT / as sysdba;
shutdown abort;
create database...
EOF
```
