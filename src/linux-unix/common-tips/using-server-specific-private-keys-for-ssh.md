# [Using server specific private keys for ssh](http://nagpals.com/posts/using-different-ssh-keys-for-different-servers/)


```
Host yourappname.unfuddle.com
User username
IdentityFile /home/localusername/.ssh/yourcustomname_id_rsa
```
