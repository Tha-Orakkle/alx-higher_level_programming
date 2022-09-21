#!/usr/bin/python3
def uppercase(str):
    output = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            output += chr(ord(c) - 32)
        elif ord(c) >= 65 and ord(c) <= 90:
            output += c
        else:
            output += c
    print("{}".format(output))
