#!/usr/bin/python
import os
import beanstalkc
import netifaces
import argparse
import textwrap
import json

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='zabbix-beanstalkd-discover.py', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
                        TODO
                        '''), epilog="e.g. zabbix-beanstalkd-discover.py -p <beanstralk port> --get <tube> <stat name>")
    parser.add_argument('-p', '--port', help='set beanstalkd port', required=False, default='11300')
    parser.add_argument('--get', nargs = '*', help='get tube stats', required=False)
    parser.add_argument('--discover', help='discover tubes', required=False, action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s v0.1')
    args = parser.parse_args()

    beanstalk = beanstalkc.Connection(host='localhost', port=11300)
    if args.get and len(args.get) == 2:
        tube = args.get[0]
        stat = args.get[1]
        print beanstalk.stats_tube(tube)[stat]
    elif args.discover:
     tubes = beanstalk.tubes()
     data = [{"{#TUBENAME}": tube} for tube in tubes]
     print(json.dumps({"data": data}))
