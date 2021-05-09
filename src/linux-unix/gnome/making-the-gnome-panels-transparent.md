# [Making the Gnome Panels Transparent](http://www.howtogeek.com/howto/43673/how-to-make-the-gnome-panels-in-ubuntu-totally-transparent/)

We all love transparency, since it makes your desktop so beautiful and lovely—so today we’re going to show you how to apply transparency to the panels in your Ubuntu Gnome setup. It’s an easy process, and here’s how to do it.

This article is the first part of a multi-part series on how to customize the Ubuntu desktop, written by How-To Geek reader and ubergeek, Omar Hafiz.


### Making the Gnome Panels Transparent

Of course we all love transparency, It makes your desktop so beautiful and lovely. So you go for enabling transparency in your panels , you right click on your panel, choose properties, go to the Background tab and make your panel transparent. Easy right? But instead of getting a lovely transparent panel, you often get a cluttered, ugly panel like this:

![Panel before fixing](http://www.howtogeek.com/wp-content/uploads/2011/02/Panel-before-fixing.png)

Fortunately it can be easily fixed, all we need to do is to edit the theme files. If your theme is one of those themes that came with Ubuntu like Ambiance then you’ll have to copy it from /usr/share/themes to your own .themes directory in your Home Folder. You can do so by typing the following command in the terminal


> cp -R /usr/share/themes/theme_name ~/.themes

 _Note:_ don’t forget to substitute theme_name with the theme name you want to fix.

But if your theme is one you downloaded then it is already in your .themes folder. Now open your file manager and navigate to your home folder then do to .themes folder. If you can’t see it then you probably have disabled the “View hidden files” option. Press Ctrl+H to enable it.

![Themes folder](http://www.howtogeek.com/wp-content/uploads/2011/02/Themes-folder.png)

Now in .themes you’ll find your previously copied theme folder there, enter it then go to gtk-2.0 folder. There you may find a file named “panel.rc”, which is a configuration file that tells your panel how it should look like. If you find it there then rename it to “panel.rc.bak”. If you don’t find don’t panic! There’s nothing wrong with your system, it’s just that your theme decided to put the panel configurations in the “gtkrc” file.

![target theme folder](http://www.howtogeek.com/wp-content/uploads/2011/02/target-theme-folder.png)

Open this file with your favorite text editor and at the end of the file there is line that looks like this “include “apps/gnome-panel.rc””. Comment out this line by putting a hash mark # in front of it. Now it should look like this “# include “apps/gnome-panel.rc””

![gtkrc file](http://www.howtogeek.com/wp-content/uploads/2011/02/gtkrc-file.png)

Save and exit the text editor. Now change your theme to any other one then switch back to the one you edited. Now your panel should look like this:

[![Panel after fixing](http://www.howtogeek.com/wp-content/uploads/2011/02/Panel-after-fixing_thumb.png)](http://www.howtogeek.com/wp-content/uploads/2011/02/Panel-after-fixing.png)

Stay tuned for the second part in the series, where we’ll cover how to change the color and fonts on your panels.

Daniel's Note: The key point is to comment out the line below:
