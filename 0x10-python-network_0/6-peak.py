#!/usr/bin/python3
"""
COntains a function that finds the peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds the peak"""
    if list_of_integers is None or list_of_integers == []:
        return None

    if len(list_of_integers) == 1:
        return (list_of_integers[0])

    if len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid])
