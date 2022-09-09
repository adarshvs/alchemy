# Flow
-------

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