# Flow
----------

### Port Scans
------------------
```bash
nmap -sC -sV -v --open -oN nmap_default.out $IP
nmap -sC -sV -v --open -Pn -oN nmap_default.out $IP

nmap -p- -v --open -oN nmap_full.out $IP
nmap -p- -v -Pn --open -oN nmap_full.out $IP

rustscan -a $IP
```

### Directory Fuzz
---------
```bash
gobuster dir -u http://$IP/ -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt

gobuster dir -u http://:$IP/ -w /opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt

python3 /opt/dirsearch/dirsearch.py -u http://10.10.10.191/

```

### Subdomain FUZZ
------------
```bash
wfuzz -w /opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --hc 404 -c -u http://backdoor.htb -H "Host:FUZZ.backdoor.htb" 
```



nginx -> almost no php