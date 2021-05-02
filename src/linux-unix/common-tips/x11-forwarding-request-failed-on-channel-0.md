# X11 forwarding request failed on channel 0

```
debug2: x11_get_proto: /usr/bin/xauth list :0 2>/dev/null
debug1: Requesting X11 forwarding with authentication spoofing.
debug2: channel 0: request x11-req confirm 1
debug2: fd 3 setting TCP_NODELAY
debug2: client_session2_setup: id 0
debug2: channel 0: request pty-req confirm 1
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
debug2: channel 0: request env confirm 0
debug2: channel 0: request shell confirm 1
debug2: callback done
debug2: channel 0: open confirm rwindow 0 rmax 32768
debug2: channel_input_status_confirm: type 100 id 0
X11 forwarding request failed on channel 0
adding "X11UseLocalhost no" to /etc/ssh/sshd_config
```
