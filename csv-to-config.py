#!/usr/bin/env python

"""
This script parses a csv file and from it creates 
a dhcp reservation printer config file.
"""

import sys
import os
import csv

def parse_csv(input_file, output_file=None):
    if output_file and os.path.exists(output_file):
        try:
            os.remove(output_file)
        except OSError as e:
            print(e)
            pass
    with open(input_file) as fin:
        ss = csv.reader(fin)
        for row in ss:
            for word in row:
                if word[:4] == 'host':
                    process_output(f'{word} {{', output_file)
                elif word[:1] == '#':
                    comments = word[1:].split('#')
                    for comment in comments:
                        process_output(f'\t#{comment}', output_file)
                else:
                    process_output(f'\t{word}', output_file)
            process_output('}\n', output_file)

def process_output(output, output_file=None):
    if output_file:
        with open(output_file, 'a') as fout:
            fout.write(f'{output}\n')
    else:
        print(output)

if __name__ == '__main__':
    arguments = sys.argv[1:]
    if len(arguments) > 1:
        parse_csv(arguments[0], arguments[1])
    else:
        parse_csv(arguments[0])
