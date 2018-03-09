#!/usr/bin/env python

"""
This script creates a csv file from a dhcp printer reservation conf
"""

import sys
import os

def parse_config(input_file, output_file=None):
    if output_file and os.path.exists(output_file):
        try:
            os.remove(output_file)
        except OSError as e:
            print(e)
            pass 
    with open(input_file) as fin:
        for line in fin.readlines():
            line = line.strip()
            if line[:4] == 'host':
                row = f'{line[:-2]},'
                last_was_comment = False
            elif line[:1] == '#':
                if last_was_comment:
                    row = row[:-1]
                    row += f' {line},'
                else:
                    row += f'{line},'
                last_was_comment = True
            elif line == '}':
                process_output(row[:-1], output_file)
            else:
                row += f'{line},'
                last_was_comment = False

def process_output(output, output_file=None):
    if output_file:
        with open(output_file, 'a') as fout:
            fout.write(f'{output.rstrip()}\n')
    else:
        print(output)

if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) > 1:
        parse_config(arguments[0], arguments[1])
    else:
        parse_config(arguments[0])

