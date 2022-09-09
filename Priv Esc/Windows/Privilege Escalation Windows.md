# Windows PE
----------


Unqouted Service Paths [[Enterprise]]
DnsAdmins / dll injection [[hackthebox/01 - OSCP_Machines/Resolute/Resolute]]
Print Nightmare [[Driver]]
DC Sync [[hackthebox/01 - OSCP_Machines/Forest/Forest]]
Azure Admins AD Sync [[hackthebox/01 - OSCP_Machines/Monteverde/Monteverde]]
WSL [[hackthebox/01 - OSCP_Machines/Secnotes/SecNotes]]







## Enumeration
-----------



Always Install Elevated:

```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
```