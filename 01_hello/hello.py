#!/usr/bin/env python3
"""Say Hello""" 
import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('-n', '--name', metavar='name', default='World', help='usage: hello.py [-h] [-n name]')  
args = parser.parse_args()
print(f'Hello, {args.name}!')   # This is the main function that prints the output