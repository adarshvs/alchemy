# SNMP
------

port UDP 161
```bash
sudo apt install onesixtyone
sudo apt install snmp-mibs-downloader
download-mibs
sudo apt install snmp
```

to use snmp-mibs-downloader thing:
```bash
subl /etc/snmp/snmp.conf  -> comment out mibs
```

```nmap
nmap -sU --open -p 161 -oG nmap_snmp 192.168.121.42
```

Enumeration
```bash
snmpwalk -c public -v2c -t 10 $IP # where c is the community string, v2c is the version on snmp
```

```bash
# fuzzing to get community string
onesixtyone -c /opt/SecLists/Discovery/SNMP/common-snmp-community-strings-onesixtyone.txt 192.168.209.42 
```

```bash
snmp-check 192.168.121.42
```

```bash
snmpwalk -c public -v2c 10.10.10.241 .
```