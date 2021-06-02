#!/usr/bin/python3
"""Module: 1-write_file
Contains write_file() function that returns the number
of characters written
"""


def write_file(filename="", text=""):
    """ Args: filename as name of file
              text as content to write in file
       This function writes a string to a text file(UTF8)
    and returns then number of characters written
    """

    with open(filename, 'w') as f:
        return f.write(text)
