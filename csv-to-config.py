#!/usr/bin/env python

"""
This script parses a csv file and from it creates 
a dhcp reservation printer config file.
"""

import csv

def parse_csv(file):
    with open(file) as fin:
        ss = csv.reader(fin)
        for row in ss:
            for word in row:
                if word[:4] == 'host':
                    print(f'{word} {{')
                elif word[:1] == '#':
                    comments = word[1:].split('#')
                    for comment in comments:
                        print(f'\t#{comment}')
                else:
                    print(f'\t{word}')
            print('}\n')

parse_csv('src/dhcp.csv')

