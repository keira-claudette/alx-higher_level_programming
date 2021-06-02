#!/usr/bin/python3
"""
Module: 1-my_list
describes a class Mylist that inherits from list
"""


class MyList(list):
    """ inherits from list class"""

    def print_sorted(self):
        """ sorts and prints the assorted list"""

        a_list = self[:]
        a_list.sort()
        print("{}".format(a_list))
