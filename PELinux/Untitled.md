


Try setting SUID on the passwd binary.

- Whenever SUID bit is set on a binary, it implies that it will be executed as the owner of the binary.

- Same but to allow it to a group SGID bit is used.

- Sticky bit (Check it again)

Special bits -> 7 

SUID - 4
SGID - 2 
Sticky bit - 1

Using relative paths in binaries lead to command injection.


- [ ] Check more on write permissions to /etc/sudoers group.


```bash
student ALL= NOPASSWD : /bin/vim
```

```
username host=(runasuser:runasgroup) Commandtoexecute:All
```

```
cbbn ALL=NOPASSWD:ALL 
```

```bash
student ALL=NOPASSWD:ALL" >> /etc/sudoers
``` 

