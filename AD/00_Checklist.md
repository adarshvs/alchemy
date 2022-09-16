# Checklist
-------

## unauthenticated

Make LDAP queries use windapsearch
Generate usernames if found on the webserver
Kerbrute - to enumerate users
Generate passwords using cewl

SMB Recon
RPC Recon

AS - REP roast

----
## after shell and/or creds

### priv esc?

If landed with not an admin user and to priv esc, check:
winPEAS
Print Nightmare
SAM the admin
Zerologon
goldenPAC

---
Check for logon credentials
Check for kerberoast
Check again if there are as-rep roastable users
Mimikatz - password dump

dump local SAM
dump NTDS


Pass the Hash
Bloodhound
DC Sync
LAPS Passwords
SPN Impersonate

------------






