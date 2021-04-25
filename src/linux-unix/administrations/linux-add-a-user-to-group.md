
date: None  
author(s): None  

# [Linux: Add a User To Group - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/linux-add-a-user-to-group)

<http://www.cyberciti.biz/faq/ubuntu-add-user-to-group/>

How do I add a user to group under Ubuntu Linux operating system using command line options?

You need to use the following commands:

[a] **useradd command** \- Create a new user or update default new user information or add a new user to secondary group.

[b] **usermod command** \- Modifies the system account and make changes to existing user accounts.

## First, login as the root user

You must login as the root user. You can switch to the root user by typing ' **su -** ' and entering the root password, when prompted. However, sudo command is recommend under Ubuntu Linux for switching to root user:
    
    
    su -

OR
    
    
    sudo -s

OR
    
    
    sudo useradd ...

## Ubuntu Linux: add a new user to secondary group

Use the following syntax:
    
    
     
    useradd -G Group-name Username
    passwd Username
     

Create a group called foo and add user tom to a secondary group called foo:  
`$ sudo groupadd foo  
$ sudo useradd -G foo tom` OR

`# groupadd foo  
# useradd -G foo tom`

  
Verify new settings:
    
    
     
    id tom
    groups tom
     

Finally, [set the password](http://www.cyberciti.biz/faq/linux-set-change-password-how-to/) for tom user, enter:  
`$ sudo passwd tom` OR

`# passwd tom`

You can add user tom to multiple groups - foo, bar, and ftp, enter:

`# useradd -G foo,bar,ftp tom`

## Ubuntu Linux: add a new user to primary group

To add a user called tom to a group called www use the following command:
    
    
    useradd -g www tom
    id tom
    groups tom
     

## Ubuntu Linux: add a existing user to existing group

To add an existing user jerry to ftp supplementary/secondary group with usermod command using -a option ~ i.e. add the user to the supplemental group(s). Use only with -G option:
    
    
     
    usermod -a -G ftp jerry
    id jerry
     

To change existing jerry's primary group to www, enter:
    
    
     
    usermod -g www jerry
     

For more information and options read the following man pages:  
`[man 8 useradd](http://www.manpager.com/linux/man8/useradd.8.html)  
[man 8 usemod](http://www.manpager.com/linux/man8/usermod.8.html)`  
  
---

