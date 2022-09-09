# Enumeration
------------------------

https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_windows.html]

## System
```powershell

# SYSTEM 
systeminfo	#system information
systeminfo | findstr /B /C:"OS Name"

wmic # windows management instrumentation commandline
wmic qfe	#quick fix engineering -> list patches


wmic logicaldisk	#list all drives
list drives
wmic logicaldisk get caption,description


findstr /si password *.txt *.ini	#look for passwords
```


## User
```powershell
# USER
whoami
whoami /priv
whoami /groups

net user	#get users on the machine
net user cibbin

net localgroup
net localgroup Administrator
```


## Network
```powershell
# NETWORK
ipconfig
ipconfig /all

arp -a

route print	#print routing table

# checking for services available only from the inside:
netstat -ano
```


## AV and Firewall
```powershell
# AV and FIREWALL 
sc query windefend	#info about windows defender

netsh advfirewall firewall dump	#prints state of the firewall
netsh firewall show state

```


## Services
```powershell
net start #list running services
net start | findstr "Wise" #grep
net start | Select-String "Wise"


sc queryx type= service	#list running services
sc stop SERVICENAME
sc query SERVICENAME
sc stop SERVICENAME
```

