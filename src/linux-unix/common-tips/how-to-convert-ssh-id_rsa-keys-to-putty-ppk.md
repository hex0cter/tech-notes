# [How to convert ssh private key id_rsa to Putty .ppk](http://wazem.blogspot.se/2007/11/how-to-convert-idrsa-keys-to-putty-ppk.html)

This how to will show how to convert id_rsa keys that were already created on Linux, without a passphrase, to .ppk extension so it can be used with Putty on a Windows box.

Download PuttyGen from [here](http://the.earth.li/~sgtatham/putty/latest/x86/puttygen.exe) and open it. Once it opens click on Conversions => Import Key

Search for the id_rsa key on you computer

Click on “Save Private Key” and “Yes” to save without a passphrase.


Choose a location and a name for the new .ppk key

Now go to putty and add a path to key for the connection.
