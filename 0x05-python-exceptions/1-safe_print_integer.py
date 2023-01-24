#!/usr/bin/python3

def safe_print_integer(value):
    return_value = False
    try:
        print("{:d}".format(value))
        return_value = True
    except ValueError:
        return_value = False
    finally:
        return return_value
