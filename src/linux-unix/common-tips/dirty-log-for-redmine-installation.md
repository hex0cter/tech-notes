# dirty log for redmine installation

```
daniel@danielhan-IdeaPad-U150:~$ sudo apt-get install ruby
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
  libjs-jquery libruby2.1 libyaml-0-2 ruby2.1 rubygems-integration
Suggested packages:
  javascript-common ri ruby-dev bundler
The following NEW packages will be installed:
  libjs-jquery libruby2.1 libyaml-0-2 ruby ruby2.1 rubygems-integration
0 upgraded, 6 newly installed, 0 to remove and 7 not upgraded.
Need to get 3,297 kB/3,425 kB of archives.
After this operation, 16.6 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://se.archive.ubuntu.com/ubuntu/ utopic-updates/main libruby2.1 i386 2.1.2-2ubuntu1.2 [3,226 kB]
Get:2 http://se.archive.ubuntu.com/ubuntu/ utopic-updates/main ruby2.1 i386 2.1.2-2ubuntu1.2 [70.7 kB]
Fetched 3,297 kB in 2s (1,176 kB/s)
Selecting previously unselected package libyaml-0-2:i386.
(Reading database ... 187904 files and directories currently installed.)
Preparing to unpack .../libyaml-0-2_0.1.6-1_i386.deb ...
Unpacking libyaml-0-2:i386 (0.1.6-1) ...
Selecting previously unselected package libjs-jquery.
Preparing to unpack .../libjs-jquery_1.7.2+dfsg-3ubuntu2_all.deb ...
Unpacking libjs-jquery (1.7.2+dfsg-3ubuntu2) ...
Selecting previously unselected package rubygems-integration.
Preparing to unpack .../rubygems-integration_1.7_all.deb ...
Unpacking rubygems-integration (1.7) ...
Selecting previously unselected package libruby2.1:i386.
Preparing to unpack .../libruby2.1_2.1.2-2ubuntu1.2_i386.deb ...
Unpacking libruby2.1:i386 (2.1.2-2ubuntu1.2) ...
Selecting previously unselected package ruby2.1.
Preparing to unpack .../ruby2.1_2.1.2-2ubuntu1.2_i386.deb ...
Unpacking ruby2.1 (2.1.2-2ubuntu1.2) ...
Selecting previously unselected package ruby.
Preparing to unpack .../ruby_1%3a2.1.0.0~ubuntu3_all.deb ...
Unpacking ruby (1:2.1.0.0~ubuntu3) ...
Processing triggers for man-db (2.7.0.2-2) ...
Setting up libyaml-0-2:i386 (0.1.6-1) ...
Setting up libjs-jquery (1.7.2+dfsg-3ubuntu2) ...
Setting up rubygems-integration (1.7) ...
Setting up ruby2.1 (2.1.2-2ubuntu1.2) ...
Setting up ruby (1:2.1.0.0~ubuntu3) ...
Setting up libruby2.1:i386 (2.1.2-2ubuntu1.2) ...
Processing triggers for libc-bin (2.19-10ubuntu2) ...
daniel@danielhan-IdeaPad-U150:~$ ruby --version
ruby 2.1.2p95 (2014-05-08) [i386-linux-gnu]
daniel@danielhan-IdeaPad-U150:~$ gem install mysql2
Fetching: mysql2-0.3.17.gem (100%)
ERROR:  While executing gem ... (Errno::EACCES)
    Permission denied @ dir_s_mkdir - /var/lib/gems
daniel@danielhan-IdeaPad-U150:~$ sudo gem install mysql2
Fetching: mysql2-0.3.17.gem (100%)
Building native extensions.  This could take a while...
ERROR:  Error installing mysql2:
    ERROR: Failed to build gem native extension.

    /usr/bin/ruby2.1 extconf.rb
mkmf.rb can't find header files for ruby at /usr/lib/ruby/include/ruby.h

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/2.1.0/gems/mysql2-0.3.17 for inspection.
Results logged to /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/gem_make.out
daniel@danielhan-IdeaPad-U150:~$ sudo apt-get install ruby-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
  libgmp-dev libgmpxx4ldbl ruby2.1-dev
Suggested packages:
  libgmp10-doc libmpfr-dev
The following NEW packages will be installed:
  libgmp-dev libgmpxx4ldbl ruby-dev ruby2.1-dev
0 upgraded, 4 newly installed, 0 to remove and 7 not upgraded.
Need to get 1,298 kB of archives.
After this operation, 5,332 kB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://se.archive.ubuntu.com/ubuntu/ utopic/main libgmpxx4ldbl i386 2:6.0.0+dfsg-4build1 [9,296 B]
Get:2 http://se.archive.ubuntu.com/ubuntu/ utopic/main libgmp-dev i386 2:6.0.0+dfsg-4build1 [313 kB]
Get:3 http://se.archive.ubuntu.com/ubuntu/ utopic-updates/main ruby2.1-dev i386 2.1.2-2ubuntu1.2 [971 kB]
Get:4 http://se.archive.ubuntu.com/ubuntu/ utopic/main ruby-dev all 1:2.1.0.0~ubuntu3 [4,484 B]
Fetched 1,298 kB in 0s (1,375 kB/s)
Selecting previously unselected package libgmpxx4ldbl:i386.
(Reading database ... 188995 files and directories currently installed.)
Preparing to unpack .../libgmpxx4ldbl_2%3a6.0.0+dfsg-4build1_i386.deb ...
Unpacking libgmpxx4ldbl:i386 (2:6.0.0+dfsg-4build1) ...
Selecting previously unselected package libgmp-dev:i386.
Preparing to unpack .../libgmp-dev_2%3a6.0.0+dfsg-4build1_i386.deb ...
Unpacking libgmp-dev:i386 (2:6.0.0+dfsg-4build1) ...
Selecting previously unselected package ruby2.1-dev:i386.
Preparing to unpack .../ruby2.1-dev_2.1.2-2ubuntu1.2_i386.deb ...
Unpacking ruby2.1-dev:i386 (2.1.2-2ubuntu1.2) ...
Selecting previously unselected package ruby-dev.
Preparing to unpack .../ruby-dev_1%3a2.1.0.0~ubuntu3_all.deb ...
Unpacking ruby-dev (1:2.1.0.0~ubuntu3) ...
Setting up libgmpxx4ldbl:i386 (2:6.0.0+dfsg-4build1) ...
Setting up libgmp-dev:i386 (2:6.0.0+dfsg-4build1) ...
Setting up ruby2.1-dev:i386 (2.1.2-2ubuntu1.2) ...
Setting up ruby-dev (1:2.1.0.0~ubuntu3) ...
Processing triggers for libc-bin (2.19-10ubuntu2) ...
daniel@danielhan-IdeaPad-U150:~$ sudo gem install mysql2
Building native extensions.  This could take a while...
ERROR:  Error installing mysql2:
    ERROR: Failed to build gem native extension.

    /usr/bin/ruby2.1 extconf.rb
checking for ruby/thread.h... yes
checking for rb_thread_call_without_gvl() in ruby/thread.h... yes
checking for rb_thread_blocking_region()... yes
checking for rb_wait_for_single_fd()... yes
checking for rb_hash_dup()... yes
checking for rb_intern3()... yes
checking for mysql_query() in -lmysqlclient... no
checking for main() in -lm... yes
checking for mysql_query() in -lmysqlclient... no
checking for main() in -lz... no
checking for mysql_query() in -lmysqlclient... no
checking for main() in -lsocket... no
checking for mysql_query() in -lmysqlclient... no
checking for main() in -lnsl... yes
checking for mysql_query() in -lmysqlclient... no
checking for main() in -lmygcc... no
checking for mysql_query() in -lmysqlclient... no
*** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
    --with-opt-dir
    --without-opt-dir
    --with-opt-include
    --without-opt-include=${opt-dir}/include
    --with-opt-lib
    --without-opt-lib=${opt-dir}/lib
    --with-make-prog
    --without-make-prog
    --srcdir=.
    --curdir
    --ruby=/usr/bin/ruby2.1
    --with-mysql-dir
    --without-mysql-dir
    --with-mysql-include
    --without-mysql-include=${mysql-dir}/include
    --with-mysql-lib
    --without-mysql-lib=${mysql-dir}/lib
    --with-mysql-config
    --without-mysql-config
    --with-mysql-dir
    --without-mysql-dir
    --with-mysql-include
    --without-mysql-include=${mysql-dir}/include
    --with-mysql-lib
    --without-mysql-lib=${mysql-dir}/lib
    --with-mysqlclientlib
    --without-mysqlclientlib
    --with-mlib
    --without-mlib
    --with-mysqlclientlib
    --without-mysqlclientlib
    --with-zlib
    --without-zlib
    --with-mysqlclientlib
    --without-mysqlclientlib
    --with-socketlib
    --without-socketlib
    --with-mysqlclientlib
    --without-mysqlclientlib
    --with-nsllib
    --without-nsllib
    --with-mysqlclientlib
    --without-mysqlclientlib
    --with-mygcclib
    --without-mygcclib
    --with-mysqlclientlib
    --without-mysqlclientlib

extconf failed, exit code 1

Gem files will remain installed in /var/lib/gems/2.1.0/gems/mysql2-0.3.17 for inspection.
Results logged to /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/gem_make.out
daniel@danielhan-IdeaPad-U150:~$ ls
'                                              partitions
Angels & Demons - Dan Brown.mobi               Pictures
Backup                                         ps
bin                                            Public
blanket                                        recovery.img
Calibre Library                                settings.db
Desktop                                        speedup
disk.diff                                      SSK.list
Documents                                      SSK-sorted.list
Downloads                                      STB
Dropbox                                        stb-open-ports
FAT.list                                       Templates
FAT-sorted.list                                tmp
gi-de                                          UDF Volume-0.iso
gi-de.tar.gz                                   UDF Volume.iso
Git                                            Untitled1.abw.saved
google-cloud-sdk                               Update_kindle_5.3.2.1.bin
GT-I9100_JB_ClockworkMod-Recovery_6.0.2.9.tar  Videos
M310                                           VMs
mbr.img                                        Windows7-Zhongcong.iso
mbr-tip.txt                                    workspace
mbr-xubuntu-winxp.img                          wuyuanhang
Music                                          zImage.xx
output.mkv
daniel@danielhan-IdeaPad-U150:~$ ls mkmf.log
ls: cannot access mkmf.log: No such file or directory
daniel@danielhan-IdeaPad-U150:~$ vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/g
daniel@danielhan-IdeaPad-U150:~$ vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/gem_make.out
daniel@danielhan-IdeaPad-U150:~$ vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/
gem_make.out  mkmf.log
daniel@danielhan-IdeaPad-U150:~$ vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/mkmf.log daniel@danielhan-IdeaPad-U150:~$ ld
ld: no input files
daniel@danielhan-IdeaPad-U150:~$ vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/mkmf.log
daniel@danielhan-IdeaPad-U150:~$ mysqlclient
mysqlclient: command not found
daniel@danielhan-IdeaPad-U150:~$ apt-cache search mysqlclient
libmysqlclient-dev - MySQL database development files
libmysqlclient18 - MySQL database client library
kbtin - tintin++ style text-based MUD client
libcrypt-mysql-perl - Perl module to emulate the MySQL PASSWORD() function
libglpk36 - linear programming kit with integer (MIP) support
daniel@danielhan-IdeaPad-U150:~$ sudo apt-get libmysqlclient-dev libmysqlclient18
[sudo] password for daniel:
daniel@danielhan-IdeaPad-U150:~$ sudo apt-get install libmysqlclient-dev libmysqlclient18
[sudo] password for daniel:
Reading package lists... Done
Building dependency tree
Reading state information... Done
libmysqlclient18 is already the newest version.
libmysqlclient18 set to manually installed.
The following NEW packages will be installed:
  libmysqlclient-dev zlib1g-dev
0 upgraded, 2 newly installed, 0 to remove and 7 not upgraded.
Need to get 1,086 kB of archives.
After this operation, 5,790 kB of additional disk space will be used.
Get:1 http://se.archive.ubuntu.com/ubuntu/ utopic/main zlib1g-dev i386 1:1.2.8.dfsg-1ubuntu1 [181 kB]
Get:2 http://se.archive.ubuntu.com/ubuntu/ utopic/main libmysqlclient-dev i386 5.5.40-0ubuntu1 [906 kB]
Fetched 1,086 kB in 0s (1,466 kB/s)
Selecting previously unselected package zlib1g-dev:i386.
(Reading database ... 191842 files and directories currently installed.)
Preparing to unpack .../zlib1g-dev_1%3a1.2.8.dfsg-1ubuntu1_i386.deb ...
Unpacking zlib1g-dev:i386 (1:1.2.8.dfsg-1ubuntu1) ...
Selecting previously unselected package libmysqlclient-dev.
Preparing to unpack .../libmysqlclient-dev_5.5.40-0ubuntu1_i386.deb ...
Unpacking libmysqlclient-dev (5.5.40-0ubuntu1) ...
Processing triggers for man-db (2.7.0.2-2) ...
Setting up zlib1g-dev:i386 (1:1.2.8.dfsg-1ubuntu1) ...
Setting up libmysqlclient-dev (5.5.40-0ubuntu1) ...
daniel@danielhan-IdeaPad-U150:~$ sudo gem install mysql2
Building native extensions.  This could take a while...
Successfully installed mysql2-0.3.17
Parsing documentation for mysql2-0.3.17
Installing ri documentation for mysql2-0.3.17
Done installing documentation for mysql2 after 0 seconds
1 gem installed
daniel@danielhan-IdeaPad-U150:~$ cd Documents/
daniel@danielhan-IdeaPad-U150:~/Documents$ s
s: command not found
daniel@danielhan-IdeaPad-U150:~/Documents$ ks
ks: command not found
daniel@danielhan-IdeaPad-U150:~/Documents$ ls
1.txt                   Dan Brown - Angels and Demons.mobi  ER-CA70、ER-CA65、ER-CA35使用说明书.pdf  issurance  Manual_Nordea_Eng.pdf      Out of Africa.txt                       thinkpython.pdf
2.txt                   emma-pspt.pdf                       housing                                  klarna     Meego-1.2-Notebook.tar.gz  rynair.txt                              英语发音入门.doc
bookmarks_8_19_14.html  emma.xcf                            hwinfo                                   lshw       nokia-sd                   sogou_pinyin_linux_1.1.0.0037_i386.deb  英语发音入门.odt
daniel@danielhan-IdeaPad-U150:~/Documents$ cd klarna/
daniel@danielhan-IdeaPad-U150:~/Documents/klarna$ ls
redmine-2.6.0
daniel@danielhan-IdeaPad-U150:~/Documents/klarna$ cd redmine-2.6.0/
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ s
s: command not found
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ ks
ks: command not found
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ ls
app  config  config.ru  CONTRIBUTING.md  db  doc  extra  files  Gemfile  lib  log  plugins  public  Rakefile  README.rdoc  script  test  tmp  vendor
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ sudo apt-get install mysql-server
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
  libaio1 libdbd-mysql-perl libdbi-perl libhtml-template-perl libterm-readkey-perl mysql-client-5.5 mysql-client-core-5.5 mysql-server-5.5 mysql-server-core-5.5
Suggested packages:
  libmldbm-perl libnet-daemon-perl libsql-statement-perl libipc-sharedcache-perl tinyca mailx
The following NEW packages will be installed:
  libaio1 libdbd-mysql-perl libdbi-perl libhtml-template-perl libterm-readkey-perl mysql-client-5.5 mysql-client-core-5.5 mysql-server mysql-server-5.5 mysql-server-core-5.5
0 upgraded, 10 newly installed, 0 to remove and 7 not upgraded.
Need to get 9,058 kB of archives.
After this operation, 92.2 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://se.archive.ubuntu.com/ubuntu/ utopic/main libaio1 i386 0.3.110-1 [6,790 B]
Get:2 http://se.archive.ubuntu.com/ubuntu/ utopic/main libdbi-perl i386 1.631-3build1 [774 kB]
Get:3 http://se.archive.ubuntu.com/ubuntu/ utopic/main libdbd-mysql-perl i386 4.028-2 [93.0 kB]
Get:4 http://se.archive.ubuntu.com/ubuntu/ utopic/main libterm-readkey-perl i386 2.32-1build1 [26.0 kB]
Get:5 http://se.archive.ubuntu.com/ubuntu/ utopic/main mysql-client-core-5.5 i386 5.5.40-0ubuntu1 [731 kB]
Get:6 http://se.archive.ubuntu.com/ubuntu/ utopic/main mysql-client-5.5 i386 5.5.40-0ubuntu1 [1,505 kB]
Get:7 http://se.archive.ubuntu.com/ubuntu/ utopic/main mysql-server-core-5.5 i386 5.5.40-0ubuntu1 [3,796 kB]
Get:8 http://se.archive.ubuntu.com/ubuntu/ utopic/main mysql-server-5.5 i386 5.5.40-0ubuntu1 [2,048 kB]
Get:9 http://se.archive.ubuntu.com/ubuntu/ utopic/main libhtml-template-perl all 2.95-1 [65.5 kB]
Get:10 http://se.archive.ubuntu.com/ubuntu/ utopic/main mysql-server all 5.5.40-0ubuntu1 [12.4 kB]
Fetched 9,058 kB in 5s (1,531 kB/s)
Preconfiguring packages ...
Selecting previously unselected package libaio1:i386.
(Reading database ... 191938 files and directories currently installed.)
Preparing to unpack .../libaio1_0.3.110-1_i386.deb ...
Unpacking libaio1:i386 (0.3.110-1) ...
Selecting previously unselected package libdbi-perl.
Preparing to unpack .../libdbi-perl_1.631-3build1_i386.deb ...
Unpacking libdbi-perl (1.631-3build1) ...
Selecting previously unselected package libdbd-mysql-perl.
Preparing to unpack .../libdbd-mysql-perl_4.028-2_i386.deb ...
Unpacking libdbd-mysql-perl (4.028-2) ...
Selecting previously unselected package libterm-readkey-perl.
Preparing to unpack .../libterm-readkey-perl_2.32-1build1_i386.deb ...
Unpacking libterm-readkey-perl (2.32-1build1) ...
Selecting previously unselected package mysql-client-core-5.5.
Preparing to unpack .../mysql-client-core-5.5_5.5.40-0ubuntu1_i386.deb ...
Unpacking mysql-client-core-5.5 (5.5.40-0ubuntu1) ...
Selecting previously unselected package mysql-client-5.5.
Preparing to unpack .../mysql-client-5.5_5.5.40-0ubuntu1_i386.deb ...
Unpacking mysql-client-5.5 (5.5.40-0ubuntu1) ...
Selecting previously unselected package mysql-server-core-5.5.
Preparing to unpack .../mysql-server-core-5.5_5.5.40-0ubuntu1_i386.deb ...
Unpacking mysql-server-core-5.5 (5.5.40-0ubuntu1) ...
Selecting previously unselected package mysql-server-5.5.
Preparing to unpack .../mysql-server-5.5_5.5.40-0ubuntu1_i386.deb ...
Unpacking mysql-server-5.5 (5.5.40-0ubuntu1) ...
Selecting previously unselected package libhtml-template-perl.
Preparing to unpack .../libhtml-template-perl_2.95-1_all.deb ...
Unpacking libhtml-template-perl (2.95-1) ...
Selecting previously unselected package mysql-server.
Preparing to unpack .../mysql-server_5.5.40-0ubuntu1_all.deb ...
Unpacking mysql-server (5.5.40-0ubuntu1) ...
Processing triggers for man-db (2.7.0.2-2) ...
Processing triggers for ureadahead (0.100.0-16) ...
Setting up libaio1:i386 (0.3.110-1) ...
Setting up libdbi-perl (1.631-3build1) ...
Setting up libdbd-mysql-perl (4.028-2) ...
Setting up libterm-readkey-perl (2.32-1build1) ...
Setting up mysql-client-core-5.5 (5.5.40-0ubuntu1) ...
Setting up mysql-client-5.5 (5.5.40-0ubuntu1) ...
Setting up mysql-server-core-5.5 (5.5.40-0ubuntu1) ...
Setting up mysql-server-5.5 (5.5.40-0ubuntu1) ...
141126 22:57:13 [Warning] Using unique option prefix key_buffer instead of key_buffer_size is deprecated and will be removed in a future release. Please use the full name instead.
mysql start/running, process 10182
Setting up libhtml-template-perl (2.95-1) ...
Processing triggers for ureadahead (0.100.0-16) ...
Setting up mysql-server (5.5.40-0ubuntu1) ...
Processing triggers for libc-bin (2.19-10ubuntu2) ...
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ mysql -u root -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.5.40-0ubuntu1 (Ubuntu)

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)

mysql> CREATE DATABASE redmine CHARACTER SET utf8;
Query OK, 1 row affected (0.00 sec)

mysql> CREATE USER 'redmine'@'localhost' IDENTIFIED BY 'my_password';
Query OK, 0 rows affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON redmine.* TO 'redmine'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> quit
Bye
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ gem install bundler
Fetching: bundler-1.7.7.gem (100%)
ERROR:  While executing gem ... (Gem::FilePermissionError)
    You don't have write permissions for the /var/lib/gems/2.1.0 directory.
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ sudo gem install bundler
Fetching: bundler-1.7.7.gem (100%)
Successfully installed bundler-1.7.7
Parsing documentation for bundler-1.7.7
Installing ri documentation for bundler-1.7.7
Done installing documentation for bundler after 8 seconds
1 gem installed
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ bundle install --without development test
Fetching gem metadata from https://rubygems.org/.........
Resolving dependencies...
Installing rake 10.4.0
Installing i18n 0.6.11
Installing multi_json 1.10.1
Installing activesupport 3.2.19
Installing builder 3.0.4
Installing activemodel 3.2.19
Installing erubis 2.7.0
Installing journey 1.0.4
Installing rack 1.4.5
Installing rack-cache 1.2
Installing rack-test 0.6.2
Installing hike 1.2.3
Installing tilt 1.4.1
Installing sprockets 2.2.3
Installing actionpack 3.2.19
Installing mime-types 1.25.1
Installing polyglot 0.3.5
Installing treetop 1.4.15
Installing mail 2.5.4
Installing actionmailer 3.2.19
Installing arel 3.0.3
Installing tzinfo 0.3.42
Installing activerecord 3.2.19
Installing activeresource 3.2.19
Using bundler 1.7.7
Installing coderay 1.1.0
Installing rack-ssl 1.3.4
Using json 1.8.1
Installing rdoc 3.12.2
Installing thor 0.19.1
Installing railties 3.2.19
Installing jquery-rails 3.1.2
Using mysql2 0.3.17
Installing net-ldap 0.3.1
Installing ruby-openid 2.3.0
Installing rack-openid 1.4.2
Installing rails 3.2.19
Installing rbpdf 1.18.2
Installing redcarpet 2.3.0
Installing request_store 1.0.5

Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    /usr/bin/ruby2.1 extconf.rb
checking for Ruby version >= 1.8.5... yes
checking for gcc... yes
checking for Magick-config... no
checking for pkg-config... yes
checking for ImageMagick version >= 6.4.9... *** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
    --with-opt-dir
    --without-opt-dir
    --with-opt-include
    --without-opt-include=${opt-dir}/include
    --with-opt-lib
    --without-opt-lib=${opt-dir}/lib
    --with-make-prog
    --without-make-prog
    --srcdir=.
    --curdir
    --ruby=/usr/bin/ruby2.1
extconf.rb:154:in ``': No such file or directory - convert (Errno::ENOENT)
    from extconf.rb:154:in `block in <main>'
    from /usr/lib/ruby/2.1.0/mkmf.rb:918:in `block in checking_for'
    from /usr/lib/ruby/2.1.0/mkmf.rb:351:in `block (2 levels) in postpone'
    from /usr/lib/ruby/2.1.0/mkmf.rb:321:in `open'
    from /usr/lib/ruby/2.1.0/mkmf.rb:351:in `block in postpone'
    from /usr/lib/ruby/2.1.0/mkmf.rb:321:in `open'
    from /usr/lib/ruby/2.1.0/mkmf.rb:347:in `postpone'
    from /usr/lib/ruby/2.1.0/mkmf.rb:917:in `checking_for'
    from extconf.rb:151:in `<main>'

extconf failed, exit code 1

