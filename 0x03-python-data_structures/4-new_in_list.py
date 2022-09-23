#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    i = 0
    new_list = []
    while i < len(my_list):
        n = my_list[i]
        new_list.append(n)
        i = i + 1
    new_list[idx] = element
    return new_list
