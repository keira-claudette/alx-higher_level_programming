#!/usr/bin/python3

""" function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""

    if len(list_of_integers) == 0:
        return "None"
    else:
        mid = len(list_of_integers) // 2
        for item in list_of_integers:
            if item >= list_of_integers[mid]:
                peak = item
        return peak
