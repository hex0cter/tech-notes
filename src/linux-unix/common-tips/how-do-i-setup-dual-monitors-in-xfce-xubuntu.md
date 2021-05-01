# [How do I setup dual monitors in XFCE/Xubuntu?](http://askubuntu.com/questions/62681/how-do-i-setup-dual-monitors-in-xfce)

First, open up monitor config - it's in `Start > Settings > Settings Manger`, then open the `Display`item.

Make sure both your displays are on.![enter image description here](http://i.stack.imgur.com/ayCTI.png)

Then, open a terminal and run this:

`xrandr`

The output will look something like this:

`Screen 0: minimum 320 x 200, current 2464 x 900, maximum 4096 x 4096 LVDS1 connected 1024x600+1440+0 (normal left inverted right x axis y axis) 220mm x 129mm 1024x600 60.0*+ 65.0800x600 60.3 56.2640x480 59.9VGA1 connected 1440x900+0+0 (normal left inverted right x axis y axis) 408mm x 255mm 1440x900 59.9*+ 75.01280x1024 75.0 60.01280x960 60.01280x800 74.9 59.81152x864 75.01024x768 75.1 70.1 60.0832x624 74.6800x600 72.2 75.0 60.3 56.2640x480 72.8 75.0 66.7 60.0

720x400 70.1

`

Then, run the following, changing `VGA1` and `LVDS1` to match the appropriate display:

`xrandr --output VGA1 --left-of LVDS1`

Note that you can move change `--left-of` to `--right-of`.

Now, it should work, but you've still got one problem.

It will disappear after you logout. So, you need to add it to your login items.

Head over to `Start > Settings > Settings Manger`, then open "Session and Startup", add the above command to your login items, and you're good to go!
