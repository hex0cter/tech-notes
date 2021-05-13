# [capture network traffic using wireshark without sudo](http://ihacklog.com/linux/run-whireshark-as-non-root.html)

```
sudo apt-get install wireshark
sudo apt-get install pcaputils
sudo dpkg-reconfigure wireshark-common
sudo groupadd wireshark
sudo usermod -a -G wireshark daniel
newgrp wireshark
wireshark &
```
