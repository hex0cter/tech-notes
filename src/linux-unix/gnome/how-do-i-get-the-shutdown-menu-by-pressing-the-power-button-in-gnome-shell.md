# [How to suspend Gnome Shell by pressing the power button](https://ask.fedoraproject.org/en/question/10325/how-do-i-get-the-shutdown-menu-by-pressing-the-power-button-in-fedora-16/)



Open `dconf-editor` from gnome, and navigate to Org-> Gnome-> Settings-daemon-> Plugins-> Power Change "button-power" to "suspend" and exit.
