#!/usr/bin/python

from socket import *
import optparse
from threading import *

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

main()