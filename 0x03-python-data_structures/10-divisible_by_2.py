#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in range(len(my_list)):
        if my_list[n] % 2 == 0:
            m = True
            new_list.append(m)
        else:
            m = False
            new_list.append(m)
    return new_list
