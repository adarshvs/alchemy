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


Remember **SEARCHSPLOIT** and **METASPLOIT**



nginx -> almost no php





https://therealunicornsecurity.github.io/OSCP/#tldr-



### Compiling exploits

32bit linux 
```bash
gcc -m32 -march=i686 code.c -o exp -static
```

Cross compile exploit for windows
```bash
# dpkg --add-architecture i386
# install mingw32/64
# 32 bits:
i686-w64-mingw32-g++-win32 exp.cpp -static -o exp
# 64 bits:
x86_64-w64-mingw32-g++ exp.cpp -static -o exp
```



