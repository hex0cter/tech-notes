
date: None  
author(s): None  

# [How to List All Tables and Describe Tables in Oracle - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/database/how-to-list-all-tables-and-describe-tables-in-oracle)

<http://onewebsql.com/blog/list-all-tables>

Connect to the database:

| 

1

| 

`sqlplus username``/password``@database-name`  
  
---|---  
  
To list all tables owned by the current user, type:

1

| 

`select` `tablespace_name, table_name ``from` `user_tables;`  
  
---|---  
  
To list all tables in a database:

1

| 

`select` `tablespace_name, table_name ``from` `dba_tables;`  
  
---|---  
  
To list all tables accessible to the current user, type:

1

| 

`select` `tablespace_name, table_name ``from` `all_tables;`  
  
---|---  
  
You can find more info about views [`all_tables`](http://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_2105.htm), [`user_tables`](http://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_4473.htm#i1635629), and [`dba_tables`](http://docs.oracle.com/cd/B19306_01/server.102/b14237/statviews_4155.htm#i1627762) in Oracle Documentation. To describe a table, type:

