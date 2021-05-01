# [How to disable lightdm?](http://askubuntu.com/questions/139014/how-to-disable-lightdm)


Lightdm is starter by Upstart, not SysV Init, so update-rc.d doesn't work.

Use
```
echo  "manual" | sudo tee -a /etc/init/lightdm.override
```
