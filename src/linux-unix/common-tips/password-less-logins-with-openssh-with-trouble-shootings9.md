
date: Fri 3 Jun 2005 at 09:45
author(s): [Steve](https://www.debian-administration.org/users/Steve)

# [Password-less logins with OpenSSH (with trouble shootings)](https://www.debian-administration.org/article/152/Password-less_logins_with_OpenSSH)

Tags: [public key authentication](https://www.debian-administration.org/tag/public%20key%20authentication), [ssh](https://www.debian-administration.org/tag/ssh)

Because OpenSSH allows you to run commands on remote systems, showing you the results directly, as well as just logging in to systems it's ideal for automating common tasks with shellscripts and cronjobs. One thing that you probably won't want is to do though is store the remote system's password in the script. Instead you'll want to setup SSH so that you can login securely without having to give a password.

Thankfully this is very straightforward, with the use of public keys.

To enable the remote login you create a pair of keys, one of which you simply append to a file upon the remote system. When this is done you'll then be able to login without being prompted for a password - and this also includes any [cronjobs](http://www.debian-administration.org/articles/56) you have setup to run.

If you don't already have a keypair generated you'll first of all need to create one.

If you do have a keypair handy already you can keep using that, by default the keys will be stored in one of the following pair of files:

  * `~/.ssh/identity` and `~/.ssh/identity.pub`
    * (This is an older DSA key).
  * `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`
    * (This is a newer RSA key).



If you have neither of the two files then you should generate one. The DSA-style keys are older ones, and should probably be ignored in favour of the newer RSA keytypes (unless you're looking at connecting to an outdated installation of OpenSSH). We'll use the RSA keytype in the following example.

To generate a new keypair you run the following command:


    skx@lappy:~$ ssh-keygen -t rsa


This will prompt you for a location to save the keys, and a pass-phrase:


    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/skx/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/skx/.ssh/id_rsa.
    Your public key has been saved in /home/skx/.ssh/id_rsa.pub.


If you accept the defaults you'll have a pair of files created, as shown above, with no passphrase. This means that the key files can be used as they are, without being "unlocked" with a password first. If you're wishing to automate things this is what you want.

Now that you have a pair of keyfiles generated, or pre-existing, you need to append the contents of the `.pub` file to the correct location on the remote server.

Assuming that you wish to login to the machine called `mystery` from your current host with the `id_rsa` and `id_rsa.pub` files you've just generated you should run the following command:


    ssh-copy-id -i ~/.ssh/id_rsa.pub username@mystery


This will prompt you for the login password for the host, then copy the keyfile for you, creating the correct directory and fixing the permissions as necessary.

The contents of the keyfile will be appended to the file `~/.ssh/authorized_keys2` for RSA keys, and `~/.ssh/authorised_keys` for the older DSA key types.

Once this has been done you should be able to login remotely, and run commands, without being prompted for a password:


    skx@lappy:~$ ssh mystery uptime
     09:52:50 up 96 days, 13:45,  0 users,  load average: 0.00, 0.00, 0.00


**What if it doesn't work?**

> There are three common problems when setting up passwordless logins:
>
>   * The remote SSH server hasn't been setup to allow public key authentication.
>   * File permissions cause problems.
>   * Your keytype isn't supported.
>

>
> Each of these problems is easily fixable, although the first will require you have root privileges upon the remote host.
>
> If the remote server doesn't allow public key based logins you will need to updated the SSH configuration. To do this edit the file `/etc/sshd/sshd_config` with your favourite text editor.
>
> You will need to uncomment, or add, the following two lines:
>
>
>     RSAAuthentication yes
>     PubkeyAuthentication yes
>
>
> Once that's been done you can restart the SSH server - don't worry this won't kill existing sessions:
>
>
>     /etc/init.d/ssh restart
>
>
> File permission problems should be simple to fix. Upon the remote machine your `.ssh` file must **not** be writable to any other user - for obvious reasons. (If it's writable to another user they could add their own keys to it, and login to your account without your password!).
>
> If this is your problem you will see a message similar to the following upon the remote machine, in the file `/var/log/auth`:
>
>
>     Jun  3 10:23:57 localhost sshd[18461]: Authentication refused:
>      bad ownership or modes for directory /home/skx/.ssh
>
>
> To fix this error you need to login to the machine (with your password!) and run the following command:
>
>
>     cd
>     chmod 700 .ssh
>
>
> Finally if you're logging into an older system which has an older version of OpenSSH installed upon it which you cannot immediately upgrade you might discover that RSA files are not supported.
>
> In this case use a DSA key instead - by generating one:
>
>
>     ssh-keygen
>
>
> Then appending it to the file `~/.ssh/authorized_keys` on the remote machine - or using the `ssh-copy-id` command we showed earlier.
>
>  **Note** if you've got a system running an older version of OpenSSH you should upgrade it unless you have a very good reason not to. There are known security issues in several older releases. Even if the machine isn't connected to the public internet, and it's only available "internally" you should fix it.
>
> Instead of using `authorized_keys`/`authorized_keys2` you could also achieve a very similar effect with the use of the `ssh-agent` command, although this isn't so friendly for scripting commands.
>
> This program allows you to type in the passphrase for any of your private keys when you login, then keep all the keys in memory, so you don't have password-less keys upon your disk and still gain the benefits of reduced password usage.
>
> If you're interested read the documentation by running:
>
>
>     man ssh-agent
>