Gem files will remain installed in /tmp/bundler20141126-10420-iqpl66/rmagick-2.13.4/gems/rmagick-2.13.4 for inspection.
Results logged to /tmp/bundler20141126-10420-iqpl66/rmagick-2.13.4/extensions/x86-linux/2.1.0/rmagick-2.13.4/gem_make.out
An error occurred while installing rmagick (2.13.4), and Bundler cannot continue.
Make sure that `gem install rmagick -v '2.13.4'` succeeds before bundling.
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/mkmf.log
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ vi /tmp/bundler20141126-10420-iqpl66/rmagick-2.13.4/extensions/x86-linux/2.1.0/rmagick-2.13.4/gem_make.out
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ gem install rmagick -v '2.13.4'
Fetching: rmagick-2.13.4.gem (100%)
ERROR:  While executing gem ... (Gem::FilePermissionError)
    You don't have write permissions for the /var/lib/gems/2.1.0 directory.
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ apt-cache search ImageMagick
groff - GNU troff text-formatting system
imagemagick - image manipulation programs
imagemagick-common - image manipulation programs -- infrastructure
imagemagick-dbg - debugging symbols for ImageMagick
imagemagick-doc - document files of ImageMagick
libmagick++-dev - object-oriented C++ interface to ImageMagick - development files
libmagick++5 - object-oriented C++ interface to ImageMagick
libmagickcore5 - low-level image manipulation library
libmagickwand5 - image manipulation library
perlmagick - Perl interface to the ImageMagick graphics routines
caja-image-converter - Caja extension to mass resize or rotate images
epix - Create mathematically accurate line figures, plots and movies
fbi - Linux frame buffer image viewer
gambas3-gb-image - Gambas image effects
gem-plugin-magick - Graphics Environment for Multimedia - ImageMagick support
gkrellshoot - Plugin for gkrellm to lock the screen and make screenshots
goby - WYSIWYG presentation tool for Emacs
graphicsmagick - collection of image processing tools
graphicsmagick-dbg - format-independent image processing - debugging symbols
graphicsmagick-imagemagick-compat - image processing tools providing ImageMagick interface
graphicsmagick-libmagick-dev-compat - image processing libraries providing ImageMagick interface
imageinfo - Displays selected image attributes
imgsizer - Adds WIDTH and HEIGHT attributes to IMG tags in HTML files
jmagick6-docs - java interface to ImageMagick - api documentation
libchart-gnuplot-perl - module for generating two- and three-dimensional plots
libgraphics-magick-perl - format-independent image processing - perl interface
libgraphicsmagick++1-dev - format-independent image processing - C++ development files
libgraphicsmagick++3 - format-independent image processing - C++ shared library
libgraphicsmagick1-dev - format-independent image processing - C development files
libgraphicsmagick3 - format-independent image processing - C shared library
libjmagick6-java - java interface to ImageMagick - java classes
libjmagick6-jni - java interface to ImageMagick - native library
libreoffice - office productivity suite (metapackage)
libvips-dev - image processing system good for very large images (dev)
libvips-doc - image processing system good for very large images (doc)
libvips-tools - image processing system good for very large images (tools)
libvips37 - image processing system good for very large images
nautilus-image-converter - nautilus extension to mass resize or rotate images
nip2 - spreadsheet-like graphical image manipulation tool
octave-image - image manipulation for Octave
php-horde-image - Horde Image API
php5-imagick - ImageMagick module for php5
pypy-wand - Python interface for ImageMagick library (PyPy build)
python-pythonmagick - Object-oriented Python interface to ImageMagick
python-sorl-thumbnail - thumbnail support for the Django framework
python-vipscc - image processing system good for very large images (tools)
python-wand - Python interface for ImageMagick library (Python 2 build)
python3-wand - Python interface for ImageMagick library (Python 3 build)
ruby-mini-magick - wrapper for ImageMagick with a small memory footprint
ruby-oily-png - native mixin to speed up ChunkyPNG
ruby-rmagick - ImageMagick API for Ruby
ruby-rmagick-doc - ImageMagick API for Ruby (documentation)
tex4ht - LaTeX and TeX for Hypertext (HTML) - executables
tex4ht-common - LaTeX and TeX for Hypertext (HTML) - support files
wand-doc - Python interface for ImageMagick library - documentation
worker - highly configurable two-paned file manager for X
wv - Programs for accessing Microsoft Word documents
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ sudo apt-get install libmagick++-dev
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
  autotools-dev gir1.2-rsvg-2.0 libbz2-dev libcairo-script-interpreter2 libcairo2-dev libcdt5 libcgraph6 libdjvulibre-dev libexif-dev libexpat1-dev libfontconfig1-dev libfreetype6-dev libgdk-pixbuf2.0-dev libglib2.0-dev libgraphviz-dev
  libgvc6 libgvpr2 libice-dev libilmbase-dev libjasper-dev libjbig-dev libjpeg-dev libjpeg-turbo8-dev libjpeg8-dev liblcms2-dev liblqr-1-0-dev libltdl-dev liblzma-dev libmagick++5 libmagickcore-dev libmagickcore5-extra
  libmagickwand-dev libopenexr-dev libpathplan4 libpcre3-dev libpcrecpp0 libpixman-1-dev libpng12-dev libpthread-stubs0-dev librsvg2-dev libsm-dev libtiff5-dev libtiffxx5 libtool libtool-bin libwmf-dev libx11-dev libx11-doc libxau-dev
  libxcb-render0-dev libxcb-shm0-dev libxcb1-dev libxdmcp-dev libxdot4 libxext-dev libxml2-dev libxrender-dev libxt-dev x11proto-core-dev x11proto-input-dev x11proto-kb-dev x11proto-render-dev x11proto-xext-dev xorg-sgml-doctools
  xtrans-dev
Suggested packages:
  libcairo2-doc libglib2.0-doc libice-doc libtool-doc liblzma-doc librsvg2-doc libsm-doc autoconf automaken gfortran fortran95-compiler gcj-jdk libwmf-doc libxcb-doc libxext-doc libxt-doc
The following NEW packages will be installed:
  autotools-dev gir1.2-rsvg-2.0 libbz2-dev libcairo-script-interpreter2 libcairo2-dev libcdt5 libcgraph6 libdjvulibre-dev libexif-dev libexpat1-dev libfontconfig1-dev libfreetype6-dev libgdk-pixbuf2.0-dev libglib2.0-dev libgraphviz-dev
  libgvc6 libgvpr2 libice-dev libilmbase-dev libjasper-dev libjbig-dev libjpeg-dev libjpeg-turbo8-dev libjpeg8-dev liblcms2-dev liblqr-1-0-dev libltdl-dev liblzma-dev libmagick++-dev libmagick++5 libmagickcore-dev libmagickcore5-extra
  libmagickwand-dev libopenexr-dev libpathplan4 libpcre3-dev libpcrecpp0 libpixman-1-dev libpng12-dev libpthread-stubs0-dev librsvg2-dev libsm-dev libtiff5-dev libtiffxx5 libtool libtool-bin libwmf-dev libx11-dev libx11-doc libxau-dev
  libxcb-render0-dev libxcb-shm0-dev libxcb1-dev libxdmcp-dev libxdot4 libxext-dev libxml2-dev libxrender-dev libxt-dev x11proto-core-dev x11proto-input-dev x11proto-kb-dev x11proto-render-dev x11proto-xext-dev xorg-sgml-doctools
  xtrans-dev
0 upgraded, 66 newly installed, 0 to remove and 7 not upgraded.
Need to get 21.4 MB of archives.
After this operation, 76.9 MB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://se.archive.ubuntu.com/ubuntu/ utopic/main libcairo-script-interpreter2 i386 1.13.0~20140204-0ubuntu1 [52.6 kB]
Get:2 http://se.archive.ubuntu.com/ubuntu/ utopic/main libmagick++5 i386 8:6.7.7.10+dfsg-4ubuntu1 [112 kB]
Get:3 http://se.archive.ubuntu.com/ubuntu/ utopic/main libmagickcore5-extra i386 8:6.7.7.10+dfsg-4ubuntu1 [60.2 kB]
Get:4 http://se.archive.ubuntu.com/ubuntu/ utopic/main libpcrecpp0 i386 1:8.35-3ubuntu1 [16.0 kB]
Get:5 http://se.archive.ubuntu.com/ubuntu/ utopic/main libtiffxx5 i386 4.0.3-10build1 [6,454 B]
Get:6 http://se.archive.ubuntu.com/ubuntu/ utopic/main autotools-dev all 20140911.1 [39.6 kB]
Get:7 http://se.archive.ubuntu.com/ubuntu/ utopic/main gir1.2-rsvg-2.0 i386 2.40.4-1 [3,680 B]
Get:8 http://se.archive.ubuntu.com/ubuntu/ utopic/main libbz2-dev i386 1.0.6-5ubuntu5 [28.8 kB]
Get:9 http://se.archive.ubuntu.com/ubuntu/ utopic/main libexpat1-dev i386 2.1.0-6ubuntu1 [115 kB]
Get:10 http://se.archive.ubuntu.com/ubuntu/ utopic/main libpng12-dev i386 1.2.51-0ubuntu3 [211 kB]
Get:11 http://se.archive.ubuntu.com/ubuntu/ utopic/main libfreetype6-dev i386 2.5.2-2ubuntu1 [636 kB]
Get:12 http://se.archive.ubuntu.com/ubuntu/ utopic/main libfontconfig1-dev i386 2.11.1-0ubuntu3 [635 kB]
Get:13 http://se.archive.ubuntu.com/ubuntu/ utopic/main xorg-sgml-doctools all 1:1.11-1 [12.9 kB]
Get:14 http://se.archive.ubuntu.com/ubuntu/ utopic/main x11proto-core-dev all 7.0.26-1 [700 kB]
Get:15 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxau-dev i386 1:1.0.8-1 [10.2 kB]
Get:16 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxdmcp-dev i386 1:1.1.1-1build1 [24.6 kB]
Get:17 http://se.archive.ubuntu.com/ubuntu/ utopic/main x11proto-input-dev all 2.3.1-1 [118 kB]
Get:18 http://se.archive.ubuntu.com/ubuntu/ utopic/main x11proto-kb-dev all 1.0.6-2 [269 kB]
Get:19 http://se.archive.ubuntu.com/ubuntu/ utopic/main xtrans-dev all 1.3.4-1 [70.3 kB]
Get:20 http://se.archive.ubuntu.com/ubuntu/ utopic/main libpthread-stubs0-dev i386 0.3-4 [4,054 B]
Get:21 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxcb1-dev i386 1.10-2ubuntu1 [76.6 kB]
Get:22 http://se.archive.ubuntu.com/ubuntu/ utopic/main libx11-dev i386 2:1.6.2-2ubuntu2 [657 kB]
Get:23 http://se.archive.ubuntu.com/ubuntu/ utopic/main x11proto-render-dev all 2:0.11.1-2 [20.1 kB]
Get:24 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxrender-dev i386 1:0.9.8-1 [26.6 kB]
Get:25 http://se.archive.ubuntu.com/ubuntu/ utopic/main libice-dev i386 2:1.0.9-1 [42.4 kB]
Get:26 http://se.archive.ubuntu.com/ubuntu/ utopic/main libsm-dev i386 2:1.2.2-1 [15.1 kB]
Get:27 http://se.archive.ubuntu.com/ubuntu/ utopic/main libpixman-1-dev i386 0.32.4-1ubuntu1 [235 kB]
Get:28 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxcb-render0-dev i386 1.10-2ubuntu1 [16.9 kB]
Get:29 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxcb-shm0-dev i386 1.10-2ubuntu1 [6,952 B]
Get:30 http://se.archive.ubuntu.com/ubuntu/ utopic/main x11proto-xext-dev all 7.3.0-1 [212 kB]
Get:31 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxext-dev i386 2:1.3.2-1 [89.9 kB]
Get:32 http://se.archive.ubuntu.com/ubuntu/ utopic/main libpcre3-dev i386 1:8.35-3ubuntu1 [327 kB]
Get:33 http://se.archive.ubuntu.com/ubuntu/ utopic/main libglib2.0-dev i386 2.42.0-2 [1,390 kB]
Get:34 http://se.archive.ubuntu.com/ubuntu/ utopic/main libcairo2-dev i386 1.13.0~20140204-0ubuntu1 [567 kB]
Get:35 http://se.archive.ubuntu.com/ubuntu/ utopic/main libcdt5 i386 2.38.0-5build1 [23.7 kB]
Get:36 http://se.archive.ubuntu.com/ubuntu/ utopic/main libcgraph6 i386 2.38.0-5build1 [46.8 kB]
Get:37 http://se.archive.ubuntu.com/ubuntu/ utopic/main libjpeg-turbo8-dev i386 1.3.0-0ubuntu2 [247 kB]
Get:38 http://se.archive.ubuntu.com/ubuntu/ utopic/main libjpeg8-dev i386 8c-2ubuntu8 [1,546 B]
Get:39 http://se.archive.ubuntu.com/ubuntu/ utopic/main libjpeg-dev i386 8c-2ubuntu8 [1,544 B]
Get:40 http://se.archive.ubuntu.com/ubuntu/ utopic/main libdjvulibre-dev i386 3.5.25.4-4 [2,342 kB]
Get:41 http://se.archive.ubuntu.com/ubuntu/ utopic/main libexif-dev i386 0.6.21-2 [328 kB]
Get:42 http://se.archive.ubuntu.com/ubuntu/ utopic/main libgdk-pixbuf2.0-dev i386 2.30.8-1 [43.3 kB]
Get:43 http://se.archive.ubuntu.com/ubuntu/ utopic/main libpathplan4 i386 2.38.0-5build1 [26.7 kB]
Get:44 http://se.archive.ubuntu.com/ubuntu/ utopic/main libgvc6 i386 2.38.0-5build1 [608 kB]
Get:45 http://se.archive.ubuntu.com/ubuntu/ utopic/main libgvpr2 i386 2.38.0-5build1 [179 kB]
Get:46 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxdot4 i386 2.38.0-5build1 [20.7 kB]
Get:47 http://se.archive.ubuntu.com/ubuntu/ utopic/main libltdl-dev i386 2.4.2-1.10ubuntu1 [159 kB]
Get:48 http://se.archive.ubuntu.com/ubuntu/ utopic/main libgraphviz-dev i386 2.38.0-5build1 [61.4 kB]
Get:49 http://se.archive.ubuntu.com/ubuntu/ utopic/main libilmbase-dev i386 1.0.1-6.1 [105 kB]
Get:50 http://se.archive.ubuntu.com/ubuntu/ utopic/main libjasper-dev i386 1.900.1-debian1-2 [517 kB]
Get:51 http://se.archive.ubuntu.com/ubuntu/ utopic/main liblcms2-dev i386 2.6-3ubuntu1 [4,657 kB]
Get:52 http://se.archive.ubuntu.com/ubuntu/ utopic/main liblqr-1-0-dev i386 0.4.2-1ubuntu1 [71.2 kB]
Get:53 http://se.archive.ubuntu.com/ubuntu/ utopic/main libopenexr-dev i386 1.6.1-7ubuntu1 [230 kB]
Get:54 http://se.archive.ubuntu.com/ubuntu/ utopic/main librsvg2-dev i386 2.40.4-1 [106 kB]
Get:55 http://se.archive.ubuntu.com/ubuntu/ utopic/main libjbig-dev i386 2.1-3ubuntu1 [24.1 kB]
Get:56 http://se.archive.ubuntu.com/ubuntu/ utopic/main liblzma-dev i386 5.1.1alpha+20120614-2ubuntu2 [139 kB]
Get:57 http://se.archive.ubuntu.com/ubuntu/ utopic/main libtiff5-dev i386 4.0.3-10build1 [280 kB]
Get:58 http://se.archive.ubuntu.com/ubuntu/ utopic/main libwmf-dev i386 0.2.8.4-10.3ubuntu1 [207 kB]
Get:59 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxml2-dev i386 2.9.1+dfsg1-4ubuntu1 [686 kB]
Get:60 http://se.archive.ubuntu.com/ubuntu/ utopic/main libxt-dev i386 1:1.1.4-1 [435 kB]
Get:61 http://se.archive.ubuntu.com/ubuntu/ utopic/main libmagickcore-dev i386 8:6.7.7.10+dfsg-4ubuntu1 [950 kB]
Get:62 http://se.archive.ubuntu.com/ubuntu/ utopic/main libmagickwand-dev i386 8:6.7.7.10+dfsg-4ubuntu1 [288 kB]
Get:63 http://se.archive.ubuntu.com/ubuntu/ utopic/main libmagick++-dev i386 8:6.7.7.10+dfsg-4ubuntu1 [134 kB]
Get:64 http://se.archive.ubuntu.com/ubuntu/ utopic/main libtool-bin i386 2.4.2-1.10ubuntu1 [72.1 kB]
Get:65 http://se.archive.ubuntu.com/ubuntu/ utopic/main libtool all 2.4.2-1.10ubuntu1 [181 kB]
Get:66 http://se.archive.ubuntu.com/ubuntu/ utopic/main libx11-doc all 2:1.6.2-2ubuntu2 [1,449 kB]
Fetched 21.4 MB in 18s (1,187 kB/s)
Extracting templates from packages: 100%
Selecting previously unselected package libcairo-script-interpreter2:i386.
(Reading database ... 192381 files and directories currently installed.)
Preparing to unpack .../libcairo-script-interpreter2_1.13.0~20140204-0ubuntu1_i386.deb ...
Unpacking libcairo-script-interpreter2:i386 (1.13.0~20140204-0ubuntu1) ...
Selecting previously unselected package libmagick++5:i386.
Preparing to unpack .../libmagick++5_8%3a6.7.7.10+dfsg-4ubuntu1_i386.deb ...
Unpacking libmagick++5:i386 (8:6.7.7.10+dfsg-4ubuntu1) ...
Selecting previously unselected package libmagickcore5-extra:i386.
Preparing to unpack .../libmagickcore5-extra_8%3a6.7.7.10+dfsg-4ubuntu1_i386.deb ...
Unpacking libmagickcore5-extra:i386 (8:6.7.7.10+dfsg-4ubuntu1) ...
Selecting previously unselected package libpcrecpp0:i386.
Preparing to unpack .../libpcrecpp0_1%3a8.35-3ubuntu1_i386.deb ...
Unpacking libpcrecpp0:i386 (1:8.35-3ubuntu1) ...
Selecting previously unselected package libtiffxx5:i386.
Preparing to unpack .../libtiffxx5_4.0.3-10build1_i386.deb ...
Unpacking libtiffxx5:i386 (4.0.3-10build1) ...
Selecting previously unselected package autotools-dev.
Preparing to unpack .../autotools-dev_20140911.1_all.deb ...
Unpacking autotools-dev (20140911.1) ...
Selecting previously unselected package gir1.2-rsvg-2.0.
Preparing to unpack .../gir1.2-rsvg-2.0_2.40.4-1_i386.deb ...
Unpacking gir1.2-rsvg-2.0 (2.40.4-1) ...
Selecting previously unselected package libbz2-dev:i386.
Preparing to unpack .../libbz2-dev_1.0.6-5ubuntu5_i386.deb ...
Unpacking libbz2-dev:i386 (1.0.6-5ubuntu5) ...
Selecting previously unselected package libexpat1-dev:i386.
Preparing to unpack .../libexpat1-dev_2.1.0-6ubuntu1_i386.deb ...
Unpacking libexpat1-dev:i386 (2.1.0-6ubuntu1) ...
Selecting previously unselected package libpng12-dev:i386.
Preparing to unpack .../libpng12-dev_1.2.51-0ubuntu3_i386.deb ...
Unpacking libpng12-dev:i386 (1.2.51-0ubuntu3) ...
Selecting previously unselected package libfreetype6-dev:i386.
Preparing to unpack .../libfreetype6-dev_2.5.2-2ubuntu1_i386.deb ...
Unpacking libfreetype6-dev:i386 (2.5.2-2ubuntu1) ...
Selecting previously unselected package libfontconfig1-dev:i386.
Preparing to unpack .../libfontconfig1-dev_2.11.1-0ubuntu3_i386.deb ...
Unpacking libfontconfig1-dev:i386 (2.11.1-0ubuntu3) ...
Selecting previously unselected package xorg-sgml-doctools.
Preparing to unpack .../xorg-sgml-doctools_1%3a1.11-1_all.deb ...
Unpacking xorg-sgml-doctools (1:1.11-1) ...
Selecting previously unselected package x11proto-core-dev.
Preparing to unpack .../x11proto-core-dev_7.0.26-1_all.deb ...
Unpacking x11proto-core-dev (7.0.26-1) ...
Selecting previously unselected package libxau-dev:i386.
Preparing to unpack .../libxau-dev_1%3a1.0.8-1_i386.deb ...
Unpacking libxau-dev:i386 (1:1.0.8-1) ...
Selecting previously unselected package libxdmcp-dev:i386.
Preparing to unpack .../libxdmcp-dev_1%3a1.1.1-1build1_i386.deb ...
Unpacking libxdmcp-dev:i386 (1:1.1.1-1build1) ...
Selecting previously unselected package x11proto-input-dev.
Preparing to unpack .../x11proto-input-dev_2.3.1-1_all.deb ...
Unpacking x11proto-input-dev (2.3.1-1) ...
Selecting previously unselected package x11proto-kb-dev.
Preparing to unpack .../x11proto-kb-dev_1.0.6-2_all.deb ...
Unpacking x11proto-kb-dev (1.0.6-2) ...
Selecting previously unselected package xtrans-dev.
Preparing to unpack .../xtrans-dev_1.3.4-1_all.deb ...
Unpacking xtrans-dev (1.3.4-1) ...
Selecting previously unselected package libpthread-stubs0-dev:i386.
Preparing to unpack .../libpthread-stubs0-dev_0.3-4_i386.deb ...
Unpacking libpthread-stubs0-dev:i386 (0.3-4) ...
Selecting previously unselected package libxcb1-dev:i386.
Preparing to unpack .../libxcb1-dev_1.10-2ubuntu1_i386.deb ...
Unpacking libxcb1-dev:i386 (1.10-2ubuntu1) ...
Selecting previously unselected package libx11-dev:i386.
Preparing to unpack .../libx11-dev_2%3a1.6.2-2ubuntu2_i386.deb ...
Unpacking libx11-dev:i386 (2:1.6.2-2ubuntu2) ...
Selecting previously unselected package x11proto-render-dev.
Preparing to unpack .../x11proto-render-dev_2%3a0.11.1-2_all.deb ...
Unpacking x11proto-render-dev (2:0.11.1-2) ...
Selecting previously unselected package libxrender-dev:i386.
Preparing to unpack .../libxrender-dev_1%3a0.9.8-1_i386.deb ...
Unpacking libxrender-dev:i386 (1:0.9.8-1) ...
Selecting previously unselected package libice-dev:i386.
Preparing to unpack .../libice-dev_2%3a1.0.9-1_i386.deb ...
Unpacking libice-dev:i386 (2:1.0.9-1) ...
Selecting previously unselected package libsm-dev:i386.
Preparing to unpack .../libsm-dev_2%3a1.2.2-1_i386.deb ...
Unpacking libsm-dev:i386 (2:1.2.2-1) ...
Selecting previously unselected package libpixman-1-dev.
Preparing to unpack .../libpixman-1-dev_0.32.4-1ubuntu1_i386.deb ...
Unpacking libpixman-1-dev (0.32.4-1ubuntu1) ...
Selecting previously unselected package libxcb-render0-dev:i386.
Preparing to unpack .../libxcb-render0-dev_1.10-2ubuntu1_i386.deb ...
Unpacking libxcb-render0-dev:i386 (1.10-2ubuntu1) ...
Selecting previously unselected package libxcb-shm0-dev:i386.
Preparing to unpack .../libxcb-shm0-dev_1.10-2ubuntu1_i386.deb ...
Unpacking libxcb-shm0-dev:i386 (1.10-2ubuntu1) ...
Selecting previously unselected package x11proto-xext-dev.
Preparing to unpack .../x11proto-xext-dev_7.3.0-1_all.deb ...
Unpacking x11proto-xext-dev (7.3.0-1) ...
Selecting previously unselected package libxext-dev:i386.
Preparing to unpack .../libxext-dev_2%3a1.3.2-1_i386.deb ...
Unpacking libxext-dev:i386 (2:1.3.2-1) ...
Selecting previously unselected package libpcre3-dev:i386.
Preparing to unpack .../libpcre3-dev_1%3a8.35-3ubuntu1_i386.deb ...
Unpacking libpcre3-dev:i386 (1:8.35-3ubuntu1) ...
Selecting previously unselected package libglib2.0-dev.
Preparing to unpack .../libglib2.0-dev_2.42.0-2_i386.deb ...
Unpacking libglib2.0-dev (2.42.0-2) ...
Selecting previously unselected package libcairo2-dev.
Preparing to unpack .../libcairo2-dev_1.13.0~20140204-0ubuntu1_i386.deb ...
Unpacking libcairo2-dev (1.13.0~20140204-0ubuntu1) ...
Selecting previously unselected package libcdt5.
Preparing to unpack .../libcdt5_2.38.0-5build1_i386.deb ...
Unpacking libcdt5 (2.38.0-5build1) ...
Selecting previously unselected package libcgraph6.
Preparing to unpack .../libcgraph6_2.38.0-5build1_i386.deb ...
Unpacking libcgraph6 (2.38.0-5build1) ...
Selecting previously unselected package libjpeg-turbo8-dev:i386.
Preparing to unpack .../libjpeg-turbo8-dev_1.3.0-0ubuntu2_i386.deb ...
Unpacking libjpeg-turbo8-dev:i386 (1.3.0-0ubuntu2) ...
Selecting previously unselected package libjpeg8-dev:i386.
Preparing to unpack .../libjpeg8-dev_8c-2ubuntu8_i386.deb ...
Unpacking libjpeg8-dev:i386 (8c-2ubuntu8) ...
Selecting previously unselected package libjpeg-dev:i386.
Preparing to unpack .../libjpeg-dev_8c-2ubuntu8_i386.deb ...
Unpacking libjpeg-dev:i386 (8c-2ubuntu8) ...
Selecting previously unselected package libdjvulibre-dev:i386.
Preparing to unpack .../libdjvulibre-dev_3.5.25.4-4_i386.deb ...
Unpacking libdjvulibre-dev:i386 (3.5.25.4-4) ...
Selecting previously unselected package libexif-dev.
Preparing to unpack .../libexif-dev_0.6.21-2_i386.deb ...
Unpacking libexif-dev (0.6.21-2) ...
Selecting previously unselected package libgdk-pixbuf2.0-dev.
Preparing to unpack .../libgdk-pixbuf2.0-dev_2.30.8-1_i386.deb ...
Unpacking libgdk-pixbuf2.0-dev (2.30.8-1) ...
Selecting previously unselected package libpathplan4.
Preparing to unpack .../libpathplan4_2.38.0-5build1_i386.deb ...
Unpacking libpathplan4 (2.38.0-5build1) ...
Selecting previously unselected package libgvc6.
Preparing to unpack .../libgvc6_2.38.0-5build1_i386.deb ...
Unpacking libgvc6 (2.38.0-5build1) ...
Selecting previously unselected package libgvpr2.
Preparing to unpack .../libgvpr2_2.38.0-5build1_i386.deb ...
Unpacking libgvpr2 (2.38.0-5build1) ...
Selecting previously unselected package libxdot4.
Preparing to unpack .../libxdot4_2.38.0-5build1_i386.deb ...
Unpacking libxdot4 (2.38.0-5build1) ...
Selecting previously unselected package libltdl-dev:i386.
Preparing to unpack .../libltdl-dev_2.4.2-1.10ubuntu1_i386.deb ...
Unpacking libltdl-dev:i386 (2.4.2-1.10ubuntu1) ...
Selecting previously unselected package libgraphviz-dev.
Preparing to unpack .../libgraphviz-dev_2.38.0-5build1_i386.deb ...
Unpacking libgraphviz-dev (2.38.0-5build1) ...
Selecting previously unselected package libilmbase-dev.
Preparing to unpack .../libilmbase-dev_1.0.1-6.1_i386.deb ...
Unpacking libilmbase-dev (1.0.1-6.1) ...
Selecting previously unselected package libjasper-dev.
Preparing to unpack .../libjasper-dev_1.900.1-debian1-2_i386.deb ...
Unpacking libjasper-dev (1.900.1-debian1-2) ...
Selecting previously unselected package liblcms2-dev:i386.
Preparing to unpack .../liblcms2-dev_2.6-3ubuntu1_i386.deb ...
Unpacking liblcms2-dev:i386 (2.6-3ubuntu1) ...
Selecting previously unselected package liblqr-1-0-dev.
Preparing to unpack .../liblqr-1-0-dev_0.4.2-1ubuntu1_i386.deb ...
Unpacking liblqr-1-0-dev (0.4.2-1ubuntu1) ...
Selecting previously unselected package libopenexr-dev.
Preparing to unpack .../libopenexr-dev_1.6.1-7ubuntu1_i386.deb ...
Unpacking libopenexr-dev (1.6.1-7ubuntu1) ...
Selecting previously unselected package librsvg2-dev.
Preparing to unpack .../librsvg2-dev_2.40.4-1_i386.deb ...
Unpacking librsvg2-dev (2.40.4-1) ...
Selecting previously unselected package libjbig-dev:i386.
Preparing to unpack .../libjbig-dev_2.1-3ubuntu1_i386.deb ...
Unpacking libjbig-dev:i386 (2.1-3ubuntu1) ...
Selecting previously unselected package liblzma-dev:i386.
Preparing to unpack .../liblzma-dev_5.1.1alpha+20120614-2ubuntu2_i386.deb ...
Unpacking liblzma-dev:i386 (5.1.1alpha+20120614-2ubuntu2) ...
Selecting previously unselected package libtiff5-dev:i386.
Preparing to unpack .../libtiff5-dev_4.0.3-10build1_i386.deb ...
Unpacking libtiff5-dev:i386 (4.0.3-10build1) ...
Selecting previously unselected package libwmf-dev.
Preparing to unpack .../libwmf-dev_0.2.8.4-10.3ubuntu1_i386.deb ...
Unpacking libwmf-dev (0.2.8.4-10.3ubuntu1) ...
Selecting previously unselected package libxml2-dev:i386.
Preparing to unpack .../libxml2-dev_2.9.1+dfsg1-4ubuntu1_i386.deb ...
Unpacking libxml2-dev:i386 (2.9.1+dfsg1-4ubuntu1) ...
Selecting previously unselected package libxt-dev:i386.
Preparing to unpack .../libxt-dev_1%3a1.1.4-1_i386.deb ...
Unpacking libxt-dev:i386 (1:1.1.4-1) ...
Selecting previously unselected package libmagickcore-dev.
Preparing to unpack .../libmagickcore-dev_8%3a6.7.7.10+dfsg-4ubuntu1_i386.deb ...
Unpacking libmagickcore-dev (8:6.7.7.10+dfsg-4ubuntu1) ...
Selecting previously unselected package libmagickwand-dev.
Preparing to unpack .../libmagickwand-dev_8%3a6.7.7.10+dfsg-4ubuntu1_i386.deb ...
Unpacking libmagickwand-dev (8:6.7.7.10+dfsg-4ubuntu1) ...
Selecting previously unselected package libmagick++-dev.
Preparing to unpack .../libmagick++-dev_8%3a6.7.7.10+dfsg-4ubuntu1_i386.deb ...
Unpacking libmagick++-dev (8:6.7.7.10+dfsg-4ubuntu1) ...
Selecting previously unselected package libtool-bin.
Preparing to unpack .../libtool-bin_2.4.2-1.10ubuntu1_i386.deb ...
Unpacking libtool-bin (2.4.2-1.10ubuntu1) ...
Selecting previously unselected package libtool.
Preparing to unpack .../libtool_2.4.2-1.10ubuntu1_all.deb ...
Unpacking libtool (2.4.2-1.10ubuntu1) ...
Selecting previously unselected package libx11-doc.
Preparing to unpack .../libx11-doc_2%3a1.6.2-2ubuntu2_all.deb ...
Unpacking libx11-doc (2:1.6.2-2ubuntu2) ...
Processing triggers for man-db (2.7.0.2-2) ...
Processing triggers for doc-base (0.10.6) ...
Processing 5 added doc-base files...
Processing triggers for libglib2.0-0:i386 (2.42.0-2) ...
Setting up libcairo-script-interpreter2:i386 (1.13.0~20140204-0ubuntu1) ...
Setting up libmagick++5:i386 (8:6.7.7.10+dfsg-4ubuntu1) ...
Setting up libmagickcore5-extra:i386 (8:6.7.7.10+dfsg-4ubuntu1) ...
Setting up libpcrecpp0:i386 (1:8.35-3ubuntu1) ...
Setting up libtiffxx5:i386 (4.0.3-10build1) ...
Setting up autotools-dev (20140911.1) ...
Setting up gir1.2-rsvg-2.0 (2.40.4-1) ...
Setting up libbz2-dev:i386 (1.0.6-5ubuntu5) ...
Setting up libexpat1-dev:i386 (2.1.0-6ubuntu1) ...
Setting up libpng12-dev:i386 (1.2.51-0ubuntu3) ...
Setting up libfreetype6-dev:i386 (2.5.2-2ubuntu1) ...
Setting up libfontconfig1-dev:i386 (2.11.1-0ubuntu3) ...
Setting up xorg-sgml-doctools (1:1.11-1) ...
Setting up x11proto-core-dev (7.0.26-1) ...
Setting up libxau-dev:i386 (1:1.0.8-1) ...
Setting up libxdmcp-dev:i386 (1:1.1.1-1build1) ...
Setting up x11proto-input-dev (2.3.1-1) ...
Setting up x11proto-kb-dev (1.0.6-2) ...
Setting up xtrans-dev (1.3.4-1) ...
Setting up libpthread-stubs0-dev:i386 (0.3-4) ...
Setting up libxcb1-dev:i386 (1.10-2ubuntu1) ...
Setting up libx11-dev:i386 (2:1.6.2-2ubuntu2) ...
Setting up x11proto-render-dev (2:0.11.1-2) ...
Setting up libxrender-dev:i386 (1:0.9.8-1) ...
Setting up libice-dev:i386 (2:1.0.9-1) ...
Setting up libsm-dev:i386 (2:1.2.2-1) ...
Setting up libpixman-1-dev (0.32.4-1ubuntu1) ...
Setting up libxcb-render0-dev:i386 (1.10-2ubuntu1) ...
Setting up libxcb-shm0-dev:i386 (1.10-2ubuntu1) ...
Setting up x11proto-xext-dev (7.3.0-1) ...
Setting up libxext-dev:i386 (2:1.3.2-1) ...
Setting up libpcre3-dev:i386 (1:8.35-3ubuntu1) ...
Setting up libglib2.0-dev (2.42.0-2) ...
Setting up libcairo2-dev (1.13.0~20140204-0ubuntu1) ...
Setting up libcdt5 (2.38.0-5build1) ...
Setting up libcgraph6 (2.38.0-5build1) ...
Setting up libjpeg-turbo8-dev:i386 (1.3.0-0ubuntu2) ...
Setting up libjpeg8-dev:i386 (8c-2ubuntu8) ...
Setting up libjpeg-dev:i386 (8c-2ubuntu8) ...
Setting up libdjvulibre-dev:i386 (3.5.25.4-4) ...
Setting up libexif-dev (0.6.21-2) ...
Setting up libgdk-pixbuf2.0-dev (2.30.8-1) ...
Setting up libpathplan4 (2.38.0-5build1) ...
Setting up libgvc6 (2.38.0-5build1) ...
Setting up libgvpr2 (2.38.0-5build1) ...
Setting up libxdot4 (2.38.0-5build1) ...
Setting up libltdl-dev:i386 (2.4.2-1.10ubuntu1) ...
Setting up libgraphviz-dev (2.38.0-5build1) ...
Setting up libilmbase-dev (1.0.1-6.1) ...
Setting up libjasper-dev (1.900.1-debian1-2) ...
Setting up liblcms2-dev:i386 (2.6-3ubuntu1) ...
Setting up liblqr-1-0-dev (0.4.2-1ubuntu1) ...
Setting up libopenexr-dev (1.6.1-7ubuntu1) ...
Setting up librsvg2-dev (2.40.4-1) ...
Setting up libjbig-dev:i386 (2.1-3ubuntu1) ...
Setting up liblzma-dev:i386 (5.1.1alpha+20120614-2ubuntu2) ...
Setting up libtiff5-dev:i386 (4.0.3-10build1) ...
Setting up libwmf-dev (0.2.8.4-10.3ubuntu1) ...
Setting up libxml2-dev:i386 (2.9.1+dfsg1-4ubuntu1) ...
Setting up libxt-dev:i386 (1:1.1.4-1) ...
Setting up libmagickcore-dev (8:6.7.7.10+dfsg-4ubuntu1) ...
Setting up libmagickwand-dev (8:6.7.7.10+dfsg-4ubuntu1) ...
Setting up libmagick++-dev (8:6.7.7.10+dfsg-4ubuntu1) ...
Setting up libtool-bin (2.4.2-1.10ubuntu1) ...
Setting up libtool (2.4.2-1.10ubuntu1) ...
Setting up libx11-doc (2:1.6.2-2ubuntu2) ...
Processing triggers for libc-bin (2.19-10ubuntu2) ...
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ bundle install --without development test
Fetching gem metadata from https://rubygems.org/.........
Resolving dependencies...
Using rake 10.4.0
Using i18n 0.6.11
Using multi_json 1.10.1
Using activesupport 3.2.19
Using builder 3.0.4
Using activemodel 3.2.19
Using erubis 2.7.0
Using journey 1.0.4
Using rack 1.4.5
Using rack-cache 1.2
Using rack-test 0.6.2
Using hike 1.2.3
Using tilt 1.4.1
Using sprockets 2.2.3
Using actionpack 3.2.19
Using mime-types 1.25.1
Using polyglot 0.3.5
Using treetop 1.4.15
Using mail 2.5.4
Using actionmailer 3.2.19
Using arel 3.0.3
Using tzinfo 0.3.42
Using activerecord 3.2.19
Using activeresource 3.2.19
Using bundler 1.7.7
Using coderay 1.1.0
Using rack-ssl 1.3.4
Using json 1.8.1
Using rdoc 3.12.2
Using thor 0.19.1
Using railties 3.2.19
Using jquery-rails 3.1.2
Using mysql2 0.3.17
Using net-ldap 0.3.1
Using ruby-openid 2.3.0
Using rack-openid 1.4.2
Using rails 3.2.19
Using rbpdf 1.18.2
Using redcarpet 2.3.0
Using request_store 1.0.5

