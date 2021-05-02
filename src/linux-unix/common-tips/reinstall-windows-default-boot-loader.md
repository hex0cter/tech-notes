# Reinstall windows default boot loader

Boot from Windows 7 installation CD:

Click **Repair your computer** > click **Troubleshoot** > click **Advanced options** > choose **Command Prompt**

```
bootrec /fixmbr
bootrec /fixboot
```
