# [Raspberry Pi/Raspbian Processing Autostart](https://aib42.net/article/raspi-autostart)

This is a short article to help you run your Processing sketches automatically when your Raspberry Pi boots up in graphics mode. It is aimed at people with a preliminary understanding of Linux/command line basics.

### Command to run your sketch

First, we must come up with a single command that will run your sketch. I opened the "explode" example sketch and saved it as "explode" in my sketchbook:


    ls /home/aib/sketchbook/explode
    data/  explode.pde

We will be using the 'processing-java' executable to run this sketch from the command line. I extracted my Processing right inside Downloads, and it's still where it's at:


    ls /home/aib/Downloads/processing-3.0.2
    core/  java/  lib/  modes/  processing*  processing-java*  revisions.txt  tools/

Putting the two paths together, our command to run the sketch will be:


    /home/aib/Downloads/processing-3.0.2/processing-java --sketch=/home/aib/sketchbook/explode --present

### Desktop entry for the command

Let's create a desktop entry to run this. Desktop entry (`.desktop`) files are really simple. While their full specification can be found at [1](https://aib42.net/article/raspi-autostart#fn1), we will be using a 4-liner. Save the following file in your Desktop (`~/Desktop`) directory with any name that ends with `.desktop`: (e.g. `MySketch.desktop`)


    [Desktop Entry]
    Type=Application
    Name=My Sketch
    Exec=/home/aib/Downloads/processing-3.0.2/processing-java --sketch=/home/aib/sketchbook/explode --present

The file should appear on your desktop, named "My Sketch". Double-clicking it should run your sketch. Verify this.

### Autostart for the desktop entry

If you've come this far, autostart is going to be really easy. The full specification is at [2](https://aib42.net/article/raspi-autostart#fn2). In order to get our desktop entry to autostart, we simply put it in `~/.config/autostart/`:


    mkdir /home/aib/.config/autostart
    cp /home/aib/Desktop/MySketch.desktop /home/aib/.config/autostart/

Note that this copies the file to your `~/.config/autostart/` directory. You can delete the original on your desktop, or use `mv` (move) instead of `cp` (copy) to begin with.

### Advanced

If you don't mind having the desktop entry on your desktop for, say, testing purposes, you can create the autostart entry as a symlink (symbolic link) instead of a hard copy. This way, the autostart file will simply point to the desktop file, and you won't have multiple copies to deal with.


    ln -s /home/aib/Desktop/MySketch.desktop /home/aib/.config/autostart/MySketch.desktop

(If the autostart file exists, you need to delete it with `rm` or add the `-f` option to `ln`)

### Exported sketches

If you export your Processing sketch, a small shell script will be created that will run it for you. Let's check:


    ls /home/aib/sketchbook/explode/application.linux-armv6hf
    data/  explode*  lib/  source/

The script should be the only command you need to run:


    /home/aib/sketchbook/explode/application.linux-armv6hf/explode

Therefore, we can use it in our desktop entry file:


    [Desktop Entry]
    Type=Application
    Name=My Sketch
    Exec=/home/aib/sketchbook/explode/application.linux-armv6hf/explode

### Technical Notes

I would have expected Processing to require the current working directory to be set to the sketch folder (and thus a corresponding `Path=` entry in the desktop file to be necessary) but that doesn't seem to be the case; all the Processing file functions seem to work relative to the sketch folder and ignore the CWD.
