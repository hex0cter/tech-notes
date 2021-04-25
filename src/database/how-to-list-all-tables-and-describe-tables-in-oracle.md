# [How to List All Tables and Describe Tables in Oracle](http://onewebsql.com/blog/list-all-tables)

Connect to the database:

`sqlplus username/password@database-name`

To list all tables owned by the current user, type:

`select tablespace_name, table_name from user_tables;`

To list all tables in a database:

`select tablespace_name, table_name from dba_tables;`

To list all tables accessible to the current user, type:

`select tablespace_name, table_name from all_tables;`
