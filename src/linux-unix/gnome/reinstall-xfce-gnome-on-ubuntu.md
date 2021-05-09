# Reinstall Xfce/GNOME on Ubuntu


1. Replace XFCE with GNOME
```
sudo apt-get --purge remove a2ps abiword abiword-common abiword-plugin-grammar abiword-plugin-mathview browser-plugin-parole catfish elementary-icon-theme exo-utils gigolo gimp gimp-data gmusicbrowser gnome-time-admin gnumeric gnumeric-common gnumeric-doc gtk2-engines-xfce gvfs-bin libabiword-2.8 libaiksaurus-1.2-0c2a libaiksaurus-1.2-data libaiksaurusgtk-1.2-0c2a libao-common libao4 libasyncns0 libaudio-scrobbler-perl libbabl-0.0-0 libclutter-1.0-0 libclutter-1.0-common libclutter-gtk-0.10-0 libconfig-inifiles-perl libexo-1-0 libexo-common libgarcon-1-0 libgarcon-common libgdome2-0 libgdome2-cpp-smart0c2a libgegl-0.0-0 libgimp2.0 libgoffice-0.8-8 libgoffice-0.8-8-common libgsf-1-114 libgsf-1-common libgstreamer-perl libgtk2-notify-perl libgtk2-trayicon-perl libgtkmathview0c2a libid3tag0 libilmbase6 libjpeg-progs libjpeg8 libkeybinder0 liblink-grammar4 libloudmouth1-0 libmad0 libmng1 libopenexr6 libotr2 libots0 libsexy2 libtagc0 libthunarx-2-0 libtumbler-1-0 libwv-1.2-3 libxfce4ui-1-0 libxfce4util-bin libxfce4util-common libxfce4util4 libxfcegui4-4 libxfconf-0-2 link-grammar-dictionaries-en mousepad mpg321 murrine-themes orage parole pidgin pidgin-data pidgin-libnotify pidgin-otr plymouth-theme-xubuntu-logo plymouth-theme-xubuntu-text psutils quadrapassel ristretto tango-icon-theme tango-icon-theme-common thunar thunar-archive-plugin thunar-data thunar-media-tags-plugin thunar-volman thunderbird thunderbird-globalmenu ttf-droid ttf-lyx tumbler tumbler-common wdiff xchat xchat-common xfburn xfce-keyboard-shortcuts xfce4-appfinder xfce4-cpugraph-plugin xfce4-dict xfce4-fsguard-plugin xfce4-indicator-plugin xfce4-mailwatch-plugin xfce4-mixer xfce4-mount-plugin xfce4-netload-plugin xfce4-notes xfce4-notes-plugin xfce4-notifyd xfce4-panel xfce4-power-manager xfce4-power-manager-data xfce4-quicklauncher-plugin xfce4-screenshooter xfce4-session xfce4-settings xfce4-smartbookmark-plugin xfce4-systemload-plugin xfce4-taskmanager xfce4-terminal xfce4-utils xfce4-verve-plugin xfce4-volumed xfce4-weather-plugin xfconf xfdesktop4 xfdesktop4-data xfprint4 xfwm4 xfwm4-themes xscreensaver xubuntu-artwork xubuntu-default-settings xubuntu-desktop xubuntu-docs xubuntu-gdm-theme xubuntu-icon-theme xubuntu-wallpapers && sudo apt-get install ubuntu-desktop
```
Use --purge to delete all configuration files.

2. Replace GNOME with Xfce:
```
sudo apt-get install _xubuntu-desktop_
```
<http://www.xubuntu.org/getubuntu>

<http://www.psychocats.net/ubuntu/puregnome>

<http://www.idealog.us/2007/09/how-to-uninstal.html>
