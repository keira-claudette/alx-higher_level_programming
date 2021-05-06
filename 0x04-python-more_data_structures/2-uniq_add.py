#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_items = set(my_list)
    result = 0
    for i in uniq_items:
        result += i

    return result
