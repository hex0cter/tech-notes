# [Send gmail from command line](http://www.webupd8.org/2009/11/use-gmail-to-send-emails-from-terminal.html)


1. Install ssmtp. For Ubuntu, open a terminal and paste the following command:

```
sudo apt-get install ssmtp
```

2. Edit the ssmtp config file. Press Alt + F2 and type:

```
gksu gedit /etc/ssmtp/ssmtp.conf
```

If you don't use Gedit, replace it with your favourite text editor (kate, etc).And paste this inside the ssmtp.conf file:

```
root= YOUR_EMAIL@gmail.com
mailhub=smtp.gmail.com:465
rewriteDomain=gmail.com
AuthUser=YOUR_GMAIL_USERNAME # (without @gmail.com)
AuthPass=YOUR_GMAIL_PASSWORD
FromLineOverride=YES
UseTLS=YES
```

And replace everything in capital letters with your credentials.

3. I use Ubuntu Karmic Koala and this step wasn't necessary, but it might be for you. So, make sure you don't have sendmail installed. Again, for Ubuntu, paste this:

```
sudo service sendmail stop
sudo apt-get remove sendmail
```
And create a symbolic link for ssmtp to replace sendmail:

```
sudo ln -s /usr/sbin/ssmtp /usr/sbin/sendmail
```

You don't need do that on default Ubuntu DreamPlug. You have to install mailutils: `apt-get install mailutils`

4. That's about it. There are multiple ways you can now send an email. Open a terminal and:

a)

```
echo "email content" | mail -s "email subject" email_address_to_send_email_to@somedomain.com
```

The above line is pretty much self explainatory so replace the text between the quotes with your email body and subject and do the same for email_address_to_send_email_to@somedomain.com \- replace it with the email address you want to send the email to.

b)

```
ssmtp email_address_to_send_email_to@somedomain.com
```
Then enter the following lines in the terminal (pressing ENTER after each line):

```
To: email_address_to_send_email_to@somedomain.com
From: your_email@gmail.com
Subject: this is your email subject

And here you can write the content of the email
```

And to send the email, press: CTRL + DThis time I won't explain what to replace, I hope you got the idea. Please note that you must follow the exact format as above, with an empty line between the email subject and the content of the email.


c)You can also send emails from a text file. Use the following command:

```
ssmtp email_address_to_send_email_to@somedomain.com < message.txt
```

Where message.txt must follow the exact same format like on point b) (above).

This has a lot of things it can be used for. You can [set a cron job](http://www.webupd8.org/2009/05/schedule-tasks-in-gnome-linux-using.html) to email you different things at a given time, etc. I'm sure you can think of something you could use this for.


<http://www.webupd8.org/2009/11/use-gmail-to-send-emails-from-terminal.html>
<http://www.xit.sk/web/index.php/home-automation/my-dream-plug/95-send-mail-using-gmail-from-shell>
