#!/usr/bin/python3
""" Module: 0-read_file
contains a function read_file() that prints
file content to standard output
"""


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints to stdout"""

    with open(filename, 'r') as f:
        data = f.read()
        print(data, end='')
