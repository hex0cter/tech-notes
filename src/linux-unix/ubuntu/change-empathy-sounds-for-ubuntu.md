
date: None  
author(s): None  

# [Change Empathy sounds for Ubuntu - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/ubuntu/change-empathy-sounds-for-ubuntu)

The empathy sound that is played when you receive a new message is contained in this file:  
/usr/share/sounds/ubuntu/stereo/message-new-instant.ogg

which is in the ubuntu-sounds package. To see all the sounds in this file you can type, in a terminal, 

  
dpkg -L ubuntu-sounds

  
I found the message-new-instant.ogg to be much to 'quiet' to be useful, especially since it often blends in with background music. Personally I like the 'drip' sound better, so I changed the the message-new-instant.ogg to /usr/share/sounds/gnome/default/alerts/drip.ogg by issuing the following command in a terminal:

  
sudo cp /usr/share/sounds/gnome/default/alerts/drip.ogg /usr/share/sounds/ubuntu/stereo/message-new-instant.ogg

*NOTE*

This is not the "right" way to do things, since you are overwriting /usr/share/sounds/ubuntu/stereo/message-new-instant.ogg irreversibly. ... but I couldn't find the proper way (changing the setting with gconf-editor) and I'm sure I never want to change the sound back. If you're want to change it back, either back-up the sound first, or reinstall the ubuntu-sounds package.

<http://ubuntuforums.org/archive/index.php/t-1288559.html>  
  
---

