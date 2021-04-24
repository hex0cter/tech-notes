
# [Edit the Settings database](http://android.stackexchange.com/questions/53720/disable-window-animations-when-the-menu-option-is-missing)


```bash
daniel@daniel-IdeaPad-Lnx:~$ ssh root@10.10.10.2

SSHDroid

Use 'root' as username

root@android:/data/data/berserker.android.apps.sshdroid/home # mount | grep system

/dev/block/mmcblk0p16 /system ext4 ro,relatime,user_xattr,acl,barrier=1,data=ordered 0 0

root@android:/data/data/berserker.android.apps.sshdroid/home # mount -o remount,rw /dev/block/mmcblk0p16 /system

# sqlite3 /data/data/com.android.providers.settings/databases/settings.db

sqlite> update system set value=0 where name='window_animation_scale';

sqlite> update system set value=0 where name='transition_animation_scale';

sqlite> .exit

root@android:/data/data/berserker.android.apps.sshdroid/home # ^D

Connection to 10.10.10.2 closed.

```
