#!/usr/bin/python3
"""
Module is 5-text_indentation
This module defines a function that rints a text with 2 new lines after each of
 these characters: ., ? and :
"""


def text_indentation(text):
    """ This function prints a text with 2 lines after each of these
    characters: . , :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for item in ".?:":
        text = (item + \n\n).join(
            [line.strip(" ") for line in text.split(item)])

    print("{}".format(text), end='')
