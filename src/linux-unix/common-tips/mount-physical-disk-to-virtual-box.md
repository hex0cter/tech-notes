# Mount physical disk to virtual box

Connect the disk onto the host, assuming /dev/sdb, run the following command:

```
sudo VBoxManage internalcommands createrawvmdk -filename /home/daniel/VMs/Raw/sdb.vmdk -rawdisk /dev/sdb
```

create a vm with that file attached as the disk. Install it.
