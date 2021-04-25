# How to measure CPU temperature on Ubuntu

1. `sudo apt-get install lm-sensors`

2. `sensors-detect`

To load everything that is needed, add this to /etc/modules:

```
# chip drivers
coretemp
```

3. `sudo modprobe coretemp`

4. `sensors`

---
