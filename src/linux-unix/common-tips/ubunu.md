# [Ubuntu tips](http://ubuntuforums.org/archive/index.php/t-316655.html)

## Configure the Max, Min, Close icon on windows bar:**
<http://www.howtogeek.com/howto/ubuntu/put-closemaximizeminimize-buttons-on-the-left-in-ubuntu/>

## Install realplayer:**

<http://crunchbang.org/wiki/realplayer-on-ubuntu/>

## start scim automatically** :
```
sudo touch /etc/X11/Xsession.d/74custom-scim_startup
sudo chmod 646 /etc/X11/Xsession.d/74custom-scim_startup
echo 'export XMODIFIERS="@im=SCIM"' >> /etc/X11/Xsession.d/74custom-scim_startup
echo 'export GTK_IM_MODULE="scim"' >> /etc/X11/Xsession.d/74custom-scim_startup
echo 'export XIM_PROGRAM="scim -d"' >> /etc/X11/Xsession.d/74custom-scim_startup
echo 'export QT_IM_MODULE="scim"' >> /etc/X11/Xsession.d/74custom-scim_startup
sudo chmod 644 /etc/X11/Xsession.d/74custom-scim_startup
```