Gem::Ext::BuildError: ERROR: Failed to build gem native extension.

    /usr/bin/ruby2.1 extconf.rb
checking for Ruby version >= 1.8.5... yes
checking for gcc... yes
checking for Magick-config... yes

Warning: Found a partial ImageMagick installation. Your operating system likely has some built-in ImageMagick libraries but not all of ImageMagick. This will most likely cause problems at both compile and runtime.
Found partial installation at: /usr
checking for ImageMagick version >= 6.4.9... *** extconf.rb failed ***
Could not create Makefile due to some reason, probably lack of necessary
libraries and/or headers.  Check the mkmf.log file for more details.  You may
need configuration options.

Provided configuration options:
    --with-opt-dir
    --without-opt-dir
    --with-opt-include
    --without-opt-include=${opt-dir}/include
    --with-opt-lib
    --without-opt-lib=${opt-dir}/lib
    --with-make-prog
    --without-make-prog
    --srcdir=.
    --curdir
    --ruby=/usr/bin/ruby2.1
extconf.rb:154:in ``': No such file or directory - convert (Errno::ENOENT)
    from extconf.rb:154:in `block in <main>'
    from /usr/lib/ruby/2.1.0/mkmf.rb:918:in `block in checking_for'
    from /usr/lib/ruby/2.1.0/mkmf.rb:351:in `block (2 levels) in postpone'
    from /usr/lib/ruby/2.1.0/mkmf.rb:321:in `open'
    from /usr/lib/ruby/2.1.0/mkmf.rb:351:in `block in postpone'
    from /usr/lib/ruby/2.1.0/mkmf.rb:321:in `open'
    from /usr/lib/ruby/2.1.0/mkmf.rb:347:in `postpone'
    from /usr/lib/ruby/2.1.0/mkmf.rb:917:in `checking_for'
    from extconf.rb:151:in `<main>'

extconf failed, exit code 1

Gem files will remain installed in /tmp/bundler20141126-17162-ra2nn9/rmagick-2.13.4/gems/rmagick-2.13.4 for inspection.
Results logged to /tmp/bundler20141126-17162-ra2nn9/rmagick-2.13.4/extensions/x86-linux/2.1.0/rmagick-2.13.4/gem_make.out
An error occurred while installing rmagick (2.13.4), and Bundler cannot continue.
Make sure that `gem install rmagick -v '2.13.4'` succeeds before bundling.
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ apt-cache search ImageMagick
groff - GNU troff text-formatting system
imagemagick - image manipulation programs
imagemagick-common - image manipulation programs -- infrastructure
imagemagick-dbg - debugging symbols for ImageMagick
imagemagick-doc - document files of ImageMagick
libmagick++-dev - object-oriented C++ interface to ImageMagick - development files
libmagick++5 - object-oriented C++ interface to ImageMagick
libmagickcore5 - low-level image manipulation library
libmagickwand5 - image manipulation library
perlmagick - Perl interface to the ImageMagick graphics routines
caja-image-converter - Caja extension to mass resize or rotate images
epix - Create mathematically accurate line figures, plots and movies
fbi - Linux frame buffer image viewer
gambas3-gb-image - Gambas image effects
gem-plugin-magick - Graphics Environment for Multimedia - ImageMagick support
gkrellshoot - Plugin for gkrellm to lock the screen and make screenshots
goby - WYSIWYG presentation tool for Emacs
graphicsmagick - collection of image processing tools
graphicsmagick-dbg - format-independent image processing - debugging symbols
graphicsmagick-imagemagick-compat - image processing tools providing ImageMagick interface
graphicsmagick-libmagick-dev-compat - image processing libraries providing ImageMagick interface
imageinfo - Displays selected image attributes
imgsizer - Adds WIDTH and HEIGHT attributes to IMG tags in HTML files
jmagick6-docs - java interface to ImageMagick - api documentation
libchart-gnuplot-perl - module for generating two- and three-dimensional plots
libgraphics-magick-perl - format-independent image processing - perl interface
libgraphicsmagick++1-dev - format-independent image processing - C++ development files
libgraphicsmagick++3 - format-independent image processing - C++ shared library
libgraphicsmagick1-dev - format-independent image processing - C development files
libgraphicsmagick3 - format-independent image processing - C shared library
libjmagick6-java - java interface to ImageMagick - java classes
libjmagick6-jni - java interface to ImageMagick - native library
libreoffice - office productivity suite (metapackage)
libvips-dev - image processing system good for very large images (dev)
libvips-doc - image processing system good for very large images (doc)
libvips-tools - image processing system good for very large images (tools)
libvips37 - image processing system good for very large images
nautilus-image-converter - nautilus extension to mass resize or rotate images
nip2 - spreadsheet-like graphical image manipulation tool
octave-image - image manipulation for Octave
php-horde-image - Horde Image API
php5-imagick - ImageMagick module for php5
pypy-wand - Python interface for ImageMagick library (PyPy build)
python-pythonmagick - Object-oriented Python interface to ImageMagick
python-sorl-thumbnail - thumbnail support for the Django framework
python-vipscc - image processing system good for very large images (tools)
python-wand - Python interface for ImageMagick library (Python 2 build)
python3-wand - Python interface for ImageMagick library (Python 3 build)
ruby-mini-magick - wrapper for ImageMagick with a small memory footprint
ruby-oily-png - native mixin to speed up ChunkyPNG
ruby-rmagick - ImageMagick API for Ruby
ruby-rmagick-doc - ImageMagick API for Ruby (documentation)
tex4ht - LaTeX and TeX for Hypertext (HTML) - executables
tex4ht-common - LaTeX and TeX for Hypertext (HTML) - support files
wand-doc - Python interface for ImageMagick library - documentation
worker - highly configurable two-paned file manager for X
wv - Programs for accessing Microsoft Word documents
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ sudo apt-get install imagemagick
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following extra packages will be installed:
  libnetpbm10 netpbm
Suggested packages:
  imagemagick-doc autotrace enscript ffmpeg gnuplot grads hp2xx html2ps libwmf-bin mplayer povray radiance texlive-base-bin transfig ufraw-batch
The following NEW packages will be installed:
  imagemagick libnetpbm10 netpbm
0 upgraded, 3 newly installed, 0 to remove and 7 not upgraded.
Need to get 1,181 kB of archives.
After this operation, 4,052 kB of additional disk space will be used.
Do you want to continue? [Y/n]
Get:1 http://se.archive.ubuntu.com/ubuntu/ utopic/main imagemagick i386 8:6.7.7.10+dfsg-4ubuntu1 [189 kB]
Get:2 http://se.archive.ubuntu.com/ubuntu/ utopic/main libnetpbm10 i386 2:10.0-15.1 [58.0 kB]
Get:3 http://se.archive.ubuntu.com/ubuntu/ utopic/main netpbm i386 2:10.0-15.1 [934 kB]
Fetched 1,181 kB in 1s (1,164 kB/s)
Selecting previously unselected package imagemagick.
(Reading database ... 196293 files and directories currently installed.)
Preparing to unpack .../imagemagick_8%3a6.7.7.10+dfsg-4ubuntu1_i386.deb ...
Unpacking imagemagick (8:6.7.7.10+dfsg-4ubuntu1) ...
Selecting previously unselected package libnetpbm10.
Preparing to unpack .../libnetpbm10_2%3a10.0-15.1_i386.deb ...
Unpacking libnetpbm10 (2:10.0-15.1) ...
Selecting previously unselected package netpbm.
Preparing to unpack .../netpbm_2%3a10.0-15.1_i386.deb ...
Unpacking netpbm (2:10.0-15.1) ...
Processing triggers for man-db (2.7.0.2-2) ...
Processing triggers for hicolor-icon-theme (0.13-1) ...
Processing triggers for gnome-menus (3.10.1-0ubuntu2) ...
Processing triggers for desktop-file-utils (0.22-1ubuntu2) ...
Processing triggers for mime-support (3.55ubuntu1) ...
Setting up imagemagick (8:6.7.7.10+dfsg-4ubuntu1) ...
update-alternatives: using /usr/bin/compare.im6 to provide /usr/bin/compare (compare) in auto mode
update-alternatives: using /usr/bin/animate.im6 to provide /usr/bin/animate (animate) in auto mode
update-alternatives: using /usr/bin/convert.im6 to provide /usr/bin/convert (convert) in auto mode
update-alternatives: using /usr/bin/composite.im6 to provide /usr/bin/composite (composite) in auto mode
update-alternatives: using /usr/bin/conjure.im6 to provide /usr/bin/conjure (conjure) in auto mode
update-alternatives: using /usr/bin/import.im6 to provide /usr/bin/import (import) in auto mode
update-alternatives: using /usr/bin/identify.im6 to provide /usr/bin/identify (identify) in auto mode
update-alternatives: using /usr/bin/stream.im6 to provide /usr/bin/stream (stream) in auto mode
update-alternatives: using /usr/bin/display.im6 to provide /usr/bin/display (display) in auto mode
update-alternatives: using /usr/bin/montage.im6 to provide /usr/bin/montage (montage) in auto mode
update-alternatives: using /usr/bin/mogrify.im6 to provide /usr/bin/mogrify (mogrify) in auto mode
Setting up libnetpbm10 (2:10.0-15.1) ...
Setting up netpbm (2:10.0-15.1) ...
Processing triggers for libc-bin (2.19-10ubuntu2) ...
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ bundle install --without development test
Fetching gem metadata from https://rubygems.org/.........
Resolving dependencies...
Using rake 10.4.0
Using i18n 0.6.11
Using multi_json 1.10.1
Using activesupport 3.2.19
Using builder 3.0.4
Using activemodel 3.2.19
Using erubis 2.7.0
Using journey 1.0.4
Using rack 1.4.5
Using rack-cache 1.2
Using rack-test 0.6.2
Using hike 1.2.3
Using tilt 1.4.1
Using sprockets 2.2.3
Using actionpack 3.2.19
Using mime-types 1.25.1
Using polyglot 0.3.5
Using treetop 1.4.15
Using mail 2.5.4
Using actionmailer 3.2.19
Using arel 3.0.3
Using tzinfo 0.3.42
Using activerecord 3.2.19
Using activeresource 3.2.19
Using bundler 1.7.7
Using coderay 1.1.0
Using rack-ssl 1.3.4
Using json 1.8.1
Using rdoc 3.12.2
Using thor 0.19.1
Using railties 3.2.19
Using jquery-rails 3.1.2
Using mysql2 0.3.17
Using net-ldap 0.3.1
Using ruby-openid 2.3.0
Using rack-openid 1.4.2
Using rails 3.2.19
Using rbpdf 1.18.2
Using redcarpet 2.3.0
Using request_store 1.0.5
Installing rmagick 2.13.4
Your bundle is complete!
Gems in the groups development and test were not installed.
Use `bundle show [gemname]` to see where a bundled gem is installed.
Post-install message from rmagick:
Please report any bugs. See https://github.com/gemhome/rmagick/compare/RMagick_2-13-2...master and https://github.com/rmagick/rmagick/issues/18
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ bundle install --without development test
Using rake 10.4.0
Using i18n 0.6.11
Using multi_json 1.10.1
Using activesupport 3.2.19
Using builder 3.0.4
Using activemodel 3.2.19
Using erubis 2.7.0
Using journey 1.0.4
Using rack 1.4.5
Using rack-cache 1.2
Using rack-test 0.6.2
Using hike 1.2.3
Using tilt 1.4.1
Using sprockets 2.2.3
Using actionpack 3.2.19
Using mime-types 1.25.1
Using polyglot 0.3.5
Using treetop 1.4.15
Using mail 2.5.4
Using actionmailer 3.2.19
Using arel 3.0.3
Using tzinfo 0.3.42
Using activerecord 3.2.19
Using activeresource 3.2.19
Using coderay 1.1.0
Using rack-ssl 1.3.4
Using json 1.8.1
Using rdoc 3.12.2
Using thor 0.19.1
Using railties 3.2.19
Using jquery-rails 3.1.2
Using mysql2 0.3.17
Using net-ldap 0.3.1
Using ruby-openid 2.3.0
Using rack-openid 1.4.2
Using bundler 1.7.7
Using rails 3.2.19
Using rbpdf 1.18.2
Using redcarpet 2.3.0
Using request_store 1.0.5
Using rmagick 2.13.4
Your bundle is complete!
Gems in the groups development and test were not installed.
Use `bundle show [gemname]` to see where a bundled gem is installed.
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ rake generate_secret_token
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ rake -T
rake about                                       # List versions of all Rails frameworks and the environment
rake assets:clean                                # Remove compiled assets
rake assets:precompile                           # Compile all the assets named in config.assets.precompile
rake ci                                          # Run the Continuous Integration tests for Redmine
rake ci:build                                    # Build Redmine
rake ci:setup                                    # Setup Redmine for a new build
rake ci:teardown                                 # Finish the build
rake config/database.yml                         # Creates database.yml for the CI server
rake config/initializers/secret_token.rb         # Generates a secret token for the application
rake db:create                                   # Create the database from DATABASE_URL or config/database.yml for the current Rails.env (use db:create:all to create all dbs in the config)
rake db:decrypt                                  # Decrypts SCM and LDAP passwords in the database
rake db:drop                                     # Drops the database using DATABASE_URL or the current Rails.env (use db:drop:all to drop all databases)
rake db:encrypt                                  # Encrypts SCM and LDAP passwords in the database
rake db:fixtures:load                            # Load fixtures into the current environment's database
rake db:migrate                                  # Migrate the database (options: VERSION=x, VERBOSE=false)
rake db:migrate:status                           # Display status of migrations
rake db:rollback                                 # Rolls the schema back to the previous version (specify steps w/ STEP=n)
rake db:schema:dump                              # Create a db/schema.rb file that can be portably used against any DB supported by AR
rake db:schema:load                              # Load a schema.rb file into the database
rake db:seed                                     # Load the seed data from db/seeds.rb
rake db:setup                                    # Create the database, load the schema, and initialize with the seed data (use db:reset to also drop the db first)
rake db:structure:dump                           # Dump the database structure to db/structure.sql
rake db:version                                  # Retrieves the current schema version number
rake doc:app                                     # Generate docs for the app -- also available doc:rails, doc:guides, doc:plugins (options: TEMPLATE=/rdoc-template.rb, TITLE="Custom Title")
rake extract_fixtures                            # Create YAML test fixtures from data in an existing database
rake generate_secret_token                       # Generates a secret token for the application
rake locales                                     # Updates and checks locales against en.yml
rake locales:add_key                             # Adds a new top-level translation string to all locale file (only works for childless keys, probably doesn't work on windows, doesn't check for duplicates)
rake locales:check_interpolation                 # Checks interpolation arguments in locals against en.yml
rake locales:check_parsing_by_psych              # Check parsing yaml by psych library on Ruby 1.9
rake locales:dup                                 # Duplicates a key
rake locales:remove_key                          # Removes a translation string from all locale file (only works for top-level childless non-multiline keys, probably doesn't work on windows)
rake locales:update                              # Updates language files based on en.yml content (only works for new top level keys)
rake log:clear                                   # Truncates all *.log files in log/ to zero bytes
rake middleware                                  # Prints out your Rack middleware stack
rake notes                                       # Enumerate all annotations (use notes:optimize, :fixme, :todo for focus)
rake notes:custom                                # Enumerate a custom annotation, specify with ANNOTATION=CUSTOM
rake rails:template                              # Applies the template supplied by LOCATION=(/path/to/template) or URL
rake rails:update                                # Update configs and some other initially generated files (or use just update:configs, update:scripts, or update:application_controller)
rake redmine:attachments:move_to_subdirectories  # Moves attachments stored at the root of the file directory (ie
rake redmine:attachments:prune                   # Removes uploaded files left unattached after one day
rake redmine:email:read                          # Read an email from standard input
rake redmine:email:receive_imap                  # Read emails from an IMAP server
rake redmine:email:receive_pop3                  # Read emails from an POP3 server
rake redmine:email:test[login]                   # Send a test email to the user with the provided login name
rake redmine:fetch_changesets                    # Fetch changesets from the repositories
rake redmine:load_default_data                   # Load Redmine default configuration data
rake redmine:migrate_dbms                        # FOR EXPERIMENTAL USE ONLY, Moves Redmine data from production database to the development database
rake redmine:migrate_from_mantis                 # Mantis migration script
rake redmine:migrate_from_trac                   # Trac migration script
rake redmine:permissions                         # List all permissions and the actions registered with them
rake redmine:plugins                             # Migrates and copies plugins assets
rake redmine:plugins:assets                      # Copies plugins assets into the public directory
rake redmine:plugins:migrate                     # Migrates installed plugins
rake redmine:plugins:test                        # Runs the plugins tests
rake redmine:plugins:test:functionals            # Run tests for {:functionals=>"db:test:prepare"}
rake redmine:plugins:test:integration            # Run tests for {:integration=>"db:test:prepare"}
rake redmine:plugins:test:units                  # Run tests for {:units=>"db:test:prepare"}
rake redmine:send_reminders                      # Send reminders about issues due in the next days
rake redmine:tokens:prune                        # Removes expired tokens
rake redmine:watchers:prune                      # Removes watchers from what they can no longer view
rake routes                                      # Print out all defined routes in match order, with names
rake secret                                      # Generate a cryptographically secure secret key (this is typically used to generate a secret for cookie sessions)
rake stats                                       # Report code statistics (KLOCs, etc) from the application
rake test                                        # Runs test:units, test:functionals, test:integration together (also available: test:benchmark, test:profile, test:plugins)
rake test:coverage                               # Measures test coverage
rake test:rdm_routing                            # Run tests for rdm_routing / Run the routing tests
rake test:recent                                 # Run tests for {:recent=>"test:prepare"} / Test recent changes
rake test:scm                                    # Run unit and functional scm tests
rake test:scm:functionals                        # Run tests for {:functionals=>"db:test:prepare"} / Run the scm functional tests
rake test:scm:setup:all                          # Creates all test repositories
rake test:scm:setup:bazaar                       # Creates a test bazaar repository
rake test:scm:setup:create_dir                   # Creates directory for test repositories
rake test:scm:setup:cvs                          # Creates a test cvs repository
rake test:scm:setup:darcs                        # Creates a test darcs repository
rake test:scm:setup:filesystem                   # Creates a test filesystem repository
rake test:scm:setup:git                          # Creates a test git repository
rake test:scm:setup:mercurial                    # Creates a test mercurial repository
rake test:scm:setup:subversion                   # Creates a test subversion repository
rake test:scm:units                              # Run tests for {:units=>"db:test:prepare"} / Run the scm unit tests
rake test:scm:update                             # Updates installed test repositories
rake test:single                                 # Run tests for {:single=>"test:prepare"}
rake test:ui                                     # Run tests for {:ui=>"db:test:prepare"} / Run the UI tests with Capybara (PhantomJS listening on port 4444 is required)
rake test:uncommitted                            # Run tests for {:uncommitted=>"test:prepare"} / Test changes since last checkin (only Subversion and Git)
rake time:zones:all                              # Displays all time zones, also available: time:zones:us, time:zones:local -- filter with OFFSET parameter, e.g., OFFSET=-6
rake tmp:clear                                   # Clear session, cache, and socket files from tmp/ (narrow w/ tmp:sessions:clear, tmp:cache:clear, tmp:sockets:clear)
rake tmp:create                                  # Creates tmp directories for sessions, cache, sockets, and pids
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ RAILS_ENV=production rake db:migrate
rake aborted!
Mysql2::Error: Access denied for user 'root'@'localhost' (using password: YES)
/var/lib/gems/2.1.0/gems/mysql2-0.3.17/lib/mysql2/client.rb:70:in `connect'
/var/lib/gems/2.1.0/gems/mysql2-0.3.17/lib/mysql2/client.rb:70:in `initialize'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/mysql2_adapter.rb:16:in `new'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/mysql2_adapter.rb:16:in `mysql2_connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:315:in `new_connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:325:in `checkout_new_connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:247:in `block (2 levels) in checkout'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:242:in `loop'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:242:in `block in checkout'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:239:in `checkout'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:102:in `block in connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:101:in `connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_pool.rb:410:in `retrieve_connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_specification.rb:171:in `retrieve_connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/connection_adapters/abstract/connection_specification.rb:145:in `connection'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/model_schema.rb:224:in `table_exists?'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/attribute_methods/primary_key.rb:75:in `get_primary_key'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/attribute_methods/primary_key.rb:60:in `reset_primary_key'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/attribute_methods/primary_key.rb:49:in `primary_key'
/var/lib/gems/2.1.0/gems/activerecord-3.2.19/lib/active_record/attribute_assignment.rb:13:in `attributes_protected_by_default'
/var/lib/gems/2.1.0/gems/activemodel-3.2.19/lib/active_model/mass_assignment_security.rb:216:in `block in protected_attributes_configs'
/var/lib/gems/2.1.0/gems/activemodel-3.2.19/lib/active_model/mass_assignment_security.rb:188:in `yield'
/var/lib/gems/2.1.0/gems/activemodel-3.2.19/lib/active_model/mass_assignment_security.rb:188:in `protected_attributes'
/var/lib/gems/2.1.0/gems/activemodel-3.2.19/lib/active_model/mass_assignment_security.rb:118:in `block in attr_protected'
/var/lib/gems/2.1.0/gems/activemodel-3.2.19/lib/active_model/mass_assignment_security.rb:117:in `each'
/var/lib/gems/2.1.0/gems/activemodel-3.2.19/lib/active_model/mass_assignment_security.rb:117:in `attr_protected'
/home/daniel/Documents/klarna/redmine-2.6.0/app/models/issue_relation.rb:73:in `<class:IssueRelation>'
/home/daniel/Documents/klarna/redmine-2.6.0/app/models/issue_relation.rb:18:in `<top (required)>'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `block in require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:236:in `load_dependency'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:359:in `require_or_load'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:502:in `load_missing_constant'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:192:in `block in const_missing'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `each'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `const_missing'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:514:in `load_missing_constant'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:192:in `block in const_missing'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `each'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `const_missing'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:514:in `load_missing_constant'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:192:in `block in const_missing'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `each'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `const_missing'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:514:in `load_missing_constant'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:192:in `block in const_missing'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `each'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:190:in `const_missing'
/home/daniel/Documents/klarna/redmine-2.6.0/lib/redmine/helpers/gantt.rb:28:in `<class:Gantt>'
/home/daniel/Documents/klarna/redmine-2.6.0/lib/redmine/helpers/gantt.rb:21:in `<module:Helpers>'
/home/daniel/Documents/klarna/redmine-2.6.0/lib/redmine/helpers/gantt.rb:19:in `<module:Redmine>'
/home/daniel/Documents/klarna/redmine-2.6.0/lib/redmine/helpers/gantt.rb:18:in `<top (required)>'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `block in require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:236:in `load_dependency'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/home/daniel/Documents/klarna/redmine-2.6.0/lib/redmine.rb:56:in `<top (required)>'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `block in require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:236:in `load_dependency'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/home/daniel/Documents/klarna/redmine-2.6.0/config/initializers/30-redmine.rb:4:in `<top (required)>'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:245:in `load'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:245:in `block in load'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:236:in `load_dependency'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:245:in `load'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/engine.rb:593:in `block (2 levels) in <class:Engine>'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/engine.rb:592:in `each'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/engine.rb:592:in `block in <class:Engine>'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/initializable.rb:30:in `instance_exec'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/initializable.rb:30:in `run'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/initializable.rb:55:in `block in run_initializers'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/initializable.rb:54:in `each'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/initializable.rb:54:in `run_initializers'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/application.rb:136:in `initialize!'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/railtie/configurable.rb:30:in `method_missing'
/home/daniel/Documents/klarna/redmine-2.6.0/config/environment.rb:14:in `<top (required)>'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `block in require'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:236:in `load_dependency'
/var/lib/gems/2.1.0/gems/activesupport-3.2.19/lib/active_support/dependencies.rb:251:in `require'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/application.rb:103:in `require_environment!'
/var/lib/gems/2.1.0/gems/railties-3.2.19/lib/rails/application.rb:305:in `block (2 levels) in initialize_tasks'
Tasks: TOP => db:migrate => environment
(See full trace by running task with --trace)
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ bundle install --without development test
Using rake 10.4.0
Using i18n 0.6.11
Using multi_json 1.10.1
Using activesupport 3.2.19
Using builder 3.0.4
Using activemodel 3.2.19
Using erubis 2.7.0
Using journey 1.0.4
Using rack 1.4.5
Using rack-cache 1.2
Using rack-test 0.6.2
Using hike 1.2.3
Using tilt 1.4.1
Using sprockets 2.2.3
Using actionpack 3.2.19
Using mime-types 1.25.1
Using polyglot 0.3.5
Using treetop 1.4.15
Using mail 2.5.4
Using actionmailer 3.2.19
Using arel 3.0.3
Using tzinfo 0.3.42
Using activerecord 3.2.19
Using activeresource 3.2.19
Using coderay 1.1.0
Using rack-ssl 1.3.4
Using json 1.8.1
Using rdoc 3.12.2
Using thor 0.19.1
Using railties 3.2.19
Using jquery-rails 3.1.2
Using mysql2 0.3.17
Using net-ldap 0.3.1
Using ruby-openid 2.3.0
Using rack-openid 1.4.2
Using bundler 1.7.7
Using rails 3.2.19
Using rbpdf 1.18.2
Using redcarpet 2.3.0
Using request_store 1.0.5
Using rmagick 2.13.4
Your bundle is complete!
Gems in the groups development and test were not installed.
Use `bundle show [gemname]` to see where a bundled gem is installed.
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ RAILS_ENV=production rake db:migrate
==  Setup: migrating ==========================================================
-- create_table("attachments", {:force=>true})
   -> 0.0943s
-- create_table("auth_sources", {:force=>true})
   -> 0.0780s
-- create_table("custom_fields", {:force=>true})
   -> 0.0781s
-- create_table("custom_fields_projects", {:id=>false, :force=>true})
   -> 0.0670s
-- create_table("custom_fields_trackers", {:id=>false, :force=>true})
   -> 0.2010s
-- create_table("custom_values", {:force=>true})
   -> 0.0668s
-- create_table("documents", {:force=>true})
   -> 0.0670s
-- add_index("documents", ["project_id"], {:name=>"documents_project_id"})
   -> 0.1563s
-- create_table("enumerations", {:force=>true})
   -> 0.0780s
-- create_table("issue_categories", {:force=>true})
   -> 0.0780s
-- add_index("issue_categories", ["project_id"], {:name=>"issue_categories_project_id"})
   -> 0.1674s
-- create_table("issue_histories", {:force=>true})
   -> 0.0778s
-- add_index("issue_histories", ["issue_id"], {:name=>"issue_histories_issue_id"})
   -> 0.1580s
-- create_table("issue_statuses", {:force=>true})
   -> 0.0778s
-- create_table("issues", {:force=>true})
   -> 0.0782s
-- add_index("issues", ["project_id"], {:name=>"issues_project_id"})
   -> 0.1673s
-- create_table("members", {:force=>true})
   -> 0.0889s
-- create_table("news", {:force=>true})
   -> 0.1004s
-- add_index("news", ["project_id"], {:name=>"news_project_id"})
   -> 0.1675s
-- create_table("permissions", {:force=>true})
   -> 0.0667s
-- create_table("permissions_roles", {:id=>false, :force=>true})
   -> 0.0670s
-- add_index("permissions_roles", ["role_id"], {:name=>"permissions_roles_role_id"})
   -> 0.1451s
-- create_table("projects", {:force=>true})
   -> 0.0779s
-- create_table("roles", {:force=>true})
   -> 0.0670s
-- create_table("tokens", {:force=>true})
   -> 0.0671s
-- create_table("trackers", {:force=>true})
   -> 0.0781s
-- create_table("users", {:force=>true})
   -> 0.0670s
-- create_table("versions", {:force=>true})
   -> 0.0669s
-- add_index("versions", ["project_id"], {:name=>"versions_project_id"})
   -> 0.1674s
-- create_table("workflows", {:force=>true})
   -> 0.0780s
==  Setup: migrated (4.8771s) =================================================

==  IssueMove: migrating ======================================================
==  IssueMove: migrated (0.0648s) =============================================

==  IssueAddNote: migrating ===================================================
==  IssueAddNote: migrated (0.0544s) ==========================================

==  ExportPdf: migrating ======================================================
==  ExportPdf: migrated (0.1037s) =============================================

==  IssueStartDate: migrating =================================================
-- add_column(:issues, :start_date, :date)
   -> 0.1779s
-- add_column(:issues, :done_ratio, :integer, {:default=>0, :null=>false})
   -> 0.1902s
==  IssueStartDate: migrated (0.3686s) ========================================

==  CalendarAndActivity: migrating ============================================
==  CalendarAndActivity: migrated (0.1315s) ===================================

==  CreateJournals: migrating =================================================
-- create_table(:journals, {:force=>true})
   -> 0.0738s
-- create_table(:journal_details, {:force=>true})
   -> 0.0664s
-- add_index("journals", ["journalized_id", "journalized_type"], {:name=>"journals_journalized_id"})
   -> 0.1692s
-- add_index("journal_details", ["journal_id"], {:name=>"journal_details_journal_id"})
   -> 0.1891s
-- drop_table(:issue_histories)
   -> 0.0466s
==  CreateJournals: migrated (0.6229s) ========================================

==  CreateUserPreferences: migrating ==========================================
-- create_table(:user_preferences)
   -> 0.0654s
==  CreateUserPreferences: migrated (0.0657s) =================================

==  AddHideMailPref: migrating ================================================
-- add_column(:user_preferences, :hide_mail, :boolean, {:default=>false})
   -> 0.1660s
==  AddHideMailPref: migrated (0.1663s) =======================================

==  CreateComments: migrating =================================================
-- create_table(:comments)
   -> 0.0653s
==  CreateComments: migrated (0.0655s) ========================================

==  AddNewsCommentsCount: migrating ===========================================
-- add_column(:news, :comments_count, :integer, {:default=>0, :null=>false})
   -> 0.1733s
==  AddNewsCommentsCount: migrated (0.1738s) ==================================

==  AddCommentsPermissions: migrating =========================================
==  AddCommentsPermissions: migrated (0.0870s) ================================

==  CreateQueries: migrating ==================================================
-- create_table(:queries, {:force=>true})
   -> 0.0800s
==  CreateQueries: migrated (0.0803s) =========================================

==  AddQueriesPermissions: migrating ==========================================
==  AddQueriesPermissions: migrated (0.0658s) =================================

==  CreateRepositories: migrating =============================================
-- create_table(:repositories, {:force=>true})
   -> 0.0679s
==  CreateRepositories: migrated (0.0682s) ====================================

==  AddRepositoriesPermissions: migrating =====================================
==  AddRepositoriesPermissions: migrated (0.3205s) ============================

==  CreateSettings: migrating =================================================
-- create_table(:settings, {:force=>true})
   -> 0.0650s
==  CreateSettings: migrated (0.0655s) ========================================

==  SetDocAndFilesNotifications: migrating ====================================
==  SetDocAndFilesNotifications: migrated (0.2107s) ===========================

==  AddIssueStatusPosition: migrating =========================================
-- add_column(:issue_statuses, :position, :integer, {:default=>1})
   -> 0.2785s
==  AddIssueStatusPosition: migrated (0.3348s) ================================

==  AddRolePosition: migrating ================================================
-- add_column(:roles, :position, :integer, {:default=>1})
   -> 0.2614s
==  AddRolePosition: migrated (0.3239s) =======================================

==  AddTrackerPosition: migrating =============================================
-- add_column(:trackers, :position, :integer, {:default=>1})
   -> 0.1821s
==  AddTrackerPosition: migrated (0.2466s) ====================================

==  SerializePossiblesValues: migrating =======================================
==  SerializePossiblesValues: migrated (0.0075s) ==============================

==  AddTrackerIsInRoadmap: migrating ==========================================
-- add_column(:trackers, :is_in_roadmap, :boolean, {:default=>true, :null=>false})
   -> 0.1862s
==  AddTrackerIsInRoadmap: migrated (0.1865s) =================================

==  AddRoadmapPermission: migrating ===========================================
==  AddRoadmapPermission: migrated (0.0909s) ==================================

==  AddSearchPermission: migrating ============================================
==  AddSearchPermission: migrated (0.2217s) ===================================

==  AddRepositoryLoginAndPassword: migrating ==================================
-- add_column(:repositories, :login, :string, {:limit=>60, :default=>""})
   -> 0.2907s
-- add_column(:repositories, :password, :string, {:limit=>60, :default=>""})
   -> 0.2550s
==  AddRepositoryLoginAndPassword: migrated (0.5482s) =========================

==  CreateWikis: migrating ====================================================
-- create_table(:wikis)
   -> 0.0766s
-- add_index(:wikis, :project_id, {:name=>:wikis_project_id})
   -> 0.1562s
==  CreateWikis: migrated (0.2333s) ===========================================

==  CreateWikiPages: migrating ================================================
-- create_table(:wiki_pages)
   -> 0.0767s
-- add_index(:wiki_pages, [:wiki_id, :title], {:name=>:wiki_pages_wiki_id_title})
   -> 0.1673s
==  CreateWikiPages: migrated (0.2445s) =======================================

==  CreateWikiContents: migrating =============================================
-- create_table(:wiki_contents)
   -> 0.0944s
-- add_index(:wiki_contents, :page_id, {:name=>:wiki_contents_page_id})
   -> 0.1673s
-- create_table(:wiki_content_versions)
   -> 0.0668s
-- add_index(:wiki_content_versions, :wiki_content_id, {:name=>:wiki_content_versions_wcid})
   -> 0.1451s
==  CreateWikiContents: migrated (0.4746s) ====================================

==  AddProjectsFeedsPermissions: migrating ====================================
==  AddProjectsFeedsPermissions: migrated (0.0544s) ===========================

==  AddRepositoryRootUrl: migrating ===========================================
-- add_column(:repositories, :root_url, :string, {:limit=>255, :default=>""})
   -> 0.1777s
==  AddRepositoryRootUrl: migrated (0.1780s) ==================================

==  CreateTimeEntries: migrating ==============================================
-- create_table(:time_entries)
   -> 0.0759s
-- add_index(:time_entries, [:project_id], {:name=>:time_entries_project_id})
   -> 0.1562s
-- add_index(:time_entries, [:issue_id], {:name=>:time_entries_issue_id})
   -> 0.1672s
==  CreateTimeEntries: migrated (0.4002s) =====================================

==  AddTimelogPermissions: migrating ==========================================
==  AddTimelogPermissions: migrated (0.0711s) =================================

==  CreateChangesets: migrating ===============================================
-- create_table(:changesets)
   -> 0.0773s
-- add_index(:changesets, [:repository_id, :revision], {:unique=>true, :name=>:changesets_repos_rev})
   -> 0.2230s
==  CreateChangesets: migrated (0.3008s) ======================================

==  CreateChanges: migrating ==================================================
-- create_table(:changes)
   -> 0.0785s
-- add_index(:changes, [:changeset_id], {:name=>:changesets_changeset_id})
   -> 0.1451s
==  CreateChanges: migrated (0.2241s) =========================================

==  AddChangesetCommitDate: migrating =========================================
-- add_column(:changesets, :commit_date, :date)
   -> 0.3774s
==  AddChangesetCommitDate: migrated (0.4744s) ================================

==  AddProjectIdentifier: migrating ===========================================
-- add_column(:projects, :identifier, :string, {:limit=>20})
   -> 0.1866s
==  AddProjectIdentifier: migrated (0.1869s) ==================================

==  AddCustomFieldIsFilter: migrating =========================================
-- add_column(:custom_fields, :is_filter, :boolean, {:null=>false, :default=>false})
   -> 0.1812s
==  AddCustomFieldIsFilter: migrated (0.1817s) ================================

==  CreateWatchers: migrating =================================================
-- create_table(:watchers)
   -> 0.0923s
==  CreateWatchers: migrated (0.0926s) ========================================

==  CreateChangesetsIssues: migrating =========================================
-- create_table(:changesets_issues, {:id=>false})
   -> 0.0878s
-- add_index(:changesets_issues, [:changeset_id, :issue_id], {:unique=>true, :name=>:changesets_issues_ids})
   -> 0.2898s
==  CreateChangesetsIssues: migrated (0.3782s) ================================

==  RenameCommentToComments: migrating ========================================
==  RenameCommentToComments: migrated (0.6301s) ===============================

==  CreateIssueRelations: migrating ===========================================
-- create_table(:issue_relations)
   -> 0.0779s
==  CreateIssueRelations: migrated (0.0781s) ==================================

==  AddRelationsPermissions: migrating ========================================
==  AddRelationsPermissions: migrated (0.1046s) ===============================

==  SetLanguageLengthToFive: migrating ========================================
-- change_column(:users, :language, :string, {:limit=>5, :default=>""})
   -> 0.2212s
==  SetLanguageLengthToFive: migrated (0.2217s) ===============================

==  CreateBoards: migrating ===================================================
-- create_table(:boards)
   -> 0.0652s
-- add_index(:boards, [:project_id], {:name=>:boards_project_id})
   -> 0.2563s
==  CreateBoards: migrated (0.3221s) ==========================================

==  CreateMessages: migrating =================================================
-- create_table(:messages)
   -> 0.1001s
-- add_index(:messages, [:board_id], {:name=>:messages_board_id})
   -> 0.2133s
-- add_index(:messages, [:parent_id], {:name=>:messages_parent_id})
   -> 0.1561s
==  CreateMessages: migrated (0.4702s) ========================================

==  AddBoardsPermissions: migrating ===========================================
==  AddBoardsPermissions: migrated (0.1539s) ==================================

==  AllowNullVersionEffectiveDate: migrating ==================================
-- change_column(:versions, :effective_date, :date, {:default=>nil, :null=>true})
   -> 0.0436s
==  AllowNullVersionEffectiveDate: migrated (0.0439s) =========================

==  AddWikiDestroyPagePermission: migrating ===================================
==  AddWikiDestroyPagePermission: migrated (0.1482s) ==========================

==  AddWikiAttachmentsPermissions: migrating ==================================
==  AddWikiAttachmentsPermissions: migrated (0.1210s) =========================

==  AddProjectStatus: migrating ===============================================
-- add_column(:projects, :status, :integer, {:default=>1, :null=>false})
   -> 0.2444s
==  AddProjectStatus: migrated (0.2448s) ======================================

==  AddChangesRevision: migrating =============================================
-- add_column(:changes, :revision, :string)
   -> 0.2407s
==  AddChangesRevision: migrated (0.2409s) ====================================

==  AddChangesBranch: migrating ===============================================
-- add_column(:changes, :branch, :string)
   -> 0.2148s
==  AddChangesBranch: migrated (0.2151s) ======================================

==  AddChangesetsScmid: migrating =============================================
-- add_column(:changesets, :scmid, :string)
   -> 0.3670s
==  AddChangesetsScmid: migrated (0.3672s) ====================================

==  AddRepositoriesType: migrating ============================================
-- add_column(:repositories, :type, :string)
   -> 0.1805s
==  AddRepositoriesType: migrated (0.1836s) ===================================

==  AddRepositoriesChangesPermission: migrating ===============================
==  AddRepositoriesChangesPermission: migrated (0.0717s) ======================

==  AddVersionsWikiPageTitle: migrating =======================================
-- add_column(:versions, :wiki_page_title, :string)
   -> 0.2112s
==  AddVersionsWikiPageTitle: migrated (0.2114s) ==============================

==  AddIssueCategoriesAssignedToId: migrating =================================
-- add_column(:issue_categories, :assigned_to_id, :integer)
   -> 0.2559s
==  AddIssueCategoriesAssignedToId: migrated (0.2562s) ========================

==  AddRolesAssignable: migrating =============================================
-- add_column(:roles, :assignable, :boolean, {:default=>true})
   -> 0.1808s
==  AddRolesAssignable: migrated (0.1812s) ====================================

==  ChangeChangesetsCommitterLimit: migrating =================================
-- change_column(:changesets, :committer, :string, {:limit=>nil})
   -> 0.2207s
==  ChangeChangesetsCommitterLimit: migrated (0.2212s) ========================

==  AddRolesBuiltin: migrating ================================================
-- add_column(:roles, :builtin, :integer, {:default=>0, :null=>false})
   -> 0.1886s
==  AddRolesBuiltin: migrated (0.1889s) =======================================

==  InsertBuiltinRoles: migrating =============================================
==  InsertBuiltinRoles: migrated (0.4975s) ====================================

==  AddRolesPermissions: migrating ============================================
-- add_column(:roles, :permissions, :text)
   -> 0.2987s
==  AddRolesPermissions: migrated (0.2993s) ===================================

==  DropPermissions: migrating ================================================
-- drop_table(:permissions)
   -> 0.0319s
-- drop_table(:permissions_roles)
   -> 0.0337s
==  DropPermissions: migrated (0.0663s) =======================================

==  AddSettingsUpdatedOn: migrating ===========================================
-- add_column(:settings, :updated_on, :timestamp)
   -> 0.2330s
==  AddSettingsUpdatedOn: migrated (0.3069s) ==================================

==  AddCustomValueCustomizedIndex: migrating ==================================
-- add_index(:custom_values, [:customized_type, :customized_id], {:name=>:custom_values_customized})
   -> 0.2093s
==  AddCustomValueCustomizedIndex: migrated (0.2096s) =========================

==  CreateWikiRedirects: migrating ============================================
-- create_table(:wiki_redirects)
   -> 0.0942s
-- add_index(:wiki_redirects, [:wiki_id, :title], {:name=>:wiki_redirects_wiki_id_title})
   -> 0.1563s
==  CreateWikiRedirects: migrated (0.2509s) ===================================

==  CreateEnabledModules: migrating ===========================================
-- create_table(:enabled_modules)
   -> 0.0803s
-- add_index(:enabled_modules, [:project_id], {:name=>:enabled_modules_project_id})
   -> 0.1675s
==  CreateEnabledModules: migrated (0.2530s) ==================================

==  AddIssuesEstimatedHours: migrating ========================================
-- add_column(:issues, :estimated_hours, :float)
   -> 0.2276s
==  AddIssuesEstimatedHours: migrated (0.2278s) ===============================

==  ChangeAttachmentsContentTypeLimit: migrating ==============================
-- change_column(:attachments, :content_type, :string, {:limit=>nil})
   -> 0.1999s
==  ChangeAttachmentsContentTypeLimit: migrated (0.2002s) =====================

==  AddQueriesColumnNames: migrating ==========================================
-- add_column(:queries, :column_names, :text)
   -> 0.1773s
==  AddQueriesColumnNames: migrated (0.1779s) =================================

==  AddEnumerationsPosition: migrating ========================================
-- add_column(:enumerations, :position, :integer, {:default=>1})
   -> 0.1795s
==  AddEnumerationsPosition: migrated (0.2687s) ===============================

==  AddEnumerationsIsDefault: migrating =======================================
-- add_column(:enumerations, :is_default, :boolean, {:default=>false, :null=>false})
   -> 0.2344s
==  AddEnumerationsIsDefault: migrated (0.2348s) ==============================

==  AddAuthSourcesTls: migrating ==============================================
-- add_column(:auth_sources, :tls, :boolean, {:default=>false, :null=>false})
   -> 0.2502s
==  AddAuthSourcesTls: migrated (0.2505s) =====================================

==  AddMembersMailNotification: migrating =====================================
-- add_column(:members, :mail_notification, :boolean, {:default=>false, :null=>false})
   -> 0.2585s
==  AddMembersMailNotification: migrated (0.2587s) ============================

==  AllowNullPosition: migrating ==============================================
-- change_column(:issue_statuses, :position, :integer, {:default=>1, :null=>true})
   -> 0.0506s
-- change_column(:roles, :position, :integer, {:default=>1, :null=>true})
   -> 0.0446s
-- change_column(:trackers, :position, :integer, {:default=>1, :null=>true})
   -> 0.0447s
-- change_column(:boards, :position, :integer, {:default=>1, :null=>true})
   -> 0.0890s
-- change_column(:enumerations, :position, :integer, {:default=>1, :null=>true})
   -> 0.0337s
==  AllowNullPosition: migrated (0.2640s) =====================================

==  RemoveIssueStatusesHtmlColor: migrating ===================================
-- remove_column(:issue_statuses, :html_color)
   -> 0.2447s
==  RemoveIssueStatusesHtmlColor: migrated (0.2451s) ==========================

==  AddCustomFieldsPosition: migrating ========================================
-- add_column(:custom_fields, :position, :integer, {:default=>1})
   -> 0.2217s
==  AddCustomFieldsPosition: migrated (0.2238s) ===============================

==  AddUserPreferencesTimeZone: migrating =====================================
-- add_column(:user_preferences, :time_zone, :string)
   -> 0.1785s
==  AddUserPreferencesTimeZone: migrated (0.1788s) ============================

==  AddUsersType: migrating ===================================================
-- add_column(:users, :type, :string)
   -> 0.2278s
==  AddUsersType: migrated (0.2725s) ==========================================

==  CreateProjectsTrackers: migrating =========================================
-- create_table(:projects_trackers, {:id=>false})
   -> 0.0877s
-- add_index(:projects_trackers, :project_id, {:name=>:projects_trackers_project_id})
   -> 0.2231s
==  CreateProjectsTrackers: migrated (0.3139s) ================================

==  AddMessagesLocked: migrating ==============================================
-- add_column(:messages, :locked, :boolean, {:default=>false})
   -> 0.1777s
==  AddMessagesLocked: migrated (0.1780s) =====================================

==  AddMessagesSticky: migrating ==============================================
-- add_column(:messages, :sticky, :integer, {:default=>0})
   -> 0.1805s
==  AddMessagesSticky: migrated (0.1807s) =====================================

==  ChangeAuthSourcesAccountLimit: migrating ==================================
-- change_column(:auth_sources, :account, :string, {:limit=>nil})
   -> 0.2775s
==  ChangeAuthSourcesAccountLimit: migrated (0.2780s) =========================

==  AddRoleTrackerOldStatusIndexToWorkflows: migrating ========================
-- add_index(:workflows, [:role_id, :tracker_id, :old_status_id], {:name=>:wkfs_role_tracker_old_status})
   -> 0.2239s
==  AddRoleTrackerOldStatusIndexToWorkflows: migrated (0.2245s) ===============

==  AddCustomFieldsSearchable: migrating ======================================
-- add_column(:custom_fields, :searchable, :boolean, {:default=>false})
   -> 0.1865s
==  AddCustomFieldsSearchable: migrated (0.1868s) =============================

==  ChangeProjectsDescriptionToText: migrating ================================
-- change_column(:projects, :description, :text, {:null=>true, :default=>nil})
   -> 0.2223s
==  ChangeProjectsDescriptionToText: migrated (0.2226s) =======================

==  AddCustomFieldsDefaultValue: migrating ====================================
-- add_column(:custom_fields, :default_value, :text)
   -> 0.1890s
==  AddCustomFieldsDefaultValue: migrated (0.1893s) ===========================

==  AddAttachmentsDescription: migrating ======================================
-- add_column(:attachments, :description, :string)
   -> 0.2007s
==  AddAttachmentsDescription: migrated (0.2010s) =============================

==  ChangeVersionsNameLimit: migrating ========================================
-- change_column(:versions, :name, :string, {:limit=>nil})
   -> 0.2110s
==  ChangeVersionsNameLimit: migrated (0.2113s) ===============================

==  ChangeChangesetsRevisionToString: migrating ===============================
-- index_exists?(:changesets, [:repository_id, :revision], {:name=>:changesets_repos_rev})
   -> 0.0015s
-- remove_index(:changesets, {:name=>:changesets_repos_rev})
   -> 0.1238s
-- index_exists?(:changesets, [:repository_id, :revision], {:name=>:altered_changesets_repos_rev})
   -> 0.0010s
-- change_column(:changesets, :revision, :string, {:null=>false})
   -> 0.1665s
-- add_index(:changesets, [:repository_id, :revision], {:unique=>true, :name=>:changesets_repos_rev})
   -> 0.1563s
==  ChangeChangesetsRevisionToString: migrated (0.4503s) ======================

==  ChangeChangesFromRevisionToString: migrating ==============================
-- change_column(:changes, :from_revision, :string)
   -> 0.2022s
==  ChangeChangesFromRevisionToString: migrated (0.2025s) =====================

==  AddWikiPagesProtected: migrating ==========================================
-- add_column(:wiki_pages, :protected, :boolean, {:default=>false, :null=>false})
   -> 0.2224s
==  AddWikiPagesProtected: migrated (0.2226s) =================================

==  ChangeProjectsHomepageLimit: migrating ====================================
-- change_column(:projects, :homepage, :string, {:limit=>nil, :default=>""})
   -> 0.1775s
==  ChangeProjectsHomepageLimit: migrated (0.1778s) ===========================

==  AddWikiPagesParentId: migrating ===========================================
-- add_column(:wiki_pages, :parent_id, :integer, {:default=>nil})
   -> 0.1838s
==  AddWikiPagesParentId: migrated (0.1841s) ==================================

==  AddCommitAccessPermission: migrating ======================================
==  AddCommitAccessPermission: migrated (0.0020s) =============================

==  AddViewWikiEditsPermission: migrating =====================================
==  AddViewWikiEditsPermission: migrated (0.0020s) ============================

==  SetTopicAuthorsAsWatchers: migrating ======================================
==  SetTopicAuthorsAsWatchers: migrated (0.1255s) =============================

==  AddDeleteWikiPagesAttachmentsPermission: migrating ========================
==  AddDeleteWikiPagesAttachmentsPermission: migrated (0.0019s) ===============

==  AddChangesetsUserId: migrating ============================================
-- add_column(:changesets, :user_id, :integer, {:default=>nil})
   -> 0.1923s
==  AddChangesetsUserId: migrated (0.1925s) ===================================

==  PopulateChangesetsUserId: migrating =======================================
==  PopulateChangesetsUserId: migrated (0.0020s) ==============================

==  AddCustomFieldsEditable: migrating ========================================
-- add_column(:custom_fields, :editable, :boolean, {:default=>true})
   -> 0.1667s
==  AddCustomFieldsEditable: migrated (0.1670s) ===============================

==  SetCustomFieldsEditable: migrating ========================================
==  SetCustomFieldsEditable: migrated (0.0205s) ===============================

==  AddProjectsLftAndRgt: migrating ===========================================
-- add_column(:projects, :lft, :integer)
   -> 0.5429s
-- add_column(:projects, :rgt, :integer)
   -> 0.4348s
==  AddProjectsLftAndRgt: migrated (0.9782s) ==================================

==  BuildProjectsTree: migrating ==============================================
==  BuildProjectsTree: migrated (0.0201s) =====================================

==  RemoveProjectsProjectsCount: migrating ====================================
-- remove_column(:projects, :projects_count)
   -> 0.2020s
==  RemoveProjectsProjectsCount: migrated (0.2022s) ===========================

==  AddOpenIdAuthenticationTables: migrating ==================================
-- create_table(:open_id_authentication_associations, {:force=>true})
   -> 0.0982s
-- create_table(:open_id_authentication_nonces, {:force=>true})
   -> 0.0670s
==  AddOpenIdAuthenticationTables: migrated (0.1660s) =========================

==  AddIdentityUrlToUsers: migrating ==========================================
-- add_column(:users, :identity_url, :string)
   -> 0.2757s
==  AddIdentityUrlToUsers: migrated (0.2760s) =================================

==  AddWatchersUserIdTypeIndex: migrating =====================================
-- add_index(:watchers, [:user_id, :watchable_type], {:name=>:watchers_user_id_type})
   -> 0.1699s
==  AddWatchersUserIdTypeIndex: migrated (0.1702s) ============================

==  AddQueriesSortCriteria: migrating =========================================
-- add_column(:queries, :sort_criteria, :text)
   -> 0.1662s
==  AddQueriesSortCriteria: migrated (0.1666s) ================================

==  AddProjectsTrackersUniqueIndex: migrating =================================
-- add_index(:projects_trackers, [:project_id, :tracker_id], {:name=>:projects_trackers_unique, :unique=>true})
   -> 0.2438s
==  AddProjectsTrackersUniqueIndex: migrated (0.2459s) ========================

==  ExtendSettingsName: migrating =============================================
-- change_column(:settings, :name, :string, {:limit=>255, :default=>"", :null=>false})
   -> 0.1774s
==  ExtendSettingsName: migrated (0.1777s) ====================================

==  AddTypeToEnumerations: migrating ==========================================
-- add_column(:enumerations, :type, :string)
   -> 0.1665s
==  AddTypeToEnumerations: migrated (0.1667s) =================================

==  UpdateEnumerationsToSti: migrating ========================================
==  UpdateEnumerationsToSti: migrated (0.0050s) ===============================

==  AddActiveFieldToEnumerations: migrating ===================================
-- add_column(:enumerations, :active, :boolean, {:default=>true, :null=>false})
   -> 0.1666s
==  AddActiveFieldToEnumerations: migrated (0.1669s) ==========================

==  AddProjectToEnumerations: migrating =======================================
-- add_column(:enumerations, :project_id, :integer, {:null=>true, :default=>nil})
   -> 0.2330s
-- add_index(:enumerations, :project_id)
   -> 0.1562s
==  AddProjectToEnumerations: migrated (0.3898s) ==============================

==  AddParentIdToEnumerations: migrating ======================================
-- add_column(:enumerations, :parent_id, :integer, {:null=>true, :default=>nil})
   -> 0.1851s
==  AddParentIdToEnumerations: migrated (0.1854s) =============================

==  AddQueriesGroupBy: migrating ==============================================
-- add_column(:queries, :group_by, :string)
   -> 0.2490s
==  AddQueriesGroupBy: migrated (0.2492s) =====================================

==  CreateMemberRoles: migrating ==============================================
-- create_table(:member_roles)
   -> 0.0656s
==  CreateMemberRoles: migrated (0.0659s) =====================================

==  PopulateMemberRoles: migrating ============================================
==  PopulateMemberRoles: migrated (0.0642s) ===================================

==  DropMembersRoleId: migrating ==============================================
-- remove_column(:members, :role_id)
   -> 0.1778s
==  DropMembersRoleId: migrated (0.1781s) =====================================

==  FixMessagesStickyNull: migrating ==========================================
==  FixMessagesStickyNull: migrated (0.0013s) =================================

==  PopulateUsersType: migrating ==============================================
==  PopulateUsersType: migrated (0.0015s) =====================================

==  CreateGroupsUsers: migrating ==============================================
-- create_table(:groups_users, {:id=>false})
   -> 0.0732s
-- add_index(:groups_users, [:group_id, :user_id], {:unique=>true, :name=>:groups_users_ids})
   -> 0.1897s
==  CreateGroupsUsers: migrated (0.2633s) =====================================

==  AddMemberRolesInheritedFrom: migrating ====================================
-- add_column(:member_roles, :inherited_from, :integer)
   -> 0.1737s
==  AddMemberRolesInheritedFrom: migrated (0.1739s) ===========================

==  FixUsersCustomValues: migrating ===========================================
==  FixUsersCustomValues: migrated (0.0262s) ==================================

==  AddMissingIndexesToWorkflows: migrating ===================================
-- add_index(:workflows, :old_status_id)
   -> 0.1651s
-- add_index(:workflows, :role_id)
   -> 0.1671s
-- add_index(:workflows, :new_status_id)
   -> 0.2339s
==  AddMissingIndexesToWorkflows: migrated (0.5671s) ==========================

==  AddMissingIndexesToCustomFieldsProjects: migrating ========================
-- add_index(:custom_fields_projects, [:custom_field_id, :project_id])
   -> 0.1867s
==  AddMissingIndexesToCustomFieldsProjects: migrated (0.1870s) ===============

==  AddMissingIndexesToMessages: migrating ====================================
-- add_index(:messages, :last_reply_id)
   -> 0.1809s
-- add_index(:messages, :author_id)
   -> 0.1579s
==  AddMissingIndexesToMessages: migrated (0.3392s) ===========================

==  AddMissingIndexesToRepositories: migrating ================================
-- add_index(:repositories, :project_id)
   -> 0.1546s
==  AddMissingIndexesToRepositories: migrated (0.1549s) =======================

==  AddMissingIndexesToComments: migrating ====================================
-- add_index(:comments, [:commented_id, :commented_type])
   -> 0.1545s
-- add_index(:comments, :author_id)
   -> 0.1783s
==  AddMissingIndexesToComments: migrated (0.3334s) ===========================

==  AddMissingIndexesToEnumerations: migrating ================================
-- add_index(:enumerations, [:id, :type])
   -> 0.1635s
==  AddMissingIndexesToEnumerations: migrated (0.1640s) =======================

==  AddMissingIndexesToWikiPages: migrating ===================================
-- add_index(:wiki_pages, :wiki_id)
   -> 0.1654s
-- add_index(:wiki_pages, :parent_id)
   -> 0.1560s
==  AddMissingIndexesToWikiPages: migrated (0.3222s) ==========================

==  AddMissingIndexesToWatchers: migrating ====================================
-- add_index(:watchers, :user_id)
   -> 0.1801s
-- add_index(:watchers, [:watchable_id, :watchable_type])
   -> 0.1893s
==  AddMissingIndexesToWatchers: migrated (0.3700s) ===========================

==  AddMissingIndexesToAuthSources: migrating =================================
-- add_index(:auth_sources, [:id, :type])
   -> 0.1663s
==  AddMissingIndexesToAuthSources: migrated (0.1665s) ========================

==  AddMissingIndexesToDocuments: migrating ===================================
-- add_index(:documents, :category_id)
   -> 0.1588s
==  AddMissingIndexesToDocuments: migrated (0.1591s) ==========================

==  AddMissingIndexesToTokens: migrating ======================================
-- add_index(:tokens, :user_id)
   -> 0.1661s
==  AddMissingIndexesToTokens: migrated (0.1664s) =============================

==  AddMissingIndexesToChangesets: migrating ==================================
-- add_index(:changesets, :user_id)
   -> 0.1548s
-- add_index(:changesets, :repository_id)
   -> 0.1450s
==  AddMissingIndexesToChangesets: migrated (0.3002s) =========================

==  AddMissingIndexesToIssueCategories: migrating =============================
-- add_index(:issue_categories, :assigned_to_id)
   -> 0.1763s
==  AddMissingIndexesToIssueCategories: migrated (0.1766s) ====================

==  AddMissingIndexesToMemberRoles: migrating =================================
-- add_index(:member_roles, :member_id)
   -> 0.2431s
-- add_index(:member_roles, :role_id)
   -> 0.1673s
==  AddMissingIndexesToMemberRoles: migrated (0.4108s) ========================

==  AddMissingIndexesToBoards: migrating ======================================
-- add_index(:boards, :last_message_id)
   -> 0.2428s
==  AddMissingIndexesToBoards: migrated (0.2430s) =============================

==  AddMissingIndexesToUserPreferences: migrating =============================
-- add_index(:user_preferences, :user_id)
   -> 0.1570s
==  AddMissingIndexesToUserPreferences: migrated (0.1572s) ====================

==  AddMissingIndexesToIssues: migrating ======================================
-- add_index(:issues, :status_id)
   -> 0.1730s
-- add_index(:issues, :category_id)
   -> 0.1559s
-- add_index(:issues, :assigned_to_id)
   -> 0.1672s
-- add_index(:issues, :fixed_version_id)
   -> 0.2129s
-- add_index(:issues, :tracker_id)
   -> 0.4810s
-- add_index(:issues, :priority_id)
   -> 0.3547s
-- add_index(:issues, :author_id)
   -> 0.1673s
==  AddMissingIndexesToIssues: migrated (1.7134s) =============================

==  AddMissingIndexesToMembers: migrating =====================================
-- add_index(:members, :user_id)
   -> 0.2548s
-- add_index(:members, :project_id)
   -> 0.1782s
==  AddMissingIndexesToMembers: migrated (0.4337s) ============================

==  AddMissingIndexesToCustomFields: migrating ================================
-- add_index(:custom_fields, [:id, :type])
   -> 0.1790s
==  AddMissingIndexesToCustomFields: migrated (0.1794s) =======================

==  AddMissingIndexesToQueries: migrating =====================================
-- add_index(:queries, :project_id)
   -> 0.2265s
-- add_index(:queries, :user_id)
   -> 0.1560s
==  AddMissingIndexesToQueries: migrated (0.3830s) ============================

==  AddMissingIndexesToTimeEntries: migrating =================================
-- add_index(:time_entries, :activity_id)
   -> 0.1605s
-- add_index(:time_entries, :user_id)
   -> 0.1561s
==  AddMissingIndexesToTimeEntries: migrated (0.3170s) ========================

==  AddMissingIndexesToNews: migrating ========================================
-- add_index(:news, :author_id)
   -> 0.1664s
==  AddMissingIndexesToNews: migrated (0.1667s) ===============================

==  AddMissingIndexesToUsers: migrating =======================================
-- add_index(:users, [:id, :type])
   -> 0.2437s
-- add_index(:users, :auth_source_id)
   -> 0.1754s
==  AddMissingIndexesToUsers: migrated (0.4195s) ==============================

==  AddMissingIndexesToAttachments: migrating =================================
-- add_index(:attachments, [:container_id, :container_type])
   -> 0.1845s
-- add_index(:attachments, :author_id)
   -> 0.2228s
==  AddMissingIndexesToAttachments: migrated (0.4077s) ========================

==  AddMissingIndexesToWikiContents: migrating ================================
-- add_index(:wiki_contents, :author_id)
   -> 0.1625s
==  AddMissingIndexesToWikiContents: migrated (0.1628s) =======================

==  AddMissingIndexesToCustomValues: migrating ================================
-- add_index(:custom_values, :custom_field_id)
   -> 0.1809s
==  AddMissingIndexesToCustomValues: migrated (0.1812s) =======================

==  AddMissingIndexesToJournals: migrating ====================================
-- add_index(:journals, :user_id)
   -> 0.1707s
-- add_index(:journals, :journalized_id)
   -> 0.1561s
==  AddMissingIndexesToJournals: migrated (0.3272s) ===========================

==  AddMissingIndexesToIssueRelations: migrating ==============================
-- add_index(:issue_relations, :issue_from_id)
   -> 0.1992s
-- add_index(:issue_relations, :issue_to_id)
   -> 0.1672s
==  AddMissingIndexesToIssueRelations: migrated (0.3668s) =====================

==  AddMissingIndexesToWikiRedirects: migrating ===============================
-- add_index(:wiki_redirects, :wiki_id)
   -> 0.1709s
==  AddMissingIndexesToWikiRedirects: migrated (0.1712s) ======================

==  AddMissingIndexesToCustomFieldsTrackers: migrating ========================
-- add_index(:custom_fields_trackers, [:custom_field_id, :tracker_id])
   -> 0.1546s
==  AddMissingIndexesToCustomFieldsTrackers: migrated (0.1549s) ===============

==  AddActivityIndexes: migrating =============================================
-- add_index(:journals, :created_on)
   -> 0.2548s
-- add_index(:changesets, :committed_on)
   -> 0.1672s
-- add_index(:wiki_content_versions, :updated_on)
   -> 0.1672s
-- add_index(:messages, :created_on)
   -> 0.1450s
-- add_index(:issues, :created_on)
   -> 0.1671s
-- add_index(:news, :created_on)
   -> 0.1562s
-- add_index(:attachments, :created_on)
   -> 0.2115s
-- add_index(:documents, :created_on)
   -> 0.1672s
-- add_index(:time_entries, :created_on)
   -> 0.2229s
==  AddActivityIndexes: migrated (1.6608s) ====================================

==  AddVersionsStatus: migrating ==============================================
-- add_column(:versions, :status, :string, {:default=>"open"})
   -> 0.1872s
==  AddVersionsStatus: migrated (0.1905s) =====================================

==  AddViewIssuesPermission: migrating ========================================
==  AddViewIssuesPermission: migrated (0.0157s) ===============================

==  AddDefaultDoneRatioToIssueStatus: migrating ===============================
-- add_column(:issue_statuses, :default_done_ratio, :integer)
   -> 0.1773s
==  AddDefaultDoneRatioToIssueStatus: migrated (0.1776s) ======================

==  AddVersionsSharing: migrating =============================================
-- add_column(:versions, :sharing, :string, {:default=>"none", :null=>false})
   -> 0.2206s
-- add_index(:versions, :sharing)
   -> 0.1674s
==  AddVersionsSharing: migrated (0.3885s) ====================================

==  AddLftAndRgtIndexesToProjects: migrating ==================================
-- add_index(:projects, :lft)
   -> 0.1542s
-- add_index(:projects, :rgt)
   -> 0.2115s
==  AddLftAndRgtIndexesToProjects: migrated (0.3664s) =========================

==  AddIndexToSettingsName: migrating =========================================
-- add_index(:settings, :name)
   -> 0.1660s
==  AddIndexToSettingsName: migrated (0.1662s) ================================

==  AddIndexesToIssueStatus: migrating ========================================
-- add_index(:issue_statuses, :position)
   -> 0.1550s
-- add_index(:issue_statuses, :is_closed)
   -> 0.2116s
-- add_index(:issue_statuses, :is_default)
   -> 0.1562s
==  AddIndexesToIssueStatus: migrated (0.5232s) ===============================

==  RemoveEnumerationsOpt: migrating ==========================================
-- remove_column(:enumerations, :opt)
   -> 0.1793s
==  RemoveEnumerationsOpt: migrated (0.1795s) =================================

==  ChangeWikiContentsTextLimit: migrating ====================================
-- change_column(:wiki_contents, :text, :text, {:limit=>16777216})
   -> 0.1902s
-- change_column(:wiki_content_versions, :data, :binary, {:limit=>16777216})
   -> 0.2124s
==  ChangeWikiContentsTextLimit: migrated (0.4033s) ===========================

==  ChangeUsersMailNotificationToString: migrating ============================
-- rename_column(:users, :mail_notification, :mail_notification_bool)
   -> 0.3889s
-- add_column(:users, :mail_notification, :string, {:default=>"", :null=>false})
   -> 0.2791s
-- remove_column(:users, :mail_notification_bool)
   -> 0.5211s
==  ChangeUsersMailNotificationToString: migrated (1.2261s) ===================

==  UpdateMailNotificationValues: migrating ===================================
==  UpdateMailNotificationValues: migrated (0.0000s) ==========================

==  AddIndexOnChangesetsScmid: migrating ======================================
-- add_index(:changesets, [:repository_id, :scmid], {:name=>:changesets_repos_scmid})
   -> 0.3329s
==  AddIndexOnChangesetsScmid: migrated (0.3332s) =============================

==  AddIssuesNestedSetsColumns: migrating =====================================
-- add_column(:issues, :parent_id, :integer, {:default=>nil})
   -> 0.2232s
-- add_column(:issues, :root_id, :integer, {:default=>nil})
   -> 0.1695s
-- add_column(:issues, :lft, :integer, {:default=>nil})
   -> 0.1790s
-- add_column(:issues, :rgt, :integer, {:default=>nil})
   -> 0.1790s
==  AddIssuesNestedSetsColumns: migrated (0.9515s) ============================

==  AddIndexOnIssuesNestedSet: migrating ======================================
-- add_index(:issues, [:root_id, :lft, :rgt])
   -> 0.2467s
==  AddIndexOnIssuesNestedSet: migrated (0.2469s) =============================

==  ChangeChangesPathLengthLimit: migrating ===================================
-- change_column(:changes, :path, :text, {:default=>nil, :null=>true})
   -> 0.2288s
-- change_column(:changes, :path, :text, {:null=>false})
   -> 0.1790s
-- change_column(:changes, :from_path, :text)
   -> 0.2793s
==  ChangeChangesPathLengthLimit: migrated (0.6878s) ==========================

==  EnableCalendarAndGanttModulesWhereAppropriate: migrating ==================
==  EnableCalendarAndGanttModulesWhereAppropriate: migrated (0.0639s) =========

==  AddUniqueIndexOnMembers: migrating ========================================
-- add_index(:members, [:user_id, :project_id], {:unique=>true})
   -> 0.1511s
==  AddUniqueIndexOnMembers: migrated (0.1566s) ===============================

==  AddCustomFieldsVisible: migrating =========================================
-- add_column(:custom_fields, :visible, :boolean, {:null=>false, :default=>true})
   -> 0.2281s
==  AddCustomFieldsVisible: migrated (0.2300s) ================================

==  ChangeProjectsNameLimit: migrating ========================================
-- change_column(:projects, :name, :string, {:limit=>nil, :default=>"", :null=>false})
   -> 0.1931s
==  ChangeProjectsNameLimit: migrated (0.1934s) ===============================

==  ChangeProjectsIdentifierLimit: migrating ==================================
-- change_column(:projects, :identifier, :string, {:limit=>nil})
   -> 0.1923s
==  ChangeProjectsIdentifierLimit: migrated (0.1925s) =========================

==  AddWorkflowsAssigneeAndAuthor: migrating ==================================
-- add_column(:workflows, :assignee, :boolean, {:null=>false, :default=>false})
   -> 0.2463s
-- add_column(:workflows, :author, :boolean, {:null=>false, :default=>false})
   -> 0.1678s
==  AddWorkflowsAssigneeAndAuthor: migrated (0.4383s) =========================

==  AddUsersSalt: migrating ===================================================
-- add_column(:users, :salt, :string, {:limit=>64})
   -> 0.3389s
==  AddUsersSalt: migrated (0.3392s) ==========================================

==  SaltUserPasswords: migrating ==============================================
-- Salting user passwords, this may take some time...
   -> 0.1854s
==  SaltUserPasswords: migrated (0.1856s) =====================================

==  AddRepositoriesPathEncoding: migrating ====================================
-- add_column(:repositories, :path_encoding, :string, {:limit=>64, :default=>nil})
   -> 0.1931s
==  AddRepositoriesPathEncoding: migrated (0.1933s) ===========================

==  ChangeRepositoriesPasswordLimit: migrating ================================
-- change_column(:repositories, :password, :string, {:limit=>nil, :default=>""})
   -> 0.1772s
==  ChangeRepositoriesPasswordLimit: migrated (0.1776s) =======================

==  ChangeAuthSourcesAccountPasswordLimit: migrating ==========================
-- change_column(:auth_sources, :account_password, :string, {:limit=>nil, :default=>""})
   -> 0.2455s
==  ChangeAuthSourcesAccountPasswordLimit: migrated (0.2458s) =================

==  ChangeJournalDetailsValuesToText: migrating ===============================
-- change_column(:journal_details, :old_value, :text)
   -> 0.1665s
-- change_column(:journal_details, :value, :text)
   -> 0.2343s
==  ChangeJournalDetailsValuesToText: migrated (0.4019s) ======================

==  AddRepositoriesLogEncoding: migrating =====================================
-- add_column(:repositories, :log_encoding, :string, {:limit=>64, :default=>nil})
   -> 0.2327s
==  AddRepositoriesLogEncoding: migrated (0.2330s) ============================

==  CopyRepositoriesLogEncoding: migrating ====================================
==  CopyRepositoriesLogEncoding: migrated (0.0129s) ===========================

==  AddIndexToUsersType: migrating ============================================
-- add_index(:users, :type)
   -> 0.2005s
==  AddIndexToUsersType: migrated (0.2007s) ===================================

==  AddRolesIssuesVisibility: migrating =======================================
-- add_column(:roles, :issues_visibility, :string, {:limit=>30, :default=>"default", :null=>false})
   -> 0.2754s
==  AddRolesIssuesVisibility: migrated (0.2757s) ==============================

==  AddIssuesIsPrivate: migrating =============================================
-- add_column(:issues, :is_private, :boolean, {:default=>false, :null=>false})
   -> 0.2390s
==  AddIssuesIsPrivate: migrated (0.2392s) ====================================

==  AddRepositoriesExtraInfo: migrating =======================================
-- add_column(:repositories, :extra_info, :text)
   -> 0.2082s
==  AddRepositoriesExtraInfo: migrated (0.2084s) ==============================

==  CreateChangesetParents: migrating =========================================
-- create_table(:changeset_parents, {:id=>false})
   -> 0.2205s
-- add_index(:changeset_parents, [:changeset_id], {:unique=>false, :name=>:changeset_parents_changeset_ids})
   -> 0.1565s
-- add_index(:changeset_parents, [:parent_id], {:unique=>false, :name=>:changeset_parents_parent_ids})
   -> 0.2225s
==  CreateChangesetParents: migrated (0.6008s) ================================

==  AddUniqueIndexToIssueRelations: migrating =================================
-- add_index(:issue_relations, [:issue_from_id, :issue_to_id], {:unique=>true})
   -> 0.2643s
==  AddUniqueIndexToIssueRelations: migrated (0.2656s) ========================

==  AddRepositoriesIdentifier: migrating ======================================
-- add_column(:repositories, :identifier, :string)
   -> 0.1945s
==  AddRepositoriesIdentifier: migrated (0.1948s) =============================

==  AddRepositoriesIsDefault: migrating =======================================
-- add_column(:repositories, :is_default, :boolean, {:default=>false})
   -> 0.1792s
==  AddRepositoriesIsDefault: migrated (0.1795s) ==============================

==  SetDefaultRepositories: migrating =========================================
==  SetDefaultRepositories: migrated (0.0023s) ================================

==  AddCustomFieldsMultiple: migrating ========================================
-- add_column(:custom_fields, :multiple, :boolean, {:default=>false})
   -> 0.1666s
==  AddCustomFieldsMultiple: migrated (0.1671s) ===============================

==  ChangeUsersLoginLimit: migrating ==========================================
-- change_column(:users, :login, :string, {:limit=>nil, :default=>"", :null=>false})
   -> 0.2340s
==  ChangeUsersLoginLimit: migrated (0.2343s) =================================

==  ChangeAttachmentsContainerDefaults: migrating =============================
-- remove_index(:attachments, [:container_id, :container_type])
   -> 0.0987s
-- change_column(:attachments, :container_id, :integer, {:default=>nil, :null=>true})
   -> 0.2232s
-- change_column(:attachments, :container_type, :string, {:limit=>30, :default=>nil, :null=>true})
   -> 0.1900s
-- add_index(:attachments, [:container_id, :container_type])
   -> 0.1626s
==  ChangeAttachmentsContainerDefaults: migrated (0.6809s) ====================

==  AddAuthSourcesFilter: migrating ===========================================
-- add_column(:auth_sources, :filter, :string)
   -> 0.5584s
==  AddAuthSourcesFilter: migrated (0.5588s) ==================================

==  ChangeRepositoriesToFullSti: migrating ====================================
==  ChangeRepositoriesToFullSti: migrated (0.0007s) ===========================

==  AddTrackersFieldsBits: migrating ==========================================
-- add_column(:trackers, :fields_bits, :integer, {:default=>0})
   -> 0.2519s
==  AddTrackersFieldsBits: migrated (0.2522s) =================================

==  AddAuthSourcesTimeout: migrating ==========================================
-- add_column(:auth_sources, :timeout, :integer)
   -> 0.1717s
==  AddAuthSourcesTimeout: migrated (0.1721s) =================================

==  AddWorkflowsType: migrating ===============================================
-- add_column(:workflows, :type, :string, {:limit=>30})
   -> 0.2137s
==  AddWorkflowsType: migrated (0.2139s) ======================================

==  UpdateWorkflowsToSti: migrating ===========================================
==  UpdateWorkflowsToSti: migrated (0.0014s) ==================================

==  AddWorkflowsRuleFields: migrating =========================================
-- add_column(:workflows, :field_name, :string, {:limit=>30})
   -> 0.1772s
-- add_column(:workflows, :rule, :string, {:limit=>30})
   -> 0.2123s
==  AddWorkflowsRuleFields: migrated (0.3903s) ================================

==  AddBoardsParentId: migrating ==============================================
-- add_column(:boards, :parent_id, :integer)
   -> 0.1771s
==  AddBoardsParentId: migrated (0.1775s) =====================================

==  AddJournalsPrivateNotes: migrating ========================================
-- add_column(:journals, :private_notes, :boolean, {:default=>false, :null=>false})
   -> 0.1914s
==  AddJournalsPrivateNotes: migrated (0.1919s) ===============================

==  AddEnumerationsPositionName: migrating ====================================
-- add_column(:enumerations, :position_name, :string, {:limit=>30})
   -> 0.1776s
==  AddEnumerationsPositionName: migrated (0.1778s) ===========================

==  PopulateEnumerationsPositionName: migrating ===============================
==  PopulateEnumerationsPositionName: migrated (0.0041s) ======================

==  AddQueriesType: migrating =================================================
-- add_column(:queries, :type, :string)
   -> 0.2888s
==  AddQueriesType: migrated (0.2890s) ========================================

==  UpdateQueriesToSti: migrating =============================================
==  UpdateQueriesToSti: migrated (0.0576s) ====================================

==  AddAttachmentsDiskDirectory: migrating ====================================
-- add_column(:attachments, :disk_directory, :string)
   -> 0.2224s
==  AddAttachmentsDiskDirectory: migrated (0.2226s) ===========================

==  SplitDocumentsPermissions: migrating ======================================
==  SplitDocumentsPermissions: migrated (0.0029s) =============================

==  AddUniqueIndexOnTokensValue: migrating ====================================
-- Adding unique index on tokens, this may take some time...
-- add_index(:tokens, :value, {:unique=>true, :name=>"tokens_value"})
   -> 0.2003s
   -> 0.2100s
==  AddUniqueIndexOnTokensValue: migrated (0.2102s) ===========================

==  AddProjectsInheritMembers: migrating ======================================
-- add_column(:projects, :inherit_members, :boolean, {:default=>false, :null=>false})
   -> 0.2339s
==  AddProjectsInheritMembers: migrated (0.2342s) =============================

==  AddUniqueIndexOnCustomFieldsTrackers: migrating ===========================
-- index_exists?(:custom_fields_trackers, [:custom_field_id, :tracker_id])
   -> 0.0010s
-- remove_index(:custom_fields_trackers, [:custom_field_id, :tracker_id])
   -> 0.1337s
-- add_index(:custom_fields_trackers, [:custom_field_id, :tracker_id], {:unique=>true})
   -> 0.1890s
==  AddUniqueIndexOnCustomFieldsTrackers: migrated (0.3258s) ==================

==  AddUniqueIndexOnCustomFieldsProjects: migrating ===========================
-- index_exists?(:custom_fields_projects, [:custom_field_id, :project_id])
   -> 0.0010s
-- remove_index(:custom_fields_projects, [:custom_field_id, :project_id])
   -> 0.1412s
-- add_index(:custom_fields_projects, [:custom_field_id, :project_id], {:unique=>true})
   -> 0.2165s
==  AddUniqueIndexOnCustomFieldsProjects: migrated (0.3605s) ==================

==  ChangeUsersLastnameLengthTo255: migrating =================================
-- change_column(:users, :lastname, :string, {:limit=>255, :default=>"", :null=>false})
   -> 0.2966s
==  ChangeUsersLastnameLengthTo255: migrated (0.2969s) ========================

==  AddIssuesClosedOn: migrating ==============================================
-- add_column(:issues, :closed_on, :datetime, {:default=>nil})
   -> 0.1779s
==  AddIssuesClosedOn: migrated (0.1781s) =====================================

==  PopulateIssuesClosedOn: migrating =========================================
==  PopulateIssuesClosedOn: migrated (0.0029s) ================================

==  RemoveIssuesDefaultFkValues: migrating ====================================
-- change_column_default(:issues, :tracker_id, nil)
   -> 0.0516s
-- change_column_default(:issues, :project_id, nil)
   -> 0.0448s
-- change_column_default(:issues, :status_id, nil)
   -> 0.0892s
-- change_column_default(:issues, :assigned_to_id, nil)
   -> 0.0895s
-- change_column_default(:issues, :priority_id, nil)
   -> 0.0447s
-- change_column_default(:issues, :author_id, nil)
   -> 0.0448s
==  RemoveIssuesDefaultFkValues: migrated (0.3660s) ===========================

==  CreateQueriesRoles: migrating =============================================
-- create_table(:queries_roles, {:id=>false})
   -> 0.0655s
-- add_index(:queries_roles, [:query_id, :role_id], {:unique=>true, :name=>:queries_roles_ids})
   -> 0.1897s
==  CreateQueriesRoles: migrated (0.2557s) ====================================

==  AddQueriesVisibility: migrating ===========================================
-- add_column(:queries, :visibility, :integer, {:default=>0})
   -> 0.1902s
-- remove_column(:queries, :is_public)
   -> 0.1745s
==  AddQueriesVisibility: migrated (0.3697s) ==================================

==  CreateCustomFieldsRoles: migrating ========================================
-- create_table(:custom_fields_roles, {:id=>false})
   -> 0.1435s
-- add_index(:custom_fields_roles, [:custom_field_id, :role_id], {:unique=>true, :name=>:custom_fields_roles_ids})
   -> 0.2339s
==  CreateCustomFieldsRoles: migrated (0.3796s) ===============================

==  AddQueriesOptions: migrating ==============================================
-- add_column(:queries, :options, :text)
   -> 0.2216s
==  AddQueriesOptions: migrated (0.2218s) =====================================

==  AddUsersMustChangePasswd: migrating =======================================
-- add_column(:users, :must_change_passwd, :boolean, {:default=>false, :null=>false})
   -> 0.2111s
==  AddUsersMustChangePasswd: migrated (0.2115s) ==============================

==  RemoveEolsFromAttachmentsFilename: migrating ==============================
==  RemoveEolsFromAttachmentsFilename: migrated (0.0054s) =====================

==  SupportForMultipleCommitKeywords: migrating ===============================
==  SupportForMultipleCommitKeywords: migrated (0.0060s) ======================

==  AddRepositoriesCreatedOn: migrating =======================================
-- add_column(:repositories, :created_on, :timestamp)
   -> 0.1843s
==  AddRepositoriesCreatedOn: migrated (0.1847s) ==============================

==  AddCustomFieldsFormatStore: migrating =====================================
-- add_column(:custom_fields, :format_store, :text)
   -> 0.1682s
==  AddCustomFieldsFormatStore: migrated (0.1685s) ============================

==  AddCustomFieldsDescription: migrating =====================================
-- add_column(:custom_fields, :description, :text)
   -> 0.5339s
==  AddCustomFieldsDescription: migrated (0.5344s) ============================

==  RemoveCustomFieldsMinMaxLengthDefaultValues: migrating ====================
-- change_column(:custom_fields, :min_length, :int, {:default=>nil, :null=>true})
   -> 0.3448s
-- change_column(:custom_fields, :max_length, :int, {:default=>nil, :null=>true})
   -> 0.1786s
==  RemoveCustomFieldsMinMaxLengthDefaultValues: migrated (0.5269s) ===========

==  StoreRelationTypeInJournalDetails: migrating ==============================
==  StoreRelationTypeInJournalDetails: migrated (0.0179s) =====================

==  DeleteOrphanTimeEntriesCustomValues: migrating ============================
==  DeleteOrphanTimeEntriesCustomValues: migrated (0.0017s) ===================

==  ChangeChangesetsCommentsLimit: migrating ==================================
-- change_column(:changesets, :comments, :text, {:limit=>16777216})
   -> 0.2209s
==  ChangeChangesetsCommentsLimit: migrated (0.2213s) =========================

==  AddPasswordChangedAtToUser: migrating =====================================
-- add_column(:users, :passwd_changed_on, :datetime)
   -> 0.2002s
==  AddPasswordChangedAtToUser: migrated (0.2004s) ============================

==  InsertBuiltinGroups: migrating ============================================
==  InsertBuiltinGroups: migrated (0.3561s) ===================================

daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ RAILS_ENV=production rake redmine:load_default_data

Select language: ar, az, bg, bs, ca, cs, da, de, el, en, en-GB, es, et, eu, fa, fi, fr, gl, he, hr, hu, id, it, ja, ko, lt, lv, mk, mn, nl, no, pl, pt, pt-BR, ro, ru, sk, sl, sq, sr, sr-YU, sv, th, tr, uk, vi, zh, zh-TW [en]
====================================
Default configuration data loaded.
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ ls
app  config  config.ru  CONTRIBUTING.md  db  doc  extra  files  Gemfile  Gemfile.lock  lib  log  plugins  public  Rakefile  README.rdoc  script  test  tmp  vendor
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ ls tmp/
cache  pdf  sessions  sockets  test  thumbnails
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ ls public/
404.html  500.html  dispatch.fcgi.example  favicon.ico  help  htaccess.fcgi.example  images  javascripts  stylesheets  themes
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ ls files/
delete.me
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ mkdir -p tmp tmp/pdf public/plugin_assets
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ sudo chown -R redmine:redmine files log tmp public/plugin_assets
chown: invalid user: ‘redmine:redmine’
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ sudo chmod -R 755 files log tmp public/plugin_assets
daniel@danielhan-IdeaPad-U150:~/Documents/klarna/redmine-2.6.0$ ruby script/rails server webrick -e production
=> Booting WEBrick
=> Rails 3.2.19 application starting in production on http://0.0.0.0:3000
=> Call with -d to detach
=> Ctrl-C to shutdown server
[2014-11-26 23:19:54] INFO  WEBrick 1.3.1
[2014-11-26 23:19:54] INFO  ruby 2.1.2 (2014-05-08) [i386-linux-gnu]
[2014-11-26 23:19:54] INFO  WEBrick::HTTPServer#start: pid=19326 port=3000
Started GET "/" for 127.0.0.1 at 2014-11-26 23:20:11 +0100
Processing by WelcomeController#index as HTML
  Current user: anonymous
  Rendered welcome/index.html.erb within layouts/base (122.7ms)
Completed 200 OK in 778.8ms (Views: 226.5ms | ActiveRecord: 81.8ms)
Started GET "/login" for 127.0.0.1 at 2014-11-26 23:20:30 +0100
Processing by AccountController#login as HTML
  Current user: anonymous
  Rendered account/login.html.erb within layouts/base (13.3ms)
Completed 200 OK in 71.8ms (Views: 62.8ms | ActiveRecord: 2.8ms)
Started POST "/login" for 127.0.0.1 at 2014-11-26 23:20:38 +0100
Processing by AccountController#login as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"6iVtyMujXTUuqFoGhn53ZnNF8ydBOb5oKhI+guIsu/A=", "back_url"=>"http://localhost:3000/", "username"=>"admin", "password"=>"[FILTERED]", "login"=>"Login »"}
  Current user: anonymous
Successful authentication for 'admin' from 127.0.0.1 at 2014-11-26 22:20:38 UTC
Redirected to http://localhost:3000/
Completed 302 Found in 56.9ms (ActiveRecord: 35.1ms)
Started GET "/" for 127.0.0.1 at 2014-11-26 23:20:38 +0100
Processing by WelcomeController#index as HTML
  Current user: admin (id=1)
  Rendered welcome/index.html.erb within layouts/base (161.7ms)
Completed 200 OK in 275.4ms (Views: 94.4ms | ActiveRecord: 162.3ms)
Started GET "/" for 151.177.25.37 at 2014-11-26 23:24:03 +0100
Processing by WelcomeController#index as HTML
  Current user: anonymous
  Rendered welcome/index.html.erb within layouts/base (2.4ms)
Completed 200 OK in 34.8ms (Views: 17.1ms | ActiveRecord: 3.1ms)
Started GET "/login" for 151.177.25.37 at 2014-11-26 23:24:09 +0100
Processing by AccountController#login as HTML
  Current user: anonymous
  Rendered account/login.html.erb within layouts/base (2.9ms)
Completed 200 OK in 22.0ms (Views: 16.8ms | ActiveRecord: 0.8ms)
Started POST "/login" for 151.177.25.37 at 2014-11-26 23:24:15 +0100
Processing by AccountController#login as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"87TbBdo5Y9KlxRkHwWsngpOYqIf7MBw+WqAfF+0jW1k=", "back_url"=>"http://151.177.25.37:3000/", "username"=>"admin", "password"=>"[FILTERED]", "login"=>"Login »"}
  Current user: anonymous
Successful authentication for 'admin' from 151.177.25.37 at 2014-11-26 22:24:15 UTC
Redirected to http://151.177.25.37:3000/
Completed 302 Found in 62.3ms (ActiveRecord: 54.7ms)
Started GET "/" for 151.177.25.37 at 2014-11-26 23:24:15 +0100
Processing by WelcomeController#index as HTML
  Current user: admin (id=1)
  Rendered welcome/index.html.erb within layouts/base (5.4ms)
Completed 200 OK in 41.3ms (Views: 26.5ms | ActiveRecord: 4.0ms)
Started GET "/my/account" for 127.0.0.1 at 2014-11-26 23:25:05 +0100
Processing by MyController#account as HTML
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (39.5ms)
  Rendered users/_preferences.html.erb (641.4ms)
  Rendered my/_sidebar.html.erb (19.6ms)
  Rendered my/account.html.erb within layouts/base (4337.8ms)
Completed 200 OK in 4393.8ms (Views: 4379.2ms | ActiveRecord: 5.4ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-26 23:25:20 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (16.8ms)
  Rendered admin/index.html.erb within layouts/admin (30.4ms)
  Rendered layouts/base.html.erb (23.8ms)
Completed 200 OK in 139.7ms (Views: 129.4ms | ActiveRecord: 2.0ms)
Started GET "/admin/projects" for 127.0.0.1 at 2014-11-26 23:25:22 +0100
Processing by AdminController#projects as HTML
  Current user: admin (id=1)
  Rendered admin/projects.html.erb within layouts/admin (9.5ms)
  Rendered admin/_menu.html.erb (11.0ms)
  Rendered layouts/base.html.erb (24.9ms)
Completed 200 OK in 86.9ms (Views: 74.4ms | ActiveRecord: 2.6ms)
Started GET "/projects" for 127.0.0.1 at 2014-11-26 23:25:36 +0100
Processing by ProjectsController#index as HTML
  Current user: admin (id=1)
  Rendered projects/index.html.erb within layouts/base (12.8ms)
Completed 200 OK in 72.7ms (Views: 61.3ms | ActiveRecord: 1.9ms)
Started GET "/projects/new" for 127.0.0.1 at 2014-11-26 23:25:38 +0100
Processing by ProjectsController#new as HTML
  Current user: admin (id=1)
  Rendered projects/_form.html.erb (35.0ms)
  Rendered projects/new.html.erb within layouts/base (42.8ms)
Completed 200 OK in 183.1ms (Views: 62.8ms | ActiveRecord: 10.8ms)
Started POST "/projects" for 127.0.0.1 at 2014-11-26 23:26:03 +0100
Processing by ProjectsController#create as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "project"=>{"name"=>"test project", "description"=>"test", "identifier"=>"test-project", "homepage"=>"", "is_public"=>"1", "inherit_members"=>"0", "enabled_module_names"=>["issue_tracking", "time_tracking", "news", "documents", "files", "wiki", "repository", "boards", "calendar", "gantt", ""], "tracker_ids"=>["1", "2", "3", ""]}, "commit"=>"Create"}
  Current user: admin (id=1)
Redirected to http://localhost:3000/projects/test-project/settings
Expire fragment views/localhost:3000/robots.txt 0.3ms
Completed 302 Found in 285.9ms (ActiveRecord: 75.0ms)
Started GET "/projects/test-project/settings" for 127.0.0.1 at 2014-11-26 23:26:03 +0100
Processing by ProjectsController#settings as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered projects/_form.html.erb (28.2ms)
  Rendered projects/_edit.html.erb (32.8ms)
  Rendered projects/settings/_modules.html.erb (9.8ms)
  Rendered projects/settings/_members.html.erb (81.8ms)
  Rendered projects/settings/_versions.html.erb (20.5ms)
  Rendered projects/settings/_issue_categories.html.erb (8.6ms)
  Rendered projects/settings/_wiki.html.erb (6.6ms)
  Rendered projects/settings/_repositories.html.erb (33.2ms)
  Rendered projects/settings/_boards.html.erb (12.1ms)
  Rendered projects/settings/_activities.html.erb (62.2ms)
  Rendered common/_tabs.html.erb (321.1ms)
  Rendered projects/settings.html.erb within layouts/base (336.7ms)
Completed 200 OK in 455.9ms (Views: 376.1ms | ActiveRecord: 31.7ms)
Started GET "/projects/test-project/activity" for 127.0.0.1 at 2014-11-26 23:26:18 +0100
Processing by ActivitiesController#index as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered activities/index.html.erb within layouts/base (35.6ms)
Completed 200 OK in 283.4ms (Views: 142.0ms | ActiveRecord: 32.5ms)
Started GET "/projects/test-project" for 127.0.0.1 at 2014-11-26 23:26:19 +0100
Processing by ProjectsController#show as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered projects/_members_box.html.erb (1.4ms)
  Rendered projects/_sidebar.html.erb (4.5ms)
  Rendered projects/show.html.erb within layouts/base (36.4ms)
Completed 200 OK in 194.5ms (Views: 118.5ms | ActiveRecord: 16.3ms)
Started GET "/projects/test-project/activity" for 127.0.0.1 at 2014-11-26 23:26:25 +0100
Processing by ActivitiesController#index as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered activities/index.html.erb within layouts/base (26.8ms)
Completed 200 OK in 163.7ms (Views: 70.6ms | ActiveRecord: 9.0ms)
Started GET "/projects/test-project/issues" for 127.0.0.1 at 2014-11-26 23:26:26 +0100
Processing by IssuesController#index as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered queries/_filters.html.erb (27.6ms)
  Rendered queries/_columns.html.erb (11.4ms)
  Rendered issues/_sidebar.html.erb (13.4ms)
  Rendered issues/index.html.erb within layouts/base (131.6ms)
Completed 200 OK in 396.4ms (Views: 213.8ms | ActiveRecord: 20.1ms)
Started GET "/projects/test-project/issues/new" for 127.0.0.1 at 2014-11-26 23:26:29 +0100
Processing by IssuesController#new as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered issues/_form_custom_fields.html.erb (13.3ms)
  Rendered issues/_attributes.html.erb (61.3ms)
  Rendered issues/_form.html.erb (104.8ms)
  Rendered attachments/_form.html.erb (10.6ms)
  Rendered issues/new.html.erb within layouts/base (161.3ms)
Completed 200 OK in 437.7ms (Views: 222.5ms | ActiveRecord: 23.5ms)
Started GET "/projects/test-project/issues/gantt" for 127.0.0.1 at 2014-11-26 23:26:31 +0100
Processing by GanttsController#show as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered queries/_filters.html.erb (25.0ms)
  Rendered issues/_sidebar.html.erb (13.0ms)
  Rendered gantts/show.html.erb within layouts/base (124.0ms)
Completed 200 OK in 328.8ms (Views: 191.9ms | ActiveRecord: 75.5ms)
Started GET "/projects/test-project/issues/calendar" for 127.0.0.1 at 2014-11-26 23:26:34 +0100
Processing by CalendarsController#show as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered queries/_filters.html.erb (24.0ms)
  Rendered common/_calendar.html.erb (10.7ms)
  Rendered issues/_sidebar.html.erb (9.3ms)
  Rendered calendars/show.html.erb within layouts/base (79.7ms)
Completed 200 OK in 227.3ms (Views: 153.1ms | ActiveRecord: 11.0ms)
Started GET "/projects/test-project/news" for 127.0.0.1 at 2014-11-26 23:26:37 +0100
Processing by NewsController#index as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered attachments/_form.html.erb (6.3ms)
  Rendered news/_form.html.erb (14.5ms)
  Rendered news/index.html.erb within layouts/base (46.0ms)
Completed 200 OK in 191.3ms (Views: 143.2ms | ActiveRecord: 9.6ms)
Started GET "/projects/test-project/documents" for 127.0.0.1 at 2014-11-26 23:26:38 +0100
Processing by DocumentsController#index as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered attachments/_form.html.erb (4.6ms)
  Rendered documents/_form.html.erb (18.4ms)
  Rendered documents/index.html.erb within layouts/base (33.3ms)
Completed 200 OK in 214.6ms (Views: 120.4ms | ActiveRecord: 6.7ms)
Started GET "/projects/test-project/settings" for 127.0.0.1 at 2014-11-26 23:26:40 +0100
Processing by ProjectsController#settings as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered projects/_form.html.erb (24.5ms)
  Rendered projects/_edit.html.erb (27.7ms)
  Rendered projects/settings/_modules.html.erb (7.8ms)
  Rendered projects/settings/_members.html.erb (20.5ms)
  Rendered projects/settings/_versions.html.erb (7.4ms)
  Rendered projects/settings/_issue_categories.html.erb (3.6ms)
  Rendered projects/settings/_wiki.html.erb (4.0ms)
  Rendered projects/settings/_repositories.html.erb (3.6ms)
  Rendered projects/settings/_boards.html.erb (3.7ms)
  Rendered projects/settings/_activities.html.erb (19.3ms)
  Rendered common/_tabs.html.erb (110.5ms)
  Rendered projects/settings.html.erb within layouts/base (111.8ms)
Completed 200 OK in 174.5ms (Views: 148.8ms | ActiveRecord: 8.2ms)
Started POST "/projects/test-project/modules" for 127.0.0.1 at 2014-11-26 23:26:48 +0100
Processing by ProjectsController#modules as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "enabled_module_names"=>["issue_tracking", "time_tracking", "news", "documents", "files", "wiki", "repository", "calendar", "gantt"], "commit"=>"Save", "id"=>"test-project"}
  Current user: admin (id=1)
Redirected to http://localhost:3000/projects/test-project/settings/modules
Completed 302 Found in 78.7ms (ActiveRecord: 53.9ms)
Started GET "/projects/test-project/settings/modules" for 127.0.0.1 at 2014-11-26 23:26:48 +0100
Processing by ProjectsController#settings as HTML
  Parameters: {"id"=>"test-project", "tab"=>"modules"}
  Current user: admin (id=1)
  Rendered projects/_form.html.erb (25.5ms)
  Rendered projects/_edit.html.erb (28.0ms)
  Rendered projects/settings/_modules.html.erb (7.1ms)
  Rendered projects/settings/_members.html.erb (20.2ms)
  Rendered projects/settings/_versions.html.erb (6.5ms)
  Rendered projects/settings/_issue_categories.html.erb (3.2ms)
  Rendered projects/settings/_wiki.html.erb (4.4ms)
  Rendered projects/settings/_repositories.html.erb (3.7ms)
  Rendered projects/settings/_activities.html.erb (19.1ms)
  Rendered common/_tabs.html.erb (105.2ms)
  Rendered projects/settings.html.erb within layouts/base (106.3ms)
Completed 200 OK in 170.8ms (Views: 143.7ms | ActiveRecord: 10.3ms)
Started POST "/projects/test-project/modules" for 127.0.0.1 at 2014-11-26 23:26:54 +0100
Processing by ProjectsController#modules as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "enabled_module_names"=>["issue_tracking", "time_tracking", "news", "documents", "files", "wiki", "repository", "calendar"], "commit"=>"Save", "id"=>"test-project"}
  Current user: admin (id=1)
Redirected to http://localhost:3000/projects/test-project/settings/modules
Completed 302 Found in 144.0ms (ActiveRecord: 121.6ms)
Started GET "/projects/test-project/settings/modules" for 127.0.0.1 at 2014-11-26 23:26:54 +0100
Processing by ProjectsController#settings as HTML
  Parameters: {"id"=>"test-project", "tab"=>"modules"}
  Current user: admin (id=1)
  Rendered projects/_form.html.erb (25.8ms)
  Rendered projects/_edit.html.erb (28.6ms)
  Rendered projects/settings/_modules.html.erb (7.1ms)
  Rendered projects/settings/_members.html.erb (19.0ms)
  Rendered projects/settings/_versions.html.erb (7.6ms)
  Rendered projects/settings/_issue_categories.html.erb (3.8ms)
  Rendered projects/settings/_wiki.html.erb (3.8ms)
  Rendered projects/settings/_repositories.html.erb (3.0ms)
  Rendered projects/settings/_activities.html.erb (16.2ms)
  Rendered common/_tabs.html.erb (102.8ms)
  Rendered projects/settings.html.erb within layouts/base (103.8ms)
Completed 200 OK in 165.5ms (Views: 135.7ms | ActiveRecord: 13.2ms)
Started GET "/projects/test-project/news" for 127.0.0.1 at 2014-11-26 23:26:58 +0100
Processing by NewsController#index as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered attachments/_form.html.erb (5.6ms)
  Rendered news/_form.html.erb (12.3ms)
  Rendered news/index.html.erb within layouts/base (30.9ms)
Completed 200 OK in 114.4ms (Views: 83.6ms | ActiveRecord: 6.1ms)
Started POST "/projects/test-project/news" for 127.0.0.1 at 2014-11-26 23:27:24 +0100
Processing by NewsController#create as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "news"=>{"title"=>"news here ", "summary"=>"here comes the summary", "description"=>"no details available"}, "commit"=>"Create", "project_id"=>"test-project"}
  Current user: admin (id=1)
Redirected to http://localhost:3000/projects/test-project/news
Completed 302 Found in 247.8ms (ActiveRecord: 118.5ms)
Started GET "/projects/test-project/news" for 127.0.0.1 at 2014-11-26 23:27:24 +0100
Processing by NewsController#index as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered attachments/_form.html.erb (4.6ms)
  Rendered news/_form.html.erb (11.9ms)
  Rendered news/index.html.erb within layouts/base (46.7ms)
Completed 200 OK in 145.4ms (Views: 107.5ms | ActiveRecord: 10.1ms)
Started GET "/projects/test-project/news" for 127.0.0.1 at 2014-11-26 23:27:27 +0100
Processing by NewsController#index as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered attachments/_form.html.erb (5.5ms)
  Rendered news/_form.html.erb (12.2ms)
  Rendered news/index.html.erb within layouts/base (41.0ms)
Completed 200 OK in 125.9ms (Views: 86.9ms | ActiveRecord: 4.7ms)
Started GET "/projects/test-project" for 127.0.0.1 at 2014-11-26 23:27:39 +0100
Processing by ProjectsController#show as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered projects/_members_box.html.erb (0.1ms)
  Rendered news/_news.html.erb (8.4ms)
  Rendered projects/_sidebar.html.erb (2.3ms)
  Rendered projects/show.html.erb within layouts/base (45.6ms)
Completed 200 OK in 155.1ms (Views: 88.0ms | ActiveRecord: 11.3ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-26 23:34:32 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (9.6ms)
  Rendered admin/index.html.erb within layouts/admin (10.5ms)
  Rendered layouts/base.html.erb (20.9ms)
Completed 200 OK in 42.3ms (Views: 32.9ms | ActiveRecord: 1.8ms)
Started GET "/my/account" for 127.0.0.1 at 2014-11-26 23:34:51 +0100
Processing by MyController#account as HTML
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (13.9ms)
  Rendered users/_preferences.html.erb (13.3ms)
  Rendered my/_sidebar.html.erb (10.7ms)
  Rendered my/account.html.erb within layouts/base (53.6ms)
Completed 200 OK in 80.1ms (Views: 68.5ms | ActiveRecord: 3.1ms)
Started GET "/" for 127.0.0.1 at 2014-11-26 23:34:59 +0100
Processing by WelcomeController#index as HTML
  Current user: admin (id=1)
  Rendered news/_news.html.erb (7.4ms)
  Rendered welcome/index.html.erb within layouts/base (17.6ms)
Completed 200 OK in 66.3ms (Views: 45.0ms | ActiveRecord: 3.6ms)
Started GET "/my/page" for 127.0.0.1 at 2014-11-26 23:35:02 +0100
Processing by MyController#page as HTML
  Current user: admin (id=1)
  Rendered issues/_list_simple.html.erb (4.2ms)
  Rendered my/blocks/_issuesassignedtome.html.erb (58.2ms)
  Rendered issues/_list_simple.html.erb (0.2ms)
  Rendered my/blocks/_issuesreportedbyme.html.erb (16.5ms)
  Rendered my/page.html.erb within layouts/base (115.1ms)
Completed 200 OK in 172.4ms (Views: 149.9ms | ActiveRecord: 10.1ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-26 23:35:05 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (12.7ms)
  Rendered admin/index.html.erb within layouts/admin (13.7ms)
  Rendered layouts/base.html.erb (21.1ms)
Completed 200 OK in 46.3ms (Views: 36.1ms | ActiveRecord: 1.6ms)
sh: 1: svn: not found
sh: 1: darcs: not found
sh: 1: hg: not found
sh: 1: cvs: not found
sh: 1: bzr: not found
Started GET "/settings" for 127.0.0.1 at 2014-11-26 23:35:09 +0100
Processing by SettingsController#index as HTML
  Current user: admin (id=1)
  Rendered settings/_general.html.erb (34.9ms)
  Rendered settings/_display.html.erb (28.5ms)
  Rendered settings/_authentication.html.erb (20.4ms)
  Rendered settings/_projects.html.erb (21.3ms)
  Rendered queries/_columns.html.erb (10.3ms)
  Rendered settings/_issues.html.erb (30.6ms)
  Rendered settings/_notifications.html.erb (39.9ms)
  Rendered settings/_mail_handler.html.erb (16.2ms)
  Rendered settings/_repositories.html.erb (199.5ms)
  Rendered common/_tabs.html.erb (429.8ms)
  Rendered settings/edit.html.erb within layouts/admin (432.0ms)
  Rendered admin/_menu.html.erb (9.6ms)
  Rendered layouts/base.html.erb (23.2ms)
Completed 200 OK in 537.2ms (Views: 479.3ms | ActiveRecord: 23.8ms)
Started GET "/settings?tab=authentication" for 127.0.0.1 at 2014-11-26 23:36:27 +0100
Processing by SettingsController#index as HTML
  Parameters: {"tab"=>"authentication"}
  Current user: admin (id=1)
  Rendered settings/_general.html.erb (13.3ms)
  Rendered settings/_display.html.erb (15.3ms)
  Rendered settings/_authentication.html.erb (11.3ms)
  Rendered settings/_projects.html.erb (17.7ms)
  Rendered queries/_columns.html.erb (9.3ms)
  Rendered settings/_issues.html.erb (21.0ms)
  Rendered settings/_notifications.html.erb (0.3ms)
  Rendered settings/_mail_handler.html.erb (4.5ms)
  Rendered settings/_repositories.html.erb (25.3ms)
  Rendered common/_tabs.html.erb (121.3ms)
  Rendered settings/edit.html.erb within layouts/admin (122.3ms)
  Rendered admin/_menu.html.erb (11.0ms)
  Rendered layouts/base.html.erb (23.4ms)
Completed 200 OK in 172.3ms (Views: 157.2ms | ActiveRecord: 4.8ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-26 23:36:34 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (11.4ms)
  Rendered admin/index.html.erb within layouts/admin (12.5ms)
  Rendered layouts/base.html.erb (21.8ms)
Completed 200 OK in 45.5ms (Views: 35.7ms | ActiveRecord: 1.5ms)
Started GET "/settings" for 127.0.0.1 at 2014-11-26 23:36:37 +0100
Processing by SettingsController#index as HTML
  Current user: admin (id=1)
  Rendered settings/_general.html.erb (13.0ms)
  Rendered settings/_display.html.erb (15.3ms)
  Rendered settings/_authentication.html.erb (13.5ms)
  Rendered settings/_projects.html.erb (16.4ms)
  Rendered queries/_columns.html.erb (9.7ms)
  Rendered settings/_issues.html.erb (21.0ms)
  Rendered settings/_notifications.html.erb (0.3ms)
  Rendered settings/_mail_handler.html.erb (4.9ms)
  Rendered settings/_repositories.html.erb (25.9ms)
  Rendered common/_tabs.html.erb (124.1ms)
  Rendered settings/edit.html.erb within layouts/admin (125.1ms)
  Rendered admin/_menu.html.erb (10.9ms)
  Rendered layouts/base.html.erb (24.6ms)
Completed 200 OK in 173.0ms (Views: 161.0ms | ActiveRecord: 3.2ms)
Started POST "/settings/edit?tab=authentication" for 127.0.0.1 at 2014-11-26 23:36:43 +0100
Processing by SettingsController#edit as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "settings"=>{"login_required"=>"0", "autologin"=>"0", "self_registration"=>"2", "unsubscribe"=>"1", "password_min_length"=>"[FILTERED]", "lost_password"=>"[FILTERED]", "openid"=>"0", "rest_api_enabled"=>"1", "jsonp_enabled"=>"1", "session_lifetime"=>"0", "session_timeout"=>"0"}, "commit"=>"Save", "tab"=>"authentication"}
  Current user: admin (id=1)
Redirected to http://localhost:3000/settings?tab=authentication
Completed 302 Found in 463.1ms (ActiveRecord: 374.8ms)
Started GET "/settings?tab=authentication" for 127.0.0.1 at 2014-11-26 23:36:43 +0100
Processing by SettingsController#index as HTML
  Parameters: {"tab"=>"authentication"}
Settings cache cleared.
  Current user: admin (id=1)
  Rendered settings/_general.html.erb (41.9ms)
  Rendered settings/_display.html.erb (33.6ms)
  Rendered settings/_authentication.html.erb (32.1ms)
  Rendered settings/_projects.html.erb (25.1ms)
  Rendered queries/_columns.html.erb (8.9ms)
  Rendered settings/_issues.html.erb (44.0ms)
  Rendered settings/_notifications.html.erb (0.3ms)
  Rendered settings/_mail_handler.html.erb (12.3ms)
  Rendered settings/_repositories.html.erb (41.6ms)
  Rendered common/_tabs.html.erb (242.4ms)
  Rendered settings/edit.html.erb within layouts/admin (243.4ms)
  Rendered admin/_menu.html.erb (9.2ms)
  Rendered layouts/base.html.erb (22.6ms)
Completed 200 OK in 296.2ms (Views: 237.9ms | ActiveRecord: 43.8ms)
Started GET "/my/account" for 127.0.0.1 at 2014-11-26 23:37:32 +0100
Processing by MyController#account as HTML
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (16.8ms)
  Rendered users/_preferences.html.erb (12.5ms)
  Rendered my/_sidebar.html.erb (79.5ms)
  Rendered my/account.html.erb within layouts/base (125.2ms)
Completed 200 OK in 154.8ms (Views: 88.3ms | ActiveRecord: 56.9ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-26 23:37:37 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (10.7ms)
  Rendered admin/index.html.erb within layouts/admin (11.5ms)
  Rendered layouts/base.html.erb (23.6ms)
Completed 200 OK in 49.7ms (Views: 36.4ms | ActiveRecord: 1.7ms)
Started GET "/users" for 127.0.0.1 at 2014-11-26 23:37:39 +0100
Processing by UsersController#index as HTML
  Current user: admin (id=1)
  Rendered users/index.html.erb within layouts/admin (37.8ms)
  Rendered admin/_menu.html.erb (15.2ms)
  Rendered layouts/base.html.erb (23.7ms)
Completed 200 OK in 118.1ms (Views: 97.3ms | ActiveRecord: 4.2ms)
Started GET "/users/new" for 127.0.0.1 at 2014-11-26 23:37:44 +0100
Processing by UsersController#new as HTML
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (4.7ms)
  Rendered users/_preferences.html.erb (11.3ms)
  Rendered users/_form.html.erb (34.4ms)
  Rendered users/new.html.erb within layouts/admin (43.0ms)
  Rendered admin/_menu.html.erb (10.6ms)
  Rendered layouts/base.html.erb (23.1ms)
Completed 200 OK in 118.1ms (Views: 98.3ms | ActiveRecord: 5.8ms)
Started POST "/users" for 127.0.0.1 at 2014-11-26 23:38:32 +0100
Processing by UsersController#create as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "user"=>{"login"=>"tester", "firstname"=>"Daniel", "lastname"=>"Han", "mail"=>"daniel.han@tester.com", "language"=>"en", "admin"=>"1", "password"=>"[FILTERED]", "password_confirmation"=>"[FILTERED]", "generate_password"=>"[FILTERED]", "must_change_passwd"=>"0", "mail_notification"=>"only_my_events", "notified_project_ids"=>[""]}, "pref"=>{"no_self_notified"=>"0", "hide_mail"=>"0", "time_zone"=>"", "comments_sorting"=>"asc", "warn_on_leaving_unsaved"=>"1"}, "commit"=>"Create"}
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (3.5ms)
  Rendered users/_preferences.html.erb (13.3ms)
  Rendered users/_form.html.erb (42.8ms)
  Rendered users/new.html.erb within layouts/admin (46.4ms)
  Rendered admin/_menu.html.erb (11.4ms)
  Rendered layouts/base.html.erb (24.2ms)
Completed 200 OK in 129.7ms (Views: 84.2ms | ActiveRecord: 5.6ms)
Started POST "/users" for 127.0.0.1 at 2014-11-26 23:38:48 +0100
Processing by UsersController#create as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "user"=>{"login"=>"tester", "firstname"=>"Daniel", "lastname"=>"Han", "mail"=>"daniel.han@tester.com", "language"=>"en", "admin"=>"1", "password"=>"[FILTERED]", "password_confirmation"=>"[FILTERED]", "generate_password"=>"[FILTERED]", "must_change_passwd"=>"0", "mail_notification"=>"only_my_events", "notified_project_ids"=>[""]}, "pref"=>{"no_self_notified"=>"0", "hide_mail"=>"0", "time_zone"=>"", "comments_sorting"=>"asc", "warn_on_leaving_unsaved"=>"1"}, "commit"=>"Create"}
  Current user: admin (id=1)
Redirected to http://localhost:3000/users/5/edit
Completed 302 Found in 96.1ms (ActiveRecord: 54.9ms)
Started GET "/users/5/edit" for 127.0.0.1 at 2014-11-26 23:38:48 +0100
Processing by UsersController#edit as HTML
  Parameters: {"id"=>"5"}
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (15.6ms)
  Rendered users/_preferences.html.erb (11.5ms)
  Rendered users/_form.html.erb (41.4ms)
  Rendered users/_general.html.erb (46.4ms)
  Rendered users/_memberships.html.erb (18.6ms)
  Rendered common/_tabs.html.erb (71.7ms)
  Rendered users/edit.html.erb within layouts/admin (80.4ms)
  Rendered admin/_menu.html.erb (11.3ms)
  Rendered layouts/base.html.erb (22.2ms)
Completed 200 OK in 149.0ms (Views: 130.6ms | ActiveRecord: 8.6ms)
Started GET "/" for 151.177.25.37 at 2014-11-26 23:38:59 +0100
Processing by WelcomeController#index as HTML
  Current user: admin (id=1)
  Rendered news/_news.html.erb (6.3ms)
  Rendered welcome/index.html.erb within layouts/base (16.4ms)
Completed 200 OK in 56.4ms (Views: 38.5ms | ActiveRecord: 3.5ms)
Started POST "/logout" for 151.177.25.37 at 2014-11-26 23:39:05 +0100
Processing by AccountController#logout as HTML
  Parameters: {"authenticity_token"=>"gX3XNgPFenOI8HvlHRCfvfalGYbUIZ+wbjEtPgK0974="}
  Current user: admin (id=1)
Redirected to http://151.177.25.37:3000/
Completed 302 Found in 13.7ms (ActiveRecord: 1.7ms)
Started GET "/" for 151.177.25.37 at 2014-11-26 23:39:05 +0100
Processing by WelcomeController#index as HTML
  Current user: anonymous
  Rendered news/_news.html.erb (4.5ms)
  Rendered welcome/index.html.erb within layouts/base (11.3ms)
Completed 200 OK in 48.0ms (Views: 25.7ms | ActiveRecord: 3.8ms)
Started GET "/login" for 151.177.25.37 at 2014-11-26 23:39:09 +0100
Processing by AccountController#login as HTML
  Current user: anonymous
  Rendered account/login.html.erb within layouts/base (25.1ms)
Completed 200 OK in 44.3ms (Views: 39.3ms | ActiveRecord: 0.6ms)
Started POST "/login" for 151.177.25.37 at 2014-11-26 23:39:17 +0100
Processing by AccountController#login as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"31gLIOFTUdpZ82w8eaRGNCQMVWqSSSljer1AQVHBxqw=", "back_url"=>"http://151.177.25.37:3000/", "username"=>"tester", "password"=>"[FILTERED]", "login"=>"Login »"}
  Current user: anonymous
Successful authentication for 'tester' from 151.177.25.37 at 2014-11-26 22:39:17 UTC
Redirected to http://151.177.25.37:3000/
Completed 302 Found in 91.9ms (ActiveRecord: 81.8ms)
Started GET "/" for 151.177.25.37 at 2014-11-26 23:39:17 +0100
Processing by WelcomeController#index as HTML
  Current user: tester (id=5)
  Rendered news/_news.html.erb (5.5ms)
  Rendered welcome/index.html.erb within layouts/base (66.2ms)
Completed 200 OK in 103.2ms (Views: 41.9ms | ActiveRecord: 47.7ms)
Started GET "/my/account" for 151.177.25.37 at 2014-11-26 23:39:20 +0100
Processing by MyController#account as HTML
  Current user: tester (id=5)
  Rendered users/_mail_notifications.html.erb (11.7ms)
  Rendered users/_preferences.html.erb (11.7ms)
  Rendered my/_sidebar.html.erb (77.4ms)
  Rendered my/account.html.erb within layouts/base (115.0ms)
Completed 200 OK in 138.6ms (Views: 76.6ms | ActiveRecord: 55.4ms)
Started GET "/issues.json" for 127.0.0.1 at 2014-11-27 00:07:37 +0100
Processing by IssuesController#index as JSON
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (2.6ms)
Completed 200 OK in 128.6ms (Views: 5.0ms | ActiveRecord: 69.7ms)
Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:10:47 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (2.8ms)
Completed 200 OK in 99.6ms (Views: 4.8ms | ActiveRecord: 43.9ms)
Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:11:21 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (0.9ms)
Completed 200 OK in 93.6ms (Views: 1.8ms | ActiveRecord: 41.1ms)
Started GET "/issues/1.xml" for 127.0.0.1 at 2014-11-27 00:11:21 +0100
Processing by IssuesController#show as XML
  Parameters: {"id"=>"1"}
  Current user: tester (id=5)
Filter chain halted as :find_issue rendered or redirected
Completed 404 Not Found in 44.3ms (ActiveRecord: 34.4ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-27 00:11:42 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (10.7ms)
  Rendered admin/index.html.erb within layouts/admin (11.5ms)
  Rendered layouts/base.html.erb (21.8ms)
Completed 200 OK in 47.5ms (Views: 34.6ms | ActiveRecord: 1.9ms)
Started GET "/admin/projects" for 127.0.0.1 at 2014-11-27 00:11:45 +0100
Processing by AdminController#projects as HTML
  Current user: admin (id=1)
  Rendered admin/projects.html.erb within layouts/admin (16.1ms)
  Rendered admin/_menu.html.erb (14.7ms)
  Rendered layouts/base.html.erb (24.5ms)
Completed 200 OK in 76.1ms (Views: 58.5ms | ActiveRecord: 2.9ms)
Started GET "/projects/test-project/settings" for 127.0.0.1 at 2014-11-27 00:11:49 +0100
Processing by ProjectsController#settings as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered projects/_form.html.erb (29.5ms)
  Rendered projects/_edit.html.erb (32.7ms)
  Rendered projects/settings/_modules.html.erb (8.0ms)
  Rendered projects/settings/_members.html.erb (25.0ms)
  Rendered projects/settings/_versions.html.erb (8.1ms)
  Rendered projects/settings/_issue_categories.html.erb (3.7ms)
  Rendered projects/settings/_wiki.html.erb (4.2ms)
  Rendered projects/settings/_repositories.html.erb (3.1ms)
  Rendered projects/settings/_activities.html.erb (19.5ms)
  Rendered common/_tabs.html.erb (117.9ms)
  Rendered projects/settings.html.erb within layouts/base (119.1ms)
Completed 200 OK in 192.1ms (Views: 153.7ms | ActiveRecord: 12.0ms)
Started GET "/projects/test-project/issues" for 127.0.0.1 at 2014-11-27 00:11:52 +0100
Processing by IssuesController#index as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered queries/_filters.html.erb (24.5ms)
  Rendered queries/_columns.html.erb (6.2ms)
  Rendered issues/_sidebar.html.erb (10.6ms)
  Rendered issues/index.html.erb within layouts/base (68.4ms)
Completed 200 OK in 211.2ms (Views: 132.1ms | ActiveRecord: 12.5ms)
Started GET "/projects/test-project/issues/new" for 127.0.0.1 at 2014-11-27 00:12:01 +0100
Processing by IssuesController#new as HTML
  Parameters: {"project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered issues/_form_custom_fields.html.erb (6.1ms)
  Rendered issues/_attributes.html.erb (37.2ms)
  Rendered issues/_form.html.erb (64.7ms)
  Rendered attachments/_form.html.erb (6.1ms)
  Rendered issues/new.html.erb within layouts/base (77.4ms)
Completed 200 OK in 173.4ms (Views: 121.2ms | ActiveRecord: 10.4ms)
Started POST "/projects/test-project/issues" for 127.0.0.1 at 2014-11-27 00:12:34 +0100
Processing by IssuesController#create as HTML
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "issue"=>{"is_private"=>"0", "tracker_id"=>"1", "subject"=>"this is the subject of an issue", "description"=>"descr", "status_id"=>"1", "priority_id"=>"2", "assigned_to_id"=>"1", "parent_issue_id"=>"", "start_date"=>"2014-11-27", "due_date"=>"", "estimated_hours"=>"", "done_ratio"=>"0"}, "commit"=>"Create", "project_id"=>"test-project"}
  Current user: admin (id=1)
  Rendered mailer/_issue.text.erb (8.6ms)
  Rendered mailer/issue_add.text.erb within layouts/mailer (31.6ms)
  Rendered mailer/_issue.html.erb (4.8ms)
  Rendered mailer/issue_add.html.erb within layouts/mailer (8.8ms)
Redirected to http://localhost:3000/issues/1
Completed 302 Found in 579.3ms (ActiveRecord: 73.0ms)
Started GET "/issues/1" for 127.0.0.1 at 2014-11-27 00:12:34 +0100
Processing by IssuesController#show as HTML
  Parameters: {"id"=>"1"}
  Current user: admin (id=1)
  Rendered issues/_action_menu.html.erb (10.3ms)
  Rendered issue_relations/_form.html.erb (6.8ms)
  Rendered issues/_relations.html.erb (57.4ms)
  Rendered issues/_action_menu.html.erb (6.8ms)
  Rendered issues/_form_custom_fields.html.erb (0.2ms)
  Rendered issues/_attributes.html.erb (30.6ms)
  Rendered issues/_form.html.erb (60.1ms)
  Rendered attachments/_form.html.erb (5.0ms)
  Rendered issues/_edit.html.erb (92.5ms)
  Rendered issues/_sidebar.html.erb (8.2ms)
  Rendered watchers/_watchers.html.erb (11.0ms)
  Rendered issues/show.html.erb within layouts/base (273.8ms)
Completed 200 OK in 502.4ms (Views: 333.5ms | ActiveRecord: 30.5ms)
Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:12:41 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (9.4ms)
Completed 200 OK in 170.5ms (Views: 9.8ms | ActiveRecord: 52.6ms)
Started GET "/issues/1.xml" for 127.0.0.1 at 2014-11-27 00:12:41 +0100
Processing by IssuesController#show as XML
  Parameters: {"id"=>"1"}
  Current user: tester (id=5)
  Rendered issues/show.api.rsb (23.2ms)
Completed 200 OK in 117.2ms (Views: 23.1ms | ActiveRecord: 44.0ms)
Started POST "/issues.xml" for 127.0.0.1 at 2014-11-27 00:12:41 +0100

REXML::ParseException (malformed XML: missing tag start
Line: 9
Position: 248
Last 80 unconsumed characters:
<2>Fixed</2>   </custom-field-values>   <project-id type="integer">1</project-id>):
  /usr/lib/ruby/2.1.0/rexml/parsers/baseparser.rb:374:in `pull_event'
  /usr/lib/ruby/2.1.0/rexml/parsers/baseparser.rb:184:in `pull'
  /usr/lib/ruby/2.1.0/rexml/parsers/treeparser.rb:22:in `parse'
  /usr/lib/ruby/2.1.0/rexml/document.rb:287:in `build'
  /usr/lib/ruby/2.1.0/rexml/document.rb:44:in `initialize'
  activesupport (3.2.19) lib/active_support/xml_mini/rexml.rb:30:in `new'
  activesupport (3.2.19) lib/active_support/xml_mini/rexml.rb:30:in `parse'
  activesupport (3.2.19) lib/active_support/xml_mini.rb:80:in `parse'
  activesupport (3.2.19) lib/active_support/core_ext/hash/conversions.rb:98:in `from_xml'
  actionpack (3.2.19) lib/action_dispatch/middleware/params_parser.rb:41:in `parse_formatted_parameters'
  actionpack (3.2.19) lib/action_dispatch/middleware/params_parser.rb:17:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/flash.rb:242:in `call'
  rack (1.4.5) lib/rack/session/abstract/id.rb:210:in `context'
  rack (1.4.5) lib/rack/session/abstract/id.rb:205:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/cookies.rb:341:in `call'
  activerecord (3.2.19) lib/active_record/query_cache.rb:64:in `call'
  activerecord (3.2.19) lib/active_record/connection_adapters/abstract/connection_pool.rb:479:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/callbacks.rb:28:in `block in call'
  activesupport (3.2.19) lib/active_support/callbacks.rb:405:in `_run__642836408__call__280261450__callbacks'
  activesupport (3.2.19) lib/active_support/callbacks.rb:405:in `__run_callback'
  activesupport (3.2.19) lib/active_support/callbacks.rb:385:in `_run_call_callbacks'
  activesupport (3.2.19) lib/active_support/callbacks.rb:81:in `run_callbacks'
  actionpack (3.2.19) lib/action_dispatch/middleware/callbacks.rb:27:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/remote_ip.rb:31:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/debug_exceptions.rb:16:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/show_exceptions.rb:56:in `call'
  railties (3.2.19) lib/rails/rack/logger.rb:32:in `call_app'
  railties (3.2.19) lib/rails/rack/logger.rb:16:in `block in call'
  activesupport (3.2.19) lib/active_support/tagged_logging.rb:22:in `tagged'
  railties (3.2.19) lib/rails/rack/logger.rb:16:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/request_id.rb:22:in `call'
  rack (1.4.5) lib/rack/methodoverride.rb:21:in `call'
  rack (1.4.5) lib/rack/runtime.rb:17:in `call'
  activesupport (3.2.19) lib/active_support/cache/strategy/local_cache.rb:72:in `call'
  rack (1.4.5) lib/rack/lock.rb:15:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/static.rb:63:in `call'
  rack-cache (1.2) lib/rack/cache/context.rb:136:in `forward'
  rack-cache (1.2) lib/rack/cache/context.rb:143:in `pass'
  rack-cache (1.2) lib/rack/cache/context.rb:155:in `invalidate'
  rack-cache (1.2) lib/rack/cache/context.rb:71:in `call!'
  rack-cache (1.2) lib/rack/cache/context.rb:51:in `call'
  railties (3.2.19) lib/rails/engine.rb:484:in `call'
  railties (3.2.19) lib/rails/application.rb:231:in `call'
  rack (1.4.5) lib/rack/content_length.rb:14:in `call'
  railties (3.2.19) lib/rails/rack/log_tailer.rb:17:in `call'
  rack (1.4.5) lib/rack/handler/webrick.rb:59:in `service'
  /usr/lib/ruby/2.1.0/webrick/httpserver.rb:138:in `service'
  /usr/lib/ruby/2.1.0/webrick/httpserver.rb:94:in `run'
  /usr/lib/ruby/2.1.0/webrick/server.rb:295:in `block in start_thread'


Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:13:05 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (8.9ms)
Completed 200 OK in 118.1ms (Views: 9.1ms | ActiveRecord: 47.2ms)
Started GET "/issues/1.xml" for 127.0.0.1 at 2014-11-27 00:13:06 +0100
Processing by IssuesController#show as XML
  Parameters: {"id"=>"1"}
  Current user: tester (id=5)
  Rendered issues/show.api.rsb (17.6ms)
