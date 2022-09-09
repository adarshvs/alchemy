# Subversion
------------

https://book.hacktricks.xyz/network-services-pentesting/3690-pentesting-subversion-svn-server
http://www.gcf.dkf.unibe.ch/BCB/files/BCB_Subversion_Cheat_Sheet.pdf

List files of a repo:
```bash
svn ls svn://10.10.10.203
```

Download repos:
```bash
svn checkout svn://10.10.10.203
```

Check log:
```bash
svn log svn://10.10.10.203
```

Check commits:
```bash
svn up -r 2
```