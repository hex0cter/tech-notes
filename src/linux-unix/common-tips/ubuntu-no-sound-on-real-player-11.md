# [Ubuntu: No sound on Real Player 11](http://ubuntuforums.org/showthread.php?t=954664)

This may not work as expected but worth a try. I saw this solution from [_fwelland_](http://forums.fedoraforum.org/showthread.php?t=186200&page=3) on the Fedora forums.

I fix/hacked this by changing the line in the realplay script

```
    sudo gedit /opt/real/RealPlayer/realplay
```

then on line 52 change

```
    $HELIX_LIBS/realplay.bin "$@"
```
TO

```
    padsp -n RealPlayer -m RealPlayerStream $HELIX_LIBS/realplay.bin "$@"
```
