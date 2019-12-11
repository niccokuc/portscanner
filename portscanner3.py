#!/usr/bin/python

print("hello")
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("Enter IP address to scan : ")
port = int(input("Enter Port to scan : "))

def portscanner(port):
        if sock.connect_ex((host, port)):
            print("port %d is closed ") % (port)
        else:
            print("port %d is open ") % (port)

portscanner(port)
