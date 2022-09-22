# Basic Checks
-----

OS and Architecture:
```bash
uname -a 
uname -m
cat /etc/issue
cat /etc/*-release
```

Running Processes and Services:
```bash
ps aux
sudo lsof -i tcp:445
netstat -lntp #list processes running on ports
netstat -lntp | grep -w ':80'
ss -anp
```

Network:
```bash
ip a
ifconfig
netstat -ano
/sbin/route
```

Installed Applications:
```bash
dpkg -l | grep
```

Capabilities:
```bash
getcap -r / 2>/dev/null
```

Writeable root PATH:
- echo $PATH variable to list out the directories set in the $PATH variable.
- If we have write access to any folder in the PATH and there exists a cron job that we can take advantage of, we can write a shell and get root.

- do manual checks
- run lse.sh
- linpeas.sh
- pspy


### find



