Completed 200 OK in 104.3ms (Views: 16.8ms | ActiveRecord: 38.0ms)
Started POST "/issues.xml" for 127.0.0.1 at 2014-11-27 00:13:06 +0100

REXML::ParseException (malformed XML: missing tag start
Line: 9
Position: 248
Last 80 unconsumed characters:
<2>Fixed</2>   </custom-field-values>   <project-id type="integer">1</project-id>):
  /usr/lib/ruby/2.1.0/rexml/parsers/baseparser.rb:374:in `pull_event'
  /usr/lib/ruby/2.1.0/rexml/parsers/baseparser.rb:184:in `pull'
  /usr/lib/ruby/2.1.0/rexml/parsers/treeparser.rb:22:in `parse'
  /usr/lib/ruby/2.1.0/rexml/document.rb:287:in `build'
  /usr/lib/ruby/2.1.0/rexml/document.rb:44:in `initialize'
  activesupport (3.2.19) lib/active_support/xml_mini/rexml.rb:30:in `new'
  activesupport (3.2.19) lib/active_support/xml_mini/rexml.rb:30:in `parse'
  activesupport (3.2.19) lib/active_support/xml_mini.rb:80:in `parse'
  activesupport (3.2.19) lib/active_support/core_ext/hash/conversions.rb:98:in `from_xml'
  actionpack (3.2.19) lib/action_dispatch/middleware/params_parser.rb:41:in `parse_formatted_parameters'
  actionpack (3.2.19) lib/action_dispatch/middleware/params_parser.rb:17:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/flash.rb:242:in `call'
  rack (1.4.5) lib/rack/session/abstract/id.rb:210:in `context'
  rack (1.4.5) lib/rack/session/abstract/id.rb:205:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/cookies.rb:341:in `call'
  activerecord (3.2.19) lib/active_record/query_cache.rb:64:in `call'
  activerecord (3.2.19) lib/active_record/connection_adapters/abstract/connection_pool.rb:479:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/callbacks.rb:28:in `block in call'
  activesupport (3.2.19) lib/active_support/callbacks.rb:405:in `_run__642836408__call__280261450__callbacks'
  activesupport (3.2.19) lib/active_support/callbacks.rb:405:in `__run_callback'
  activesupport (3.2.19) lib/active_support/callbacks.rb:385:in `_run_call_callbacks'
  activesupport (3.2.19) lib/active_support/callbacks.rb:81:in `run_callbacks'
  actionpack (3.2.19) lib/action_dispatch/middleware/callbacks.rb:27:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/remote_ip.rb:31:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/debug_exceptions.rb:16:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/show_exceptions.rb:56:in `call'
  railties (3.2.19) lib/rails/rack/logger.rb:32:in `call_app'
  railties (3.2.19) lib/rails/rack/logger.rb:16:in `block in call'
  activesupport (3.2.19) lib/active_support/tagged_logging.rb:22:in `tagged'
  railties (3.2.19) lib/rails/rack/logger.rb:16:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/request_id.rb:22:in `call'
  rack (1.4.5) lib/rack/methodoverride.rb:21:in `call'
  rack (1.4.5) lib/rack/runtime.rb:17:in `call'
  activesupport (3.2.19) lib/active_support/cache/strategy/local_cache.rb:72:in `call'
  rack (1.4.5) lib/rack/lock.rb:15:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/static.rb:63:in `call'
  rack-cache (1.2) lib/rack/cache/context.rb:136:in `forward'
  rack-cache (1.2) lib/rack/cache/context.rb:143:in `pass'
  rack-cache (1.2) lib/rack/cache/context.rb:155:in `invalidate'
  rack-cache (1.2) lib/rack/cache/context.rb:71:in `call!'
  rack-cache (1.2) lib/rack/cache/context.rb:51:in `call'
  railties (3.2.19) lib/rails/engine.rb:484:in `call'
  railties (3.2.19) lib/rails/application.rb:231:in `call'
  rack (1.4.5) lib/rack/content_length.rb:14:in `call'
  railties (3.2.19) lib/rails/rack/log_tailer.rb:17:in `call'
  rack (1.4.5) lib/rack/handler/webrick.rb:59:in `service'
  /usr/lib/ruby/2.1.0/webrick/httpserver.rb:138:in `service'
  /usr/lib/ruby/2.1.0/webrick/httpserver.rb:94:in `run'
  /usr/lib/ruby/2.1.0/webrick/server.rb:295:in `block in start_thread'


Started GET "/my/account" for 127.0.0.1 at 2014-11-27 00:15:29 +0100
Processing by MyController#account as HTML
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (12.6ms)
  Rendered users/_preferences.html.erb (12.2ms)
  Rendered my/_sidebar.html.erb (15.8ms)
  Rendered my/account.html.erb within layouts/base (54.3ms)
Completed 200 OK in 79.7ms (Views: 68.6ms | ActiveRecord: 4.1ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-27 00:15:45 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (9.9ms)
  Rendered admin/index.html.erb within layouts/admin (11.0ms)
  Rendered layouts/base.html.erb (21.4ms)
Completed 200 OK in 45.8ms (Views: 33.8ms | ActiveRecord: 1.6ms)
Started GET "/settings" for 127.0.0.1 at 2014-11-27 00:15:52 +0100
Processing by SettingsController#index as HTML
  Current user: admin (id=1)
  Rendered settings/_general.html.erb (14.4ms)
  Rendered settings/_display.html.erb (19.0ms)
  Rendered settings/_authentication.html.erb (11.2ms)
  Rendered settings/_projects.html.erb (17.1ms)
  Rendered queries/_columns.html.erb (8.9ms)
  Rendered settings/_issues.html.erb (19.5ms)
  Rendered settings/_notifications.html.erb (0.4ms)
  Rendered settings/_mail_handler.html.erb (4.2ms)
  Rendered settings/_repositories.html.erb (25.0ms)
  Rendered common/_tabs.html.erb (125.6ms)
  Rendered settings/edit.html.erb within layouts/admin (126.9ms)
  Rendered admin/_menu.html.erb (11.2ms)
  Rendered layouts/base.html.erb (24.5ms)
Completed 200 OK in 177.6ms (Views: 163.0ms | ActiveRecord: 3.1ms)
Started GET "/projects" for 127.0.0.1 at 2014-11-27 00:16:20 +0100
Processing by ProjectsController#index as HTML
  Current user: admin (id=1)
  Rendered projects/index.html.erb within layouts/base (22.3ms)
Completed 200 OK in 69.9ms (Views: 53.6ms | ActiveRecord: 3.3ms)
Started GET "/projects/test-project" for 127.0.0.1 at 2014-11-27 00:16:23 +0100
Processing by ProjectsController#show as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered projects/_members_box.html.erb (0.1ms)
  Rendered news/_news.html.erb (6.3ms)
  Rendered projects/_sidebar.html.erb (2.3ms)
  Rendered projects/show.html.erb within layouts/base (22.2ms)
Completed 200 OK in 120.6ms (Views: 60.2ms | ActiveRecord: 9.4ms)
Started GET "/projects/test-project/settings" for 127.0.0.1 at 2014-11-27 00:16:28 +0100
Processing by ProjectsController#settings as HTML
  Parameters: {"id"=>"test-project"}
  Current user: admin (id=1)
  Rendered projects/_form.html.erb (43.7ms)
  Rendered projects/_edit.html.erb (46.6ms)
  Rendered projects/settings/_modules.html.erb (7.3ms)
  Rendered projects/settings/_members.html.erb (23.0ms)
  Rendered projects/settings/_versions.html.erb (7.2ms)
  Rendered projects/settings/_issue_categories.html.erb (3.4ms)
  Rendered projects/settings/_wiki.html.erb (3.7ms)
  Rendered projects/settings/_repositories.html.erb (3.1ms)
  Rendered projects/settings/_activities.html.erb (19.9ms)
  Rendered common/_tabs.html.erb (126.6ms)
  Rendered projects/settings.html.erb within layouts/base (127.7ms)
Completed 200 OK in 188.1ms (Views: 158.7ms | ActiveRecord: 10.7ms)
Started GET "/admin" for 127.0.0.1 at 2014-11-27 00:17:02 +0100
Processing by AdminController#index as HTML
  Current user: admin (id=1)
  Rendered admin/_menu.html.erb (11.2ms)
  Rendered admin/index.html.erb within layouts/admin (12.1ms)
  Rendered layouts/base.html.erb (21.7ms)
Completed 200 OK in 44.4ms (Views: 35.2ms | ActiveRecord: 1.5ms)
Started GET "/users" for 127.0.0.1 at 2014-11-27 00:17:03 +0100
Processing by UsersController#index as HTML
  Current user: admin (id=1)
  Rendered users/index.html.erb within layouts/admin (26.2ms)
  Rendered admin/_menu.html.erb (10.8ms)
  Rendered layouts/base.html.erb (20.9ms)
Completed 200 OK in 77.4ms (Views: 59.4ms | ActiveRecord: 4.4ms)
Started GET "/users/5/edit" for 127.0.0.1 at 2014-11-27 00:17:11 +0100
Processing by UsersController#edit as HTML
  Parameters: {"id"=>"5"}
  Current user: admin (id=1)
  Rendered users/_mail_notifications.html.erb (14.4ms)
  Rendered users/_preferences.html.erb (11.5ms)
  Rendered users/_form.html.erb (41.2ms)
  Rendered users/_general.html.erb (43.9ms)
  Rendered users/_memberships.html.erb (9.5ms)
  Rendered common/_tabs.html.erb (56.3ms)
  Rendered users/edit.html.erb within layouts/admin (64.6ms)
  Rendered admin/_menu.html.erb (11.7ms)
  Rendered layouts/base.html.erb (21.4ms)
Completed 200 OK in 113.1ms (Views: 96.8ms | ActiveRecord: 4.8ms)
Started GET "/users/5" for 127.0.0.1 at 2014-11-27 00:17:21 +0100
Processing by UsersController#show as HTML
  Parameters: {"id"=>"5"}
  Current user: admin (id=1)
  Rendered users/show.html.erb within layouts/base (13.8ms)
Completed 200 OK in 154.6ms (Views: 66.4ms | ActiveRecord: 18.2ms)
Started POST "/users/5/memberships" for 127.0.0.1 at 2014-11-27 00:17:40 +0100
Processing by UsersController#edit_membership as JS
  Parameters: {"utf8"=>"✓", "authenticity_token"=>"7U8ZHU+8hGmRAtxmgq7Dul1KrABwof0ISskELpNEHe4=", "membership"=>{"project_id"=>"1", "role_ids"=>["3", "4", "5"]}, "commit"=>"Add", "id"=>"5"}
  Current user: admin (id=1)
  Rendered users/_memberships.html.erb (45.2ms)
  Rendered users/edit_membership.js.erb (54.3ms)
Completed 200 OK in 227.7ms (Views: 73.5ms | ActiveRecord: 55.9ms)
Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:18:07 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (8.5ms)
Completed 200 OK in 124.3ms (Views: 9.2ms | ActiveRecord: 52.9ms)
Started GET "/issues/1.xml" for 127.0.0.1 at 2014-11-27 00:18:07 +0100
Processing by IssuesController#show as XML
  Parameters: {"id"=>"1"}
  Current user: tester (id=5)
  Rendered issues/show.api.rsb (17.3ms)
Completed 200 OK in 114.2ms (Views: 16.7ms | ActiveRecord: 47.4ms)
Started POST "/issues.xml" for 127.0.0.1 at 2014-11-27 00:18:07 +0100

REXML::ParseException (malformed XML: missing tag start
Line: 9
Position: 234
Last 80 unconsumed characters:
<2>Fixed</2>   </custom-field-values>   <project-id>test-project</project-id>   <):
  /usr/lib/ruby/2.1.0/rexml/parsers/baseparser.rb:374:in `pull_event'
  /usr/lib/ruby/2.1.0/rexml/parsers/baseparser.rb:184:in `pull'
  /usr/lib/ruby/2.1.0/rexml/parsers/treeparser.rb:22:in `parse'
  /usr/lib/ruby/2.1.0/rexml/document.rb:287:in `build'
  /usr/lib/ruby/2.1.0/rexml/document.rb:44:in `initialize'
  activesupport (3.2.19) lib/active_support/xml_mini/rexml.rb:30:in `new'
  activesupport (3.2.19) lib/active_support/xml_mini/rexml.rb:30:in `parse'
  activesupport (3.2.19) lib/active_support/xml_mini.rb:80:in `parse'
  activesupport (3.2.19) lib/active_support/core_ext/hash/conversions.rb:98:in `from_xml'
  actionpack (3.2.19) lib/action_dispatch/middleware/params_parser.rb:41:in `parse_formatted_parameters'
  actionpack (3.2.19) lib/action_dispatch/middleware/params_parser.rb:17:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/flash.rb:242:in `call'
  rack (1.4.5) lib/rack/session/abstract/id.rb:210:in `context'
  rack (1.4.5) lib/rack/session/abstract/id.rb:205:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/cookies.rb:341:in `call'
  activerecord (3.2.19) lib/active_record/query_cache.rb:64:in `call'
  activerecord (3.2.19) lib/active_record/connection_adapters/abstract/connection_pool.rb:479:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/callbacks.rb:28:in `block in call'
  activesupport (3.2.19) lib/active_support/callbacks.rb:405:in `_run__642836408__call__280261450__callbacks'
  activesupport (3.2.19) lib/active_support/callbacks.rb:405:in `__run_callback'
  activesupport (3.2.19) lib/active_support/callbacks.rb:385:in `_run_call_callbacks'
  activesupport (3.2.19) lib/active_support/callbacks.rb:81:in `run_callbacks'
  actionpack (3.2.19) lib/action_dispatch/middleware/callbacks.rb:27:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/remote_ip.rb:31:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/debug_exceptions.rb:16:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/show_exceptions.rb:56:in `call'
  railties (3.2.19) lib/rails/rack/logger.rb:32:in `call_app'
  railties (3.2.19) lib/rails/rack/logger.rb:16:in `block in call'
  activesupport (3.2.19) lib/active_support/tagged_logging.rb:22:in `tagged'
  railties (3.2.19) lib/rails/rack/logger.rb:16:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/request_id.rb:22:in `call'
  rack (1.4.5) lib/rack/methodoverride.rb:21:in `call'
  rack (1.4.5) lib/rack/runtime.rb:17:in `call'
  activesupport (3.2.19) lib/active_support/cache/strategy/local_cache.rb:72:in `call'
  rack (1.4.5) lib/rack/lock.rb:15:in `call'
  actionpack (3.2.19) lib/action_dispatch/middleware/static.rb:63:in `call'
  rack-cache (1.2) lib/rack/cache/context.rb:136:in `forward'
  rack-cache (1.2) lib/rack/cache/context.rb:143:in `pass'
  rack-cache (1.2) lib/rack/cache/context.rb:155:in `invalidate'
  rack-cache (1.2) lib/rack/cache/context.rb:71:in `call!'
  rack-cache (1.2) lib/rack/cache/context.rb:51:in `call'
  railties (3.2.19) lib/rails/engine.rb:484:in `call'
  railties (3.2.19) lib/rails/application.rb:231:in `call'
  rack (1.4.5) lib/rack/content_length.rb:14:in `call'
  railties (3.2.19) lib/rails/rack/log_tailer.rb:17:in `call'
  rack (1.4.5) lib/rack/handler/webrick.rb:59:in `service'
  /usr/lib/ruby/2.1.0/webrick/httpserver.rb:138:in `service'
  /usr/lib/ruby/2.1.0/webrick/httpserver.rb:94:in `run'
  /usr/lib/ruby/2.1.0/webrick/server.rb:295:in `block in start_thread'


Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:19:15 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (8.6ms)
Completed 200 OK in 151.1ms (Views: 9.0ms | ActiveRecord: 60.9ms)
Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:19:49 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (8.4ms)
Completed 200 OK in 119.3ms (Views: 8.9ms | ActiveRecord: 49.2ms)
Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:20:07 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (8.7ms)
Completed 200 OK in 114.5ms (Views: 9.0ms | ActiveRecord: 44.6ms)
Started GET "/issues.xml" for 127.0.0.1 at 2014-11-27 00:20:24 +0100
Processing by IssuesController#index as XML
  Current user: tester (id=5)
  Rendered issues/index.api.rsb (8.6ms)
Completed 200 OK in 127.5ms (Views: 8.9ms | ActiveRecord: 57.7ms)
Started GET "/issues/1.xml" for 127.0.0.1 at 2014-11-27 00:20:25 +0100
Processing by IssuesController#show as XML
  Parameters: {"id"=>"1"}
  Current user: tester (id=5)
  Rendered issues/show.api.rsb (17.4ms)
Completed 200 OK in 113.2ms (Views: 16.5ms | ActiveRecord: 47.1ms)
Started POST "/issues.xml" for 127.0.0.1 at 2014-11-27 00:20:25 +0100
Processing by IssuesController#create as XML
  Parameters: {"issue"=>{"subject"=>"REST API"}}
  Current user: tester (id=5)
Filter chain halted as :find_project rendered or redirected
Completed 404 Not Found in 47.2ms (ActiveRecord: 39.8ms)





  893  apt-cache search ruby
  894  apt-cache search ruby | less
  895  sudo apt-get install ruby
  896  sudo apt-get update
  897  sudo apt-get install ruby
  898  ruby --version
  899  gem install mysql2
  900  sudo gem install mysql2
  901  sudo apt-get install ruby-dev
  902  sudo gem install mysql2
  903  ls
  904  ls mkmf.log
  905  vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/g
  906  vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/gem_make.out
  907  vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/mkmf.log
  908  ld
  909  vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/mkmf.log
  910  mysqlclient
  911  apt-cache search mysqlclient
  912  sudo apt-get libmysqlclient-dev libmysqlclient18
  913  sudo apt-get install libmysqlclient-dev libmysqlclient18
  914  sudo gem install mysql2
  915  cd Documents/
  916  s
  917  ks
  918  ls
  919  cd klarna/
  920  ls
  921  cd redmine-2.6.0/
  922  s
  923  ks
  924  ls
  925  sudo apt-get install mysql-server
  926  mysql -u root -p
  927  gem install bundler
  928  sudo gem install bundler
  929  bundle install --without development test
  930  vi /var/lib/gems/2.1.0/extensions/x86-linux/2.1.0/mysql2-0.3.17/mkmf.log
  931  vi /tmp/bundler20141126-10420-iqpl66/rmagick-2.13.4/extensions/x86-linux/2.1.0/rmagick-2.13.4/gem_make.out
  932  gem install rmagick -v '2.13.4'
  933  apt-cache search ImageMagick
  934  sudo apt-get install libmagick++-dev
  935  bundle install --without development test
  936  apt-cache search ImageMagick
  937  sudo apt-get install imagemagick
  938  bundle install --without development test
  939  rake generate_secret_token
  940  rake -T
  941  RAILS_ENV=production rake db:migrate
  942  bundle install --without development test
  943  RAILS_ENV=production rake db:migrate
  944  RAILS_ENV=production rake redmine:load_default_data
  945  ls
  946  ls tmp/
  947  ls public/
  948  ls files/
  949  mkdir -p tmp tmp/pdf public/plugin_assets
  950  sudo chown -R redmine:redmine files log tmp public/plugin_assets
  951  sudo chmod -R 755 files log tmp public/plugin_assets
  952  ruby script/rails server webrick -e production
  953  history
```

```
        from /Users/yecine/.rvm/gems/ruby-1.9.2-p290@global/gems/activeresource-3.1.2/lib/active_resource/base.rb:902:in `find_every'
        from /Users/yecine/.rvm/gems/ruby-1.9.2-p290@global/gems/activeresource-3.1.2/lib/active_resource/base.rb:814:in `find'
        from /Users/yecine/Documents/github/redmine_lighthouse_sync/redmine_project_sync.rb:14:in `<main>'
```

    Change to xml format and it's working ...

```
    class Issue < ActiveResource::Base
      self.site = 'http://redmine.server/'
      self.user = 'admin'
      self.password = 'test'
      self.format = :xml
    end
```
