#!/usr/bin/python
print("hello")
import socket
from colorama import Fore

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(10)

#host = "10.0.2.15"
host = input("[*] Enter the IP Address: ")
port_sta = input("[*] ENter start port range: ")
port_end = input("[*] ENter the end port range : ")

def portscanner(port):
        if sock.connect_ex((host, port)):
            print(Fore.RED + ("[!!] port %d is closed ") % (port))
        else:
            print(Fore.GREEN + ("[+] port %d is open ") % (port))

if port_sta == port_end:
    port=port_sta
    portscanner(port)
else:
    for port in range(port_sta,port_end):
        portscanner(port)
