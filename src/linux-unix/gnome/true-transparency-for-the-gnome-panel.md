# [TRUE TRANSPARENCY FOR THE GNOME PANEL](http://www.webupd8.org/2009/12/true-transparency-for-gnome-panel.html)

You can set the Gnome panel transparency through it's settings but:

1. That's not true transparency.

2. If a panel has a background, you cannot make it transparent. Well, actually you can with a special image as it's background but it doesn't work with all the themes, as we've seen in Web Upd8 post about some really [nice Gnome panel backgrounds](http://www.webupd8.org/2009/11/gnome-panel-backgrounds.html).

But you can set the Gnome panel transparency with the help of Compiz, and that will solve all the above issues. Here is how:

(I'm not going to cover the installation of CCSM and so on, see [Ubuntu Newbie Guide: Compiz, How to Get the Cube, etc. ](http://www.webupd8.org/2009/03/compiz-how-to-get-cube-and-mac-like.html))

1. Go to System > Preferences > CompizConfig Settings Manager, and check the "Opacity, brightness and saturation" plug-in under "Accessibility", then click it so we can configure the plug-in.

2. On the "Opacity" tab, under "Specific Window settings", click on "New" and paste this:

```
(class=Gnome-panel) & !(type=Menu | PopupMenu | Dialog | DropdownMenu)
```

And drag the opacity slider to a value you want. I've set mine to 50%:


[![compiz opacity plugin settings](http://www.netupd8.com/w8img/2iudsnc.jpg)](http://www.netupd8.com/w8img/2iudsnc.jpg)

The value we've entered into the Specific Window settings means Compiz will only make the Gnome panel transparent, without also setting the menu to be transparent. If you also want to make the menu transparent, instead of the line above, enter this in the Specific Window settings:

```
class=Gnome-panel
```

You can also alter the brightness and saturation for the gnome panel, repeating this step for the "Brightness" and "Saturation" tabs in the "Opacity, brightness and saturation" Compiz plugin.
