
date: None  
author(s): None  

# [Linux Users - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/administrations/linux-users)

Every user who has access to a Linux system needs a login and a password. Each user must belong to a primary group and for security or access purposes can belong to several secondary groups.

In order to create new logins, modify or delete users, you must already be logged in as **root**. The root login is the highest level and only certain individuals should have access to the root account.

useradd - Adding a new user

Options:

  *  **-d** home directory
  *  **-s** starting program (shell)
  *  **-p** password
  *  **-g** (primary group assigned to the users)
  *  **-G** (Other groups the user belongs to)
  *  **-m** (Create the user's home directory



 _Example: To add a new user with_

  * a primary group of **users**
  * a second group **mgmt**
  * starting shell **/bin/bash**
  * password of **xxxx**
  * home directory of **roger**
  * create home directory
  * a login name of **roger**



> useradd -gusers -Gmgmt -s/bin/shell -pxxxx -d/home/roger -m roger

[top of page](http://www.ahinc.com/linux101/users.htm#top)

usermod - Modifying existing user

Options:

  *  **-d** home directory
  *  **-s** starting program (shell)
  *  **-p** password
  * - **g** (primary group assigned to the users)
  *  **-G** (Other groups the user belongs to)



 _Example: To add the group 'others' to the user roger_

> usermod -Gothers roger

[top of page](http://www.ahinc.com/linux101/users.htm#top)

userdel - Deleting a user

Options:

  *  **-r** (remove home directory)



 _Example: To remove the user 'roger' and his home directory_

> userdel -r roger

[top of page](http://www.ahinc.com/linux101/users.htm#top)

passwd - User's Password

Options:

  *  **user's name** ( Only required if you are root and want to change another user's password)



 _Example: To change the password for the account you are currently logged in as..._

>  **passwd**  
>  Enter **existing password**  
>  Enter **new password**  
>  Enter **new password again** (to validate)

 _Example: To change the password for the user 'roger' (only you are logged in as root)..._

> passwd roger  
> Enter existing password (can be either roger's password or root's password)  
> Enter new password  
> Enter new password again (to validate)

[top of page](http://www.ahinc.com/linux101/users.htm#top)

Where user and group information stored

 **User names** and primary groups are stored in **/etc/passwd.** This file can be directly edited using the 'vi' editor, although this is **not recommended**.  Format of the file is...

  * User (name normally all lower case)
  * Password (encrypted - only contains the letter 'x')
  * User ID (a unique number of each user)
  * Primary Group ID
  * Comment (Normally the person's full name)
  * Home directory (normally /home/<user name>
  * Default shell (normally /bin/bash)



Each field is separated by a colon.

 **Passwords** for each user are stored in **/etc/shadow**.  This file should only be changed using the **passwd** command.

 **Group** information is stored in **/etc/group**. This file can be directly edited using the 'vi' editor. Format of the file is...

  * Group name
  * Group password (hardly ever used)
  * Group ID
  * User names (separated by commas)



Each field is separated by a colon.

 **Default files**

When a new user is created, the default files and directories that are created are stored in **/etc/skel**.

This directory can be modified to fit your needs. Modifications only effect new users and does not change anything for existing users.

[top of page](http://www.ahinc.com/linux101/users.htm#top)

su - Switch User

To switch to another user, use the **su** command. This is most commonly used to switch to the root account.

>  _Example: To switch to root account..._  
>  su  
> Enter **root's passwd**
> 
>  _Example: To switch to the user 'roger'..._  
>  su roger  
> Enter roger's or root's passwd
> 
> To return to original user, enter exit

