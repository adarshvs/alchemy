


Try setting SUID on the passwd binary.

- Whenever SUID bit is set on a binary, it implies that it will be executed as the owner of the binary.

- Same but to allow it to a group SGID bit is used.

- Sticky bit (Check it again)

Special bits -> 7 

SUID - 4
SGID - 2 
Sticky bit - 1

Using relative paths in binaries lead to command injection.


