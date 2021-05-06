#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''
    first check if key doesn't exist so you add, swapping the order of
    codeblocks would result in RunTimeError, Dictionary changed size during
    iteration.
    '''
    if key not in a_dictionary:
            a_dictionary[key] = value
    for i in a_dictionary:
        if i == key:
            a_dictionary[i] = value
    return a_dictionary
