#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else
        max = list(a_dictionary)[0]
        for n in list(a_dictionary):
            if n > max:
                max = n
        return max
