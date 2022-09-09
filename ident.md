# ident
-------
port 113 TCP

If we have ident on port 113 open, we can identify the user of a particular TCP connection.
https://gitlab.com/kalilinux/packages/ident-user-enum

```bash
./ident-user-enum.pl 192.168.83.60 113 8080 10000 22

ident-user-enum v1.0 ( http://pentestmonkey.net/tools/ident-user-enum )

192.168.83.60:113	nobody
192.168.83.60:8080	<unknown>
192.168.83.60:10000	eleanor
192.168.83.60:22	root
```
