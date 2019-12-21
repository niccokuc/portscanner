#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((tgtHost,tgtPort))
        print('[+] %d/tcp Open') % tgtPort
    except:
        print('[-] %d/tcp Closed') % tgtPort
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    # resolve the domain name into an IP. use get host by name.
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Cant resolve target host into IP address %s') %tgtHost
        exit()

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan results for: ' + tgtHost +' '+ tgtName[0])
    except:
        print('[+] Scan results for: ' + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports sperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
            print('usage :' + (parser.usage))
            print(parser.defaults)
            exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()