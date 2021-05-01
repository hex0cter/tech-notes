# [Apache2: How To Redirect Users To Mobile Or Normal Web Site Based On Device Using mod_rewrite](http://www.howtoforge.com/apache2-how-to-redirect-users-to-mobile-or-normal-web-site-based-on-device-using-mod_rewrite)

Version 1.0 Author: Falko Timme <ft [at] falkotimme [dot] com>

[![](http://static.howtoforge.com/images/socialmedia/twitter.png)](http://twitter.com/falko) [Follow me on Twitter](http://twitter.com/falko)


Last edited 08/24/2011

Since the massive rise of smartphones and tablets like the iPhone, iPad, Android phones and tablets, BlackBerries, etc. you might have considered creating a mobile version of your web site. This tutorial explains how to configure Apache to serve the mobile version of your web site if the visitor uses a mobile device, and the normal version if the visitor uses a normal desktop PC. This can be achieved with Apache's rewrite module.

I do not issue any guarantee that this will work for you!

### 1 Preliminary Note

In this tutorial, my "normal" web site is accessible under http://www.example.com and http://example.com, while my mobile site is calledhttp://m.example.com. These vhosts already exist on my system, so I'm not going to cover how to set them up.

### 2 Enabling mod_rewrite

First you have to make sure that the Apache module mod_rewrite is enabled. On Debian/Ubuntu, you can enable it like this:

a2enmod rewrite

Restart Apache afterwards - for Debian/Ubuntu, the command is:

/etc/init.d/apache2 restart

### 3 Configuring Apache To Allow Rewrite Rules In .htaccess Files

My "normal" web site www.example.com/example.com has the vhost configuration file /etc/apache2/sites-available/www.example.com.vhostand the document root /var/www/www.example.com/web.

My mobile site m.example.com has the vhost configuration file /etc/apache2/sites-available/m.example.com.vhost and the document root/var/www/www.example.com/mobile.

I want to place the rewrite rules for each site in an .htaccess file (although it is also possible to place the rewrite rules directly in the vhost configuration file). Therefore I must first modify our vhost configurations so that both .htaccess files are allowed to contain rewrite directives. We can do this with the lineAllowOverride All (which allows .htaccess to override all settings in the vhost configuration):

vi /etc/apache2/sites-available/www.example.com.vhost


    [...]
            <Directory /var/www/www.example.com/web/>
                    AllowOverride All
    	</Directory>
    [...]

---

vi /etc/apache2/sites-available/m.example.com.vhost


    [...]
            <Directory /var/www/www.example.com/mobile/>
                    AllowOverride All
            </Directory>
    [...]

---

Restart Apache afterwards:

/etc/init.d/apache2 restart

### 4 Creating Rewrite Rules

Now let's create the rewrite rules for the "normal" web site www.example.com/example.com that will redirect all users of mobile devices to the mobile versionm.example.com \- I focus on the relevant devices/user agents here which are Android, Blackberry, googlebot-mobile (Google's mobile search bot), IE Mobile, iPad, iPhone, iPod, Opera Mobile, PalmOS, and WebOS.

The /var/www/www.example.com/web/.htaccess file looks as follows:

vi /var/www/www.example.com/web/.htaccess


    <IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_USER_AGENT} "android|blackberry|googlebot-mobile|iemobile|ipad|iphone|ipod|opera mobile|palmos|webos" [NC]
    RewriteRule ^$ http://m.example.com/ [L,R=302]
    </IfModule>

---

For our mobile web site m.example.com, the rewrite rules that redirect all users that don't use a mobile device to our "normal" web sitewww.example.com/example.com look as follows - I've simply negated the RewriteCond condition from the previous .htaccess file:

vi /var/www/www.example.com/mobile/.htaccess


    <IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_USER_AGENT} "!(android|blackberry|googlebot-mobile|iemobile|ipad|iphone|ipod|opera mobile|palmos|webos)" [NC]
    RewriteRule ^$ http://www.example.com/ [L,R=302]
    </IfModule>

---

That's it! Now you can do some testing, e.g. visit m.example.com with a normal desktop browser:

![](http://static.howtoforge.com/images/apache_redirect_users_to_mobile_or_normal_website_based_on_device_using_mod_rewrite/1.png)

If all goes well, you should be redirected to www.example.com:

![](http://static.howtoforge.com/images/apache_redirect_users_to_mobile_or_normal_website_based_on_device_using_mod_rewrite/2.png)

Now test with a mobile device (I use an Android phone here) and go to www.example.com:

![](http://static.howtoforge.com/images/apache_redirect_users_to_mobile_or_normal_website_based_on_device_using_mod_rewrite/3.png)

You should be redirected to m.example.com:

![](http://static.howtoforge.com/images/apache_redirect_users_to_mobile_or_normal_website_based_on_device_using_mod_rewrite/4.png)

### 5 Links
* Apache: <http://httpd.apache.org/>
* Apache Module mod_rewrite: <http://httpd.apache.org/docs/current/mod/mod_rewrite.html>
