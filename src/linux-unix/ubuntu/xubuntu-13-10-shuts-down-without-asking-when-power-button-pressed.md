# [Xubuntu 13.10 shuts down without asking when power button pressed](http://askubuntu.com/questions/363399/xubuntu-13-10-shuts-down-without-asking-when-power-button-pressed)


edit `/etc/systemd/logind.conf` to make `HandlePowerKey=ignore`

Then you can change in the power manager in setting manager.
