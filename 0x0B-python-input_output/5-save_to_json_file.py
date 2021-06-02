#!/usr/bin/python3
"""
module: 5-save_to_json_file

contains save_to_json_file() function that writes an Object to a text file
using a JSON representation:
"""


import json


def save_to_json_file(my_obj, filename):
    """ Args: my_obj - object to serialize and store in file
              filename - name of file to save JSON representation of my_obj
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
