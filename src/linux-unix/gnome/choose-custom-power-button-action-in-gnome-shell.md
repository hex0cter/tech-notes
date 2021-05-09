# [Choose custom power button action in Gnome Shell](http://askubuntu.com/questions/66723/how-do-i-set-the-power-button-to-shutdown-instantly-instead-of-opening-a-dialog)

Install dconf-tools:
```
sudo apt-get install dconf-tools
```
Press alt+f2 and open dconf-editor (or in a terminal type dconf-editor)

Navigate to `org.gnome.settings-daemon.plugins.power` and set your default button-power action there:

<img src="http://i.stack.imgur.com/OMZL1.png">

Double click the button-power item to make it bold. Now it should work.
