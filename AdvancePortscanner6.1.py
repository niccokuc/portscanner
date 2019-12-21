#!/usr/bin/python

from socket import *
import optparse
from threading import *
opnprt = 0
clsprt = 0

def connScan(tgtHost, tgtPort):
    opnprt=0
    clsprt=0
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print('[+] %d/tcp Open') % tgtPort
        opnprt = opnprt + 1
    except:
        #print('[-] %d/tcp Closed') % tgtPort
        clsprt+=1
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts, tgtRange):
    # resolve the domain name into an IP. use get host by name.
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Cant resolve target host into IP address %s') % tgtHost
        exit()

    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan results for: ' + tgtHost + ' ' + tgtName[0])
    except:
        print('[+] Scan results for: ' + tgtIP)

    setdefaulttimeout(5)

    if tgtPorts != ['None']:
        print("[+] Scanning specific ports now:")
        for tgtPort in tgtPorts:
            t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
            t.start()

    if tgtRange != 'None':
        tgtRange = str(tgtRange).split(',')
        print("[+] Scanning the port range : " + tgtRange[0] + " to " + tgtRange[1])
        for tgtPort in range(int(tgtRange[0]),int(tgtRange[1])+1):
            t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
            t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target ports, a,b,c,d...> -r <target port range, n,m>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
    parser.add_option('-r', dest='tgtRange', type='string', help='specify target Range, eg. 25,100')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    tgtRange = str(options.tgtRange)
    if (tgtHost == None) | ((tgtPorts[0] == None) and (tgtRange == None)):
        print('usage :' + (parser.usage))
        print(parser.defaults)
        exit(0)
    portScan(tgtHost, tgtPorts, tgtRange)

if __name__ == '__main__':
    main()
