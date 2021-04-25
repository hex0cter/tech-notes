# [How to add a user to the sudoers list](http://www.pendrivelinux.com/how-to-add-a-user-to-the-sudoers-list/)

**How to add a user to the sudoers list:**

  1. Open a Root Terminal and type **visudo** (to access and edit the list)
  2. Using the **up/down arrows** , navigate to the bottom of the sudoers file that is now displayed in the terminal
  3. Just under the line that looks like the following:

> root ALL=(ALL) ALL

  4. Add the following (replacing user with your actual username):

> user ALL=(ALL) ALL

  5. Now press **Ctrl+X** and press **Y** when promted to save

That's it, your new user now has root privileges!
