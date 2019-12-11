#!/usr/bin/python
print("hello")
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(10)

#host = "10.0.2.15"
host = "160.153.138.71"
port = 1

def portscanner(port):
        if sock.connect_ex((host, port)):
            print("port %d is closed ") % (port)
        else:
            print("port %d is open ") % (port)

for port in range(1,99):
        portscanner(port)
