#!/usr/bin/env python

"""
This script creates a csv file from a dhcp printer reservation conf
"""

def parse_config(file):
    with open(file) as fin:
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
                print(row[:-1])
            else:
                row += f'{line},'
                last_was_comment = False

parse_config('src/printers.conf')

