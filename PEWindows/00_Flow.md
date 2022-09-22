# Flow
-------

Check PS shell architecture:
```PS
[Environment]::Is64BitProcess
```

- winPEAS
- WES
- sherlock.ps1

Web root paths:

Xampp : `C:\xampp\htdocs`
IIS : `C:\inetpub\wwwroot` 



- Check for any special privileges or groups
```cmd
whoami /all
```

- Check for Active Directory permissions using BloodHound





- Check for applications or services running internally:
```cmd
.\winpeas.exe quiet networkinfo
```

Check PS ReadLine:

```cmd
cd C:\Users\legacy\APPDATA\roaming\microsoft\windows\powershell\psreadline> 
```


- insecure creds
- Registry keys
- Non standard applications
- Privileged Groups

PowerShell locations:
```cmd
# 32bit powershell
c:\windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe

# 64bit powershell
c:\windows\System32\WindowsPowerShell\v1.0\powershell.exe
C:\Windows\sysnative\WindowsPowershell\v1.0\powershell.exe
```