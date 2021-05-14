# [Access remote vino server of ubuntu from OS X screen sharing app](http://askubuntu.com/questions/463486/can-no-longer-use-screen-share-to-connect-mac-to-ubuntu-since-upgrading-to-14-04)

## Problem:

The software on the remote computer appears to be incompatible with this version of Screen Sharing.

## Solution:


Using a combination of clues from <http://discourse.ubuntu.com/t/remote-desktop-sharing-in-ubuntu-14-04/1640> (which is all about VNC access) and<https://bugs.launchpad.net/ubuntu/+source/vino/+bug/1281250> (which discusses the bug introduced into Vino) I have managed to resolve the matter.

Essentially you have to disable encryption on remote desktop access in Gnome due to a bug that has come to surface in Vino. However some threads tell you uncheck it in the wrong place. Follow these guidelines and you should be able to resolve it quickly.

Specifically it's dconf > org > gnome > desktop > remote-access > require-encription - uncheck and NOT dconf > desktop > gnome > remote-access > enabled - uncheck. Here is how you do it.

  1. First make sure Desktop Sharing is set up properly.
  2. Download gconf-tools by typing in Terminal 'sudo apt-get install dconf-tools'
  3. Run dconf-Editor
  4. Expand 'org'
  5. Expand 'gnome'
  6. Expand 'Desktop'
  7. Select 'Remote Access'
  8. Uncheck 'Require Encrption'(don't click on Set to Default as it rechecks it)
  9. Exit dconf-Editor



It should now work. Tested through a reboot and all good.

Hope it helps.

(I have got a screen shot of dconf but don't have enough points on here to post it - I am sure everyone can work it out for themselves though! :-) )

---
