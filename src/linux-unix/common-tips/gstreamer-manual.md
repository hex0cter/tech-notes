# [Gstreamer manual](http://www.360doc.com/content/11/0526/17/474846_119581954.shtml)

gstreamer很牛逼，让多媒体应用程序的开发变的更加简单，但是，也正是由于gstreamer对很多细节的隐藏，使得我们很容易把多媒体编程想得过于简单。

关于gst-launch的使用，这里不做教学，初次接触者可以自行google。

然后，请准备一个摄像头，下面我举的例子，都会用到。

先罗列出一堆例子--

gst-launch-0.10 v4l2src ! ximagesink

gst-launch-0.10 v4l2src ! xvimagesink

gst-launch-0.10 v4l2src ! ffmpegcolorspace ! ximagesink

gst-launch-0.10 v4l2src ! ffmpegcolorspace ! xvimagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-rgb' ! ximagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! ximagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-rgb' ! xvimagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! xvimagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! ffmpegcolorspace ! ximagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! ffmpegcolorspace ! xvimagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YV12' ! xvimagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YUY2' ! xvimagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YV12' ! ffmpegcolorspace ! xvimagesink

gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YUY2' ! ffmpegcolorspace ! xvimagesink

然后我提出一个问题---上面这些例子，哪些可以正确执行，哪些不可以？不可以的原因是什么？

如果你能够回答我提出的问题，那说明你对视频这一部分已经很清楚了。如果答不出来的话，则可以继续往下看看。

先简要介绍一下三个重要的gstreamer插件--v4l2src，ximagesink，xvimagesink

(1)v4l2src是使用v4l2接口的视频源插件，v4l2本身不仅仅是支持视频采集功能，它还支持其他的视频功能，但是v4l2src插件，

只是用来做视频采集的。关于视频采集，有一点必须要明确，视频采集是有多种格式的，从大方向上区分的话，至少要分为rgb

格式和yuv格式。

(2)ximagesink是用来显示视频图像的sink插件，它是基于X11库的，(简单点说ximagesink会调用XPutImage函数)，XPutImage不

支持yuv格式的数据，常用的就是rgb格式。

(3)xvimagesink也是用来显示视频图像的sink插件，但是它是基于X Video Extension库的，(简单点说xvimagesink会调用

XvPutImage函数)，而XvPutImage则可能支持yuv格式的数据，这个显卡有关。

看到这里，其实就可以回答我前面提出的问题了，“不能正常执行的原因就是各个插件使用的数据格式没有匹配上”。

现在我们再一个一个的看前面使用的那些例子:

(1)gst-launch-0.10 v4l2src ! ximagesink

我的摄像头只支持yuv格式的数据，而ximagesink需要rgb数据，所以在我的电脑上，这个命令是不成功的。

一般情况下，我们使用的usb接口的摄像头，都是不支持rgb格式的数据的，所以换做其他的摄像头，这个命令也不容易成功。

(2)gst-launch-0.10 v4l2src ! xvimagesink

换做其他的摄像头，这个命令也几乎是百分之百的会成功的，因为xvimagesink支持的格式还是比较多的。

(3)gst-launch-0.10 v4l2src ! ffmpegcolorspace ! ximagesink

(4)gst-launch-0.10 v4l2src ! ffmpegcolorspace ! xvimagesink

这两个命令肯定是会成功的，因为我们使用了ffmpegcolorspace插件，这个插件就是用来做颜色空间转换的。

但是后者的执行效率会比前者高，因为xvimagesink使用了硬件加速。

接着往下看，此时可能又会产生疑惑了，'video/x-raw-rgb'这种写法是什么意思，这个其实相当于是GstCapsFilter插件，

这是个格式过滤插件，其实就是对pipeline中的数据流的格式做一个限制。

如果不限制格式，则整个pipeline中的各个插件会自动的协商出一个最合适的数据格式。

(5)gst-launch-0.10 v4l2src ! 'video/x-raw-rgb' ! ximagesink

我的摄像头不成功，因为摄像头不支持rgb格式，所以v4l2src 和 'video/x-raw-rgb'的协商会失败。

(6)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! ximagesink

不管用什么摄像头，这个肯定都不会成功，因为'video/x-raw-yuv'和ximagesink协商不会成功。

(7)gst-launch-0.10 v4l2src ! 'video/x-raw-rgb' ! xvimagesink

我的摄像头不成功，因为摄像头不支持rgb格式，所以v4l2src 和 'video/x-raw-rgb'的协商会失败。

(8)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! xvimagesink

我的摄像头是成功的，换做其他的，一般也都会成功。

(9)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! ffmpegcolorspace ! ximagesink

(10)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv' ! ffmpegcolorspace ! xvimagesink

这两个通常也都是会成功的，因为使用了ffmpegcolorspace

但是，事实可能还是要比你想象的更复杂。

前面说过，视频采集是有多种格式的，从大方向上区分的话，至少要分为rgb格式和yuv格式。

注意，这只是大方向。具体到yuv格式，yuv只是对颜色空间的一种描述，还需要细化到具体的存储格式，也就是具体

的视频数据在内存中的存储形式，这就复杂了，一两句话很难说清楚。

针对前面的例子，只需要知道--'video/x-raw-yuv,format=(fourcc)YV12'和'video/x-raw-yuv,format=(fourcc)YUY2'是

两种不同的yuv封装格式。

(11)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YV12' ! xvimagesink

(12)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YUY2' ! xvimagesink

这两个就不一定能成功了，要看摄像头是否支持我们限定的格式。

(13)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YV12' ! ffmpegcolorspace ! xvimagesink

(14)gst-launch-0.10 v4l2src ! 'video/x-raw-yuv,format=(fourcc)YUY2' ! ffmpegcolorspace ! xvimagesink

最后这两个，虽然使用了ffmpegcolorspace，但是还是要看摄像头是否支持我们限定的格式。

这篇文章只是用来进一步理解gstreamer的，仅仅是一个入门。很多技术细节，都没有进一步描述讨论。

最后我再把这几个可以进一步了解的关键的技术点列出来，有兴趣的朋友可以自行google学习。

关键技术点：V4L2，YUV，RGB，X11，XVideo

<http://www.360doc.com/content/11/0526/17/474846_119581954.shtml>
