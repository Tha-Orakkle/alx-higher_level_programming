#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0;
    length  = len(my_list) - 1
    my_list = my_list.reverse()
    while i <= length:
        print("{:d}".format(my_list[i]))
        i = i + 1
