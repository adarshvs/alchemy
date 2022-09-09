# Applications
----------------

## Startup Apps
Default Startup directory for all users:
```
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
```

If we can write a file to this directory we can use our reverse shell to spawn a administrator shell.

Startup apps in this directory must be shortcuts (.lnk file).

----------------------

## Installed Applications
Manually enumerating running programs:
```
tasklist /V
```

```
.\seatbelt.exe NonstandardProcesses
```

```
.\winPEASany.exe quiet procesinfo
```

-----------------------

##  Insecure GUI Apps

If a legacy application or any application is running as administrator, we can abuse this to spawn a child process which will also be run with administrative privileges.
