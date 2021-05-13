# Capture network traffic of another device from PC

If both the PC and other devices are connected to a dumb hub, it should be fairly easy.

With tcpdump,
```
sudo tcpdump -nn -i eth1 -s 65535
```
With wireshark, BEFORE starting the capture, set filter on the option dialog as:
```
host 10.177......
```

<http://www.wireshark.org/docs/wsug_html_chunked/AppToolstcpdump.html>

<http://wiki.wireshark.org/CaptureFilters>

<http://jcifs.samba.org/capture.html>
