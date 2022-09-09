# Scheduled Tasks
-----
Listing scheduled tasks by the current user:
```
schtasks /query /fo LIST /v
```

```
Get-ScheduledTask | where {$_.TaskPath -notlike "\Microsoft*"} | ft TaskName,TaskPath,State
```

If any script is found running as a scheduled task, use accesschk.exe to check for write permissions.

