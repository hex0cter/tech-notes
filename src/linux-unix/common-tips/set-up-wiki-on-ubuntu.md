
date: None  
author(s): None  

# [Set up Wiki on Ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/set-up-wiki-on-ubuntu)

MediaWiki is the engine that is used for Wikipedia. See [MediaWiki](http://www.mediawiki.org/) for more information. 

## Install pre-requisites

The easiest method is to first install a full LAMP (Linux, Apache2, MySQL, PHP) server: 
    
    
     sudo tasksel install lamp-server

Make sure you record your MySQL root superuser name and superuser password that you will create at installation. You will need it later. 

(Each of the components (Apache2, MySQL5, and PHP) can also be installed individually, if you wish.) 

## Install MediaWiki

Install the package: 
    
    
     sudo apt-get install mediawiki

Optionally install add-ons: 
    
    
     sudo apt-get install imagemagick mediawiki-math php5-gd

Enable MediaWiki by editing the following file and remove the '#' from the third line so that it reads 'Alias /mediawiki /var/lib/mediawiki': 
    
    
    sudo nano /etc/mediawiki/apache.conf

Then restart apache: 
    
    
     sudo /etc/init.d/apache2 restart

### Start your MediaWiki

<http://localhost/mediawiki>

Follow the setup instructions. 

### Start Mediawiki from a remote location

This method regards starting your website from a remote location. Since you will be entering passwords, you don't want to make an unsecured connection. Either set up a ssl server] ( see [forum/server/apache2/SSL](https://help.ubuntu.com/community/forum/server/apache2/SSL)) and connect with <https://yoursite.example.com/mediawiki>, or visit from the server itself (using [elinks](https://help.ubuntu.com/community/elinks) or lynx, two excellent text-based web browsers): 
    
    
     elinks localhost/mediawiki

You could also use ssh to port forward your http traffic from your local machine to the remote server. ssh -C -L 9999:localhost:80 [regularuser@www.skippybob.com](mailto:regularuser@www.skippybob.com), edit your /etc/hosts to point the webserver's name to your localhost, then open a web browser to the config page: <http://wiki.skippybob.com:9999/config>. More detailed instructions [here.](http://technonick.livejournal.com/96173.html)

fill out the forms, noting that the final form is NOT your root or user password, but the password for the root mysql account (blank by default) 

Lastly, move the config files as requested to prevent anyone else from changing these settings: 

**NOTE:** Check the output in your web browser: if its instructions differ from below, follow them. 
    
    
     sudo cp /var/lib/mediawiki/config/LocalSettings.php /etc/mediawiki/LocalSettings.php
     sudo chown www-data /etc/mediawiki/LocalSettings.php
     sudo chmod 600 /etc/mediawiki/LocalSettings.php
     sudo rm -Rf /var/lib/mediawiki/config

You are done! you should see a wiki page at: <http://yoursite.example.com/mediawiki>

## Customize

You might want to customize the look of your wiki. 

To change the icon make a 135x135 pixel logo in PNG format and move it to the right place: 
    
    
     sudo cp my_new_logo.png /var/lib/mediawiki/skins/common/images/my_new_logo.png

Avoid to use the same name as the original logo (wiki.png), it will be overwritten when upgrading Mediawiki. 

Insert the path to the image at the end of configuration file in _/etc/mediawiki/LocalSettings.php_ like so: 
    
    
     $wgLogo = "/mediawiki/skins/common/images/my_new_logo.png" ;

To get rid of the default sunburst logo in the background, edit /var/lib/mediawiki/skins/monobook/main.css and change: 

  * background: #f9f9f9 url(headbg.jpg) 0 0 no-repeat; 



to 

## Email Support

MediaWiki can be configured to send email messages for various functions. You will need to install some additional packages: 
    
    
    sudo apt-get install php-pear
    sudo pear install mail
    sudo pear install Net_SMTP

Also, you'll need to configure the `LocalSettings.php` file to use your SMTP server to send out the messages, for example: 
    
    
    $wgEnableEmail      = true;
    $wgEnableUserEmail  = true;
    $wgEmergencyContact = "wikidude@mydomain.com";
    $wgPasswordSender = "wikidude@mydomain.com";
    $wgNoReplyAddress = "noreply@mydomain.com";
    $wgPasswordSender = "password_reminder@mydomain.com";
    
    $wgSMTP = array(
     'host'     => "ssl://smtp.gmail.com",
     'IDhost'   => "gmail.com",
     'port'     => 465,
     'auth'     => true,
     'username' => "user_name@mydomain.com",
     'password' => "user_password"
    );

## Extensions

Mediawiki extensions are stored as symbolic links in the /etc/mediawiki-extensions/extensions-available folder. You can enable an extension using 
    
    
    sudo mwenext <extension.php>

Tab/autocomplete shows a list of extensions. 

Similarly use mwdisext to disable an extension. 

## MediaWiki TurnKey appliance

Some users may prefer an unofficial pre-integrated [TurnKey MediaWiki Appliance](http://www.turnkeylinux.org/mediawiki) based on Ubuntu LTS. 

## Other Resources

  


