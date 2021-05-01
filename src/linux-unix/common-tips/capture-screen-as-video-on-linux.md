# capture screen as video on Linux

```
avconv -minrate 1000 -f x11grab -s 1366x768 -r 25 -i :0.0 output.mkv

ffmpeg -f x11grab -s 1024x768 -r 25 -i :0.0 -sameq output.mkv
```
