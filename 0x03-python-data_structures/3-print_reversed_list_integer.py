#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    if my_list == []:
        return None
    if not my_list:
        return None
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))
