# SMB  
---------


### enum4linux:

```bash
python3 /opt/enum4linux-ng/enum4linux-ng.py 10.10.10.100
```

### rpclient:

```bash
rpcclient 10.10.104.212 -U ""    #anonymous authentication
```

### smbmap:

```bash
smbmap -H 10.10.10.100 -r   #unauthenticated
smbmap -H 10.10.10.100 -u SVC_TGS -p password
smbmap -H 10.10.10.100 -d active.htb -u SVC_TGS -p password 
```

if we get an error like this 

```bash
smbmap -H atom.htb             

[!] Authentication error on atom.htb
```

we can try some random username and password:

```bash
smbmap -H atom.htb -u ci -p cib                            
```


### smbclient:

```bash
smbclient -L \\10.10.10.100\\   #list shares unauthenticated
smbclient //10.10.10.100/Replication #connect unauthenticated
smbclient //10.10.10.100/Replication -U ""%"" #connect unauthenticated
smbclient //10.10.10.100/Users -U active.htb/SVC_TGS #connect authenticated; will prompt for password
smbclient //10.10.10.100/C$ -U active.htb\\administrator
```

### crackmapexec:

```bash
cme smb 10.10.10.10 -u username -p password #password spray or checking for valid creds

cme smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --shares   #list shares

crackmapexec smb 10.10.10.10 -u 'user' -p 'pass' -M spider_plus

crackmapexec smb 10.10.10.10 -u 'user' -p 'pass' -M spider_plus -o READ_ONLY=false ##dumpallfiles
```


### impacket:

```bash
python3 psexec.py active.htb/administrator@10.10.10.100

python3 smbexec.py active.htb/administrator@10.10.10.100
```


### mounting smb shares:
windows:
```bash
sudo mount -t cifs //10.10.10.10/Backups /mnt/backup

sudo mount -t cifs -o 'user=t.thompson,password=' //10.10.10.182/Data /mnt/data
```


## checking smb version using wireshark 

if the victim is old and uses smbv1 the smbclient tool does not connect throwing protocol fail error, in that case add these lines under global settings in /etc/samba/sm.b.conf

```txt
client min protocol = CORE
client max protocol = SMB3
#client min protocol = SMB1
```

use this script to initiate a smb connection and capture the requests using wireshark to determine the smb version:

```bash
#!/bin/bash

if [ -z $1 ]; then echo "Usage: ./smbver.sh RHOST {RPORT}" && exit; else rhost=$1; fi
if [ ! -z $2 ]; then rport=$2; else rport=139; fi
tcpdump -s0 -n -i tun0 src $rhost and port $rport -A -c 10 2>/dev/null | grep -i "samba\|s.a.m" | tr -d '.' | grep -oP 'UnixSamba.*[0-9a-z]' | tr -d '\n' & echo -n "$rhost: " &
echo "exit" | smbclient -L $rhost 1>/dev/null 2>/dev/null
echo "" && sleep .1
```

in most cases enum4linux-ng gave me the correct smb version.

https://4pfsec.com/manually-enumerating-smb-version/

- [ ] Include setting up an anonymous smb share