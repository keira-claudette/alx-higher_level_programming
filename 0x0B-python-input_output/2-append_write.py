#!/usr/bin/python3
"""
Module: 2-append_write
Contans append_write() function that appends a string at the end of a text file
(UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) and returns the
    number of characters added.

    Args:
         filename = name of file to append
         text = text to append to file
    """

    with open(filename, 'a') as f:
        return f.write(text)
