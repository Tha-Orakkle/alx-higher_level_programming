#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for w in sorted(a_dictionary):
        print("{:s}: {}".format(w, a_dictionary[w]))
