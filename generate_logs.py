#!/usr/bin/env python3
'''This script will generate log files at a target directory'''

__author__  = 'msanchavila'
__version__ = '0.0.1'
__license__ = 'MIT'

import sys
import os
import argparse
import subprocess
from datetime import datetime as dt


SERVICES       = ['MemeLourde', 'AutoMeme']
FLOG_EXE       = 'flog/flog.exe'
DATESTAMP      = dt.now().strftime('%Y%m%d')
LOG_TOTAL_SIZE = '10000000' # ~10MB
LOG_MAX_SIZE   = '1000000'  # ~1MB


def main(log_dir):
    
    for service in SERVICES:
        # create logfile name
        logfile = f'{log_dir}/{DATESTAMP}_{service}.log'
        
        # define command
        command = [FLOG_EXE, '-t', 'log', '-w', '-o', logfile, 
            '-b', LOG_TOTAL_SIZE, '-p', LOG_MAX_SIZE]

        print(f'Executing command: {" ".join(command)}')
        process = subprocess.Popen(command, stdout=subprocess.PIPE)

        while True:
            output = process.stdout.readline()
            if not output and process.poll() is not None:
                break

            if output:
                print(output.strip())

        print(f'Return Code: {process.poll()}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-o', '--out', nargs='?', default='logs', 
        help='Output directory for logs')
    args = parser.parse_args()

    main(args.out)