# [How to fix “X11 forwarding request failed on channel 0″](https://joshua.hoblitt.com/rtfm/2013/04/how_to_fix_x11_forwarding_request_failed_on_channel_0/)

The fix is to add this line to your `/etc/ssh/sshd_config`:

```
X11UseLocalhost no
```
