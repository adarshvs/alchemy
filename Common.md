## Common
----------

- [ ] nmap
- [ ] wfuzz outfile


port scan
```bash
rustscan -a $1 -- -A -sC -sV -oN nmap.out --open
#rust

nmap -sC -sV -v -Pn -oN nmap_pn.out 10.11.1.111 --open
#nmap -Pn 

sudo nmap -T3 -p- -vv $1 -oN nmap_full.out --open
#nmapfull

sudo nmap -T3 -p- -vv $1 -Pn -oN nmap_full.out --open
```

vuln scans
```bash
sudo nmap --script vuln -p 443,80 10.10.10.10

sudo nmap --script 'smb-vuln*' -p 445 -v 192.168.68.40
#smb vuln scan
```

UDP
```bash
sudo nmap -sUV -T4 -F --version-intensity 0 10.11.1.111

sudo nmap -n -Pn -sU -v -p69 -sV --script tftp-enum 10.11.1.111

sudo nmap -sU -T4 -v -oN nmap_udp 10.11.1.111

sudo nmap -A -sV -sC -v -sU 10.11.1.111 --script='*enum' --top-ports 20

sudo nmap -sUV -T3 -v -F --version-intensity 0 10.11.1.111

nmap -sV --script vnc-info,realvnc-auth-bypass,vnc-title -p 5800 10.11.1.227 -v
```

Proxychains
```bash
sudo proxychains nmap --top-ports=20 -sT -Pn -v 10.1.1.95 --open 

proxychains nmap -sT -Pn -p 21,22,80,111 -sC -sV -v 10.1.1.27 --open
```



directory fuzzing
```bash
wfuzz -z file,/opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt --hc 404 -c -u $1 -f wfuzz.out
#fuzzraft

wfuzz -z file,/opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt --hc 404 -c -u $1 -f wfuzz.out

#fuzz

gobuster -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -u $1
#gobust

gobuster -w /opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt -u $1
#gobustraft

# fuzzing with proxychains
dirsearch --proxy=socks5://localhost:1080 -e html -u http://10.1.1.27/  -w /opt/SecLists/Discovery/Web-Content/raft-medium-directories.txt


wfuzz -z file,/opt/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --hc 404 -c -u http://backdoor.htb -H "Host:FUZZ.backdoor.htb" 
```


cURL 
```bash
curl http://192.168.197.99:8089/  

curl -X POST http://192.168.197.99:33333/list-running-procs -d "" 

curl -G 'http://localhost/?' --data-urlencode 'cmd /c C:\\users\\ariah\\desktop\\payload.exe'
```




