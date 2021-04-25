
date: None  
author(s): None  

# [capture screen as video on Linux - Daniel Han's Technical Notes](https://sites.google.com/site/xiangyangsite/home/technical-tips/linux-unix/common-tips/capture-screen-as-video-on-linux)

avconv -minrate 1000 -f x11grab -s 1366x768 -r 25 -i :0.0 output.mkv

ffmpeg -f x11grab -s 1024x768 -r 25 -i :0.0 -sameq output.mkv  
  
---

