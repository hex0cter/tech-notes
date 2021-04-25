# [Enabling CPU Frequency Scaling](http://embraceubuntu.com/2005/11/04/enabling-cpu-frequency-scaling/)

<http://embraceubuntu.com/2005/11/04/enabling-cpu-frequency-scaling/>

I use the CPU Frequency Scaling Monitor on my panel to see the speed of my CPU. I have a centrino laptop. Ubuntu automatically increases the speed (frequency) of my laptop when the demand is more, and manages things very well.

However, when I am plugged in, I want to run my laptop at the maximum possible frequency at certain times. It turns out that the CPU Frequency Scaling Monitor can also have the functionality to change the Frequency, by “Governing” the CPU frequency. However, by default, on my laptop, left-clicking on the Monitor in the Panel did not give me the option to change the frequency.

In order to be able to change the operating frequency, your processor should support changing it. You can find out if your processor has scaling support by seeing the contents of files in the /sys/devices/system/cpu/cpu0/cpufreq/

For example, on my system:

`$cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_frequencies`
gives:

> 1300000 1200000 1000000 800000 600000

Which means that the above frequencies (in Hz) are supported by my CPU.and…

`$cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors`


gives:

> userspace powersave ondemand conservative performance

All those are the different “modes” I can operate the CPU at. Userspace, for example, regulates the frequency according to demand. Performance runs the CPU at max-frequency, etc…

On the Ubuntu Forums, I read that one can manually change the frequency by executing commands like:$ cpufreq-selector -f 1300000

which will set the frequency to 1.3 GHz.

Now, I was interested in being able to change the power mode (between the different values listed in the “governors” above, manually by using the Cpu Frequency Panel Monitor.

I found out from the Forums, again, that changing the permissions of the cpufreq-selector binary by doing a:
$sudo chmod +s /usr/bin/cpufreq-selector

will allow me to acheive this. _However_ , I was curious as to why Ubuntu does not, by default, allow me to choose the frequency using the CPU Frequency Panel Monitor, and what the “right” or “correct” way of enabling this is.

With a little bit of detective work, I found the reason why things are the way they are in [Bug #17604](http://bugzilla.ubuntu.com/show_bug.cgi?id=17604) :

> Oh, please, not another setuid root application if we can avoid it. Which file does cpufreq-selector need access to to change the CPU speed? And why should a normal user be able to change the CPU speed in the first place? The automatic CPU speed works well enough for the majority of users, and control freaks can always use sudo to manually set the speed, or deliberately shoot themselves in the foot by making the binary suid root (as explained in README.Debian).

Anyways, since I really want to “shoot my self in the foot” using my CPU ![;\)](http://s1.wp.com/wp-includes/images/smilies/icon_wink.gif?m=1293711309g) , so I read the readme:
$cat /usr/share/doc/gnome-applets-data/README.Debian

and as suggested in it, I did a$ sudo dpkg-reconfigure gnome-applets

and answered “Yes” to the question regarding setting the suid of the cpufreq-selector executable. Now, by left-clicking on the CPU Frequency Monitor Applet, I can choose the frequency for my processor, and things couldn’t be better!!

P.S.: A lot of my detective work could have been avoided had I read the README in the first place. Stupid me.
