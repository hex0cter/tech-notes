# [How to remove the passphrase for the SSH key without having to create a new key?](http://stackoverflow.com/questions/112396/how-do-i-remove-the-passphrase-for-the-ssh-key-without-having-to-create-a-new-ke)

**Backup your old .ssh/id_rsa before you do this!**

```
# Syntax: ssh-keygen -p [-P old_passphrase] [-N new_passphrase] [-f keyfile]
ssh-keygen -p -P old_passphrase
```
