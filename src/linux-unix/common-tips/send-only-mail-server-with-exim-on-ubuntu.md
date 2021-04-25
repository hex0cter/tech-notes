
date: None  
author(s): None  

# [Send-only Mail Server with Exim on Ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/send-only-mail-server-with-exim-on-ubuntu)

Many Linux server applications need to send email; cron jobs use mail services to deliver reports on jobs that have run, web applications require mail support for user registration functions, and other applications may need to send alerts via SMTP. This guide will help you install and configure the lightweight Exim MTA (Mail Transfer Agent) on your Ubuntu 10.04 LTS (Lucid) Linux VPS.

You'll gain the ability to send mail from `localhost` through either a traditional "sendmail" style interface, or via port 25 locally. As this guide is not intended to provide a full send/receive mail solution, please refer to our other [email guides](http://library.linode.com/email/) for ways to implement such configurations.

We assume that you've already followed the steps outlined in our [getting started](http://library.linode.com/getting-started/) guide. If you're just getting acquainted with Linux systems, we also encourage you to review our [using Linux](http://library.linode.com/using-linux/) guides. Make sure you're logged into your Linode as "root" via SSH before proceeding.

Before you begin installing and configuring the components described in this guide, please make sure you've followed our instructions for [setting your hostname](http://library.linode.com/getting-started#sph_set-the-hostname). Issue the following commands to make sure it is set properly:
    
    
    hostname
    hostname -f
    

Make sure you have the "universe" repositories enabled. Your `/etc/apt/sources.list` file should resemble this:

 **File:** _/etc/apt/sources.list_
    
    
    ## main & restricted repositories
    deb http://us.archive.ubuntu.com/ubuntu/ lucid main restricted
    deb-src http://us.archive.ubuntu.com/ubuntu/ lucid main restricted
    
    deb http://security.ubuntu.com/ubuntu lucid-security main restricted
    deb-src http://security.ubuntu.com/ubuntu lucid-security main restricted
    
    ## universe repositories
    deb http://us.archive.ubuntu.com/ubuntu/ lucid universe
    deb-src http://us.archive.ubuntu.com/ubuntu/ lucid universe
    deb http://us.archive.ubuntu.com/ubuntu/ lucid-updates universe
    deb-src http://us.archive.ubuntu.com/ubuntu/ lucid-updates universe
    
    deb http://security.ubuntu.com/ubuntu lucid-security universe
    deb-src http://security.ubuntu.com/ubuntu lucid-security universe
    

Issue the following commands to update your package repositories, upgrade your system, and install Exim:
    
    
    apt-get update
    apt-get upgrade
    apt-get install exim4-daemon-light mailutils
    

Issue the following command to start Exim configuration:
    
    
    dpkg-reconfigure exim4-config
    

You'll be presented with a welcome screen, followed by a screen asking what type mail delivery you'd like to support. Choose the option for "internet site" and select "Ok" to continue.

[![Exim4 mail delivery type configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/134-01-exim4-ubuntu-10.04-general.png)](http://library.linode.com/assets/134-01-exim4-ubuntu-10.04-general.png)

Enter your system's FQDN (fully qualified domain name) in the "mail name" configuration screen.

[![Exim4 system mail name configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/135-02-exim4-ubuntu-10.04-mail-name.png)](http://library.linode.com/assets/135-02-exim4-ubuntu-10.04-mail-name.png)

Enter "127.0.0.1" when asked which IP address to listen on for SMTP connections.

[![Exim4 listening IP address configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/136-03-exim4-ubuntu-10.04-ip-listen.png)](http://library.linode.com/assets/136-03-exim4-ubuntu-10.04-ip-listen.png)

Make sure you list your FQDN, hostname, and localhost entries when you're asked which destinations mail should be accepted for.

[![Exim4 mail destination configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/137-04-exim4-ubuntu-10.04-local-domains.png)](http://library.linode.com/assets/137-04-exim4-ubuntu-10.04-local-domains.png)

Leave the relay domains and relay machines fields blank.

[![Exim4 relay domains configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/138-05-exim4-ubuntu-10.04-relay-domains.png)](http://library.linode.com/assets/138-05-exim4-ubuntu-10.04-relay-domains.png)

Select "No" when asked whether to keep DNS queries to a minimum.

[![Exim4 DNS queries configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/140-07-exim4-ubuntu-10.04-dns-queries.png)](http://library.linode.com/assets/140-07-exim4-ubuntu-10.04-dns-queries.png)

You may select either "mbox" or "Maildir" when asked about the delivery method used for incoming mail. While many utilities use mbox format, Maildir format can make handling individual locally delivered mail messages easier, and is widely supporting by a range of applications.

[![Exim4 mail format configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/141-08-exim4-ubuntu-10.04-mail-format.png)](http://library.linode.com/assets/141-08-exim4-ubuntu-10.04-mail-format.png)

Accept the default "non-split" option for your mail configuration file. Enter at least one external email address (choose one that you check frequently) in addition to "root" when asked to specify postmaster mail recipients.

[![Exim4 postmaster recipient configuration on Ubuntu 10.04 LTS \(Lucid\).](http://library.linode.com/assets/142-10-exim4-ubuntu-10.04-postmater-mail.png)](http://library.linode.com/assets/142-10-exim4-ubuntu-10.04-postmater-mail.png)

Issue the following command to send a test email, substituting an external email address for `someone@somedomain.com`.
    
    
    echo "This is a test." | mail -s Testing someone@somedomain.com
    

Congratulations! You've configured Exim to send email from your Linux VPS.

