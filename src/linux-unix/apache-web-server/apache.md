# [How to install apache on Linux](http://laffers.net/howtos/howto-install-apache)

_This tutorial explains the installation of Apache web server, bundled with PHP and MySQL server on a Linux machine. The tutorial is primarily for SuSE 9.2, 9.3, 10.0 & 10.1, but most of the steps ought to be valid for all Linux-like operating systems._

## apache 2 installation

### prerequisites

Before you begin, it is highly recommended (though not inevitable) to create a system user and user group under which your Apache server will be running.

```
# groupadd www
# useradd -g www apache2 `
```

What is it good for? All actions performed by Apache (for instance your PHP scripts execution) will be restricted by this user's privileges. Thus you can explicitly rule which directories your PHP scripts may read or change. Also all files created by Apache (e.g. as a result of executing your PHP scripts) will be owned by this user (apache2 in my case), and affiliated with this user group (www in my case).

### download source

Get the source from [http://httpd.apache.org/download.cgi](http://httpd.apache.org/download.cgi) ( httpd-2.2.4.tar.gz ). These instructions are known to work with all 2.x.x Apache versions.

### unpack, configure, compile

Go to the directory with the downloaded file and enter:

```
# tar -xzf httpd-2.2.4.tar.gz # cd httpd-2.2.4
# ./configure --prefix=/usr/local/apache2 --enable-so --with-included-apr
```

The configure options deserve a little bit more of detail here. The most important `--prefix` option specifies the location where Apache is to be installed. Another commonly used option `--enable-so` turns on the DSO support, i.e. available modules compiled as shared objects can be loaded or unloaded at runtime. Very handy.

To compile some modules statically (they are always loaded, faster execution times), use `--enable- _module_` option. To compile a module as a shared object, use ` --enable- _module_ =shared` option.

For all available configuration options and their default values check the [Apache documentation](http://httpd.apache.org/docs-2.2/programs/configure.html#configurationoptions) or type `./configure --help`.

#### SSL support

To support secure connections, you need to specify `--enable-ssl` option when you run ./configure. In addition to that, you will also have to [configure your httpd.conf](http://laffers.net/howtos/howto-install-apache#edit_httpd_conf_for_ssl) file later.

_Note: Make sure that openssl is installed on your system before you run`./configure` with ` --enable-ssl`. If not, download the latest version from [http://www.openssl.org/source/](http://www.openssl.org/source/) , unpack, configure, make, make install. You will also need to [generate server certificate](http://www.google.com/search?hl=en&q=howto+generate+ssl+certificate&btnG=Google+Search). Place server.crt and server.key into /etc/ssl/apache2/ directory and make them readable by Apache2. _

#### configuration example

For example, to compile the [mod_rewrite](http://httpd.apache.org/docs-2.0/mod/mod_rewrite.html) module statically and [mod_auth_digest](http://httpd.apache.org/docs-2.0/mod/mod_auth_digest.html) as a DSO, and to enable secure connections, enter:

`# ./configure --prefix=/usr/local/apache2 --enable-so --enable-rewrite --enable-auth-digest=shared --enable-ssl`

_Tip: If you are upgrading from older Apache version, you may want to copy config.nice from the directory to which the previous version was unpacked (if available) to where you unpacked the new Apache tarball file. Run `./config.nice` instead of_ _./configure. This way all the previously used configure options will be applied to the new installation effortlessly._

Once you configured everything as you like, compile and install the software:

```
# make
# make install
```
### edit httpd.conf

Before you start Apache server, edit the httpd.conf file according to your needs (the file is generously commented).

`# vi /usr/local/apache2/conf/httpd.conf`

I suggest the following changes (some of them may have already been set automatically) at the appropriate places inside httpd.conf (ignore "`...`"):

```
ServerRoot "/usr/local/apache2"
...
<IfModule !mpm_netware.c>
 User apache2
 Group www
</IfModule>
...
DocumentRoot "/foo/path_to_your_www_documents_root"
...
<Directory />
 Options FollowSymLinks
 AllowOverride None
</Directory>
...
DirectoryIndex index.php index.html index.htm index.html.var
```

"apache2" and "www" are the user and user group I have previously created (see [Prerequisites](http://laffers.net/howtos/howto-install-apache#prerequisites))

Apart from these, later you will probably want to specify [detailed options for specific directories](http://httpd.apache.org/docs-2.0/mod/core.html#directory), [load some DSO modules](http://httpd.apache.org/docs-2.0/mod/mod_so.html#loadmodule), [setup virtual servers](http://httpd.apache.org/docs-2.0/vhosts/) etc.

#### SSL support

If you wish to enable SSL for secure connections (assuming that you have configured Apache with `--enable-ssl` option - [see above](http://laffers.net/howtos/howto-install-apache#unpack_configure_compile)), add the following in the appropriate sections inside httpd.conf (ignore "`...`"; replace "`laffers.net`" with your own, and set the actual path to your server certificate and key file):

```
Listen 80
Listen 443
...
<VirtualHost *:443>
 ServerName laffers.net:443
 SSLEngine on
 SSLCertificateFile /etc/ssl/apache2/server.crt
 SSLCertificateKeyFile /etc/ssl/apache2/server.key
 ErrorLog /usr/local/apache2/logs/error_log_laffers.net
 TransferLog /usr/local/apache2/logs/access_log_laffers.net
 SSLCipherSuite ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP:+eNULL
 SetEnvIf User-Agent ".*MSIE.*" \
 nokeepalive ssl-unclean-shutdown \
 downgrade-1.0 force-response-1.0
</VirtualHost>
```

Note: In some newer distributions, httpd.conf is dissected into many additional files located in conf/extra. In that case, you may want to do the SSL settings from above inside the conf/extra/httpd-ssl.conf file. Don't forget to uncomment "`Include conf/extra/httpd-ssl.conf`" in the httpd.conf file.

After you installed PHP ([next part of this tutorial](http://laffers.net/howtos/howto-install-php)), [few additional changes](http://laffers.net/howtos/howto-install-php#edit_httpd_conf) need to be done to httpd.conf (but they are usually made automatically during PHP installation).

### setup access privileges

Don't forget to setup Apache access privileges to your www directories:

```
# chown -R apache2:www _/foo/path_to_your_www_documents_root_
# chmod -R 750 _/foo/path_to_your_www_documents_root_
```

"apache2" and "www" are the user and user group I have previously created (see [Prerequisites](http://laffers.net/howtos/howto-install-apache#prerequisites))

### start and stop apache server

After everything is set up, start Apache:

`# /usr/local/apache2/bin/apachectl start`

Similarly, if you wish to stop Apache, type:

`# /usr/local/apache2/bin/apachectl stop`

### automatic startup

It's a good idea to let your Apache server start automatically after each system reboot. To setup Apache automatic startup, do:

```
# cp /usr/local/apache2/bin/apachectl /etc/init.d
# chmod 755 /etc/init.d/apachectl
# chkconfig --add apachectl
# chkconfig --level 35 apachectl on
```
