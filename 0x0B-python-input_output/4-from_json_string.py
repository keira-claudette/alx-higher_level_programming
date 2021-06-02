#!/usr/bin/python3
"""
module: 4-from_json_string
contains from_json_string() function that returns an object
(Python data structure) represented by a JSON string:
"""


import json


def from_json_string(my_str):
    """ Args: my_str - JSON string to be deserialzed to a
    python dat a structure

    returns an object (Python data structure)
    """

    return json.loads(my_str)
