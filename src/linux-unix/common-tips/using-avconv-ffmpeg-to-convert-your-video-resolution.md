# [Using avconv/ffmpeg to convert your video resolution](http://en.linuxreviews.org/HOWTO_Convert_video_files)

Here is a example for Samsung Android:

```
avconv -i Sugar.mov -s vga -strict experimental -b:a 64k -b:v 800k out-1.mp4
avconv -i Sugar.mov -s wvga -strict experimental -b:a 64k -b:v 1200k out-2.mp4
```

More online description:

<http://en.linuxreviews.org/HOWTO_Convert_video_files>
