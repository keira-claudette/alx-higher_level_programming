#!/usr/bin/python3
"""
Module: 6-load_from_json_file
Contains load_from_json_file() function that creates an
Object  from a "JSON file"
"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""

    with open(filename, 'r') as f:
        return json.load(f)
