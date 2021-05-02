# [Send-only Mail Server with Exim on Ubuntu](http://library.linode.com/email/exim/send-only-mta-ubuntu-10.04-lucid)

Many Linux server applications need to send email; cron jobs use mail services to deliver reports on jobs that have run, web applications require mail support for user registration functions, and other applications may need to send alerts via SMTP. This guide will help you install and configure the lightweight Exim MTA (Mail Transfer Agent) on your Ubuntu 10.04 LTS (Lucid) Linux VPS.

You'll gain the ability to send mail from `localhost` through either a traditional "sendmail" style interface, or via port 25 locally. As this guide is not intended to provide a full send/receive mail solution, please refer to our other [email guides](http://library.linode.com/email/) for ways to implement such configurations.

We assume that you've already followed the steps outlined in our [getting started](http://library.linode.com/getting-started/) guide. If you're just getting acquainted with Linux systems, we also encourage you to review our [using Linux](http://library.linode.com/using-linux/) guides. Make sure you're logged into your Linode as "root" via SSH before proceeding.

## Set the Hostname

Before you begin installing and configuring the components described in this guide, please make sure you've followed our instructions for [setting your hostname](http://library.linode.com/getting-started#sph_set-the-hostname). Issue the following commands to make sure it is set properly:

```
    hostname
    hostname -f
```

##  Install Required Packages

Make sure you have the "universe" repositories enabled. Your `/etc/apt/sources.list` file should resemble this:

 **File:** _/etc/apt/sources.list_

```
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
```

Issue the following commands to update your package repositories, upgrade your system, and install Exim:

```
    apt-get update
    apt-get upgrade
    apt-get install exim4-daemon-light mailutils
```
## Configure Exim for Local Mail Service

Issue the following command to start Exim configuration:

```
    dpkg-reconfigure exim4-config
```

You'll be presented with a welcome screen, followed by a screen asking what type mail delivery you'd like to support. Choose the option for "internet site" and select "Ok" to continue.

## Test Your Mail Configuration

Issue the following command to send a test email, substituting an external email address for `someone@somedomain.com`.

```
    echo "This is a test." | mail -s Testing someone@somedomain.com
```

Congratulations! You've configured Exim to send email from your Linux VPS.
