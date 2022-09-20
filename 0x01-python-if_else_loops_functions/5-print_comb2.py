#!/usr/bin/python3
for ch in range(100):
    if ch < 10:
        print("0{}".format(ch), end=", ")
        continue
    print("{}".format(ch), end=(", " if ch < 99 else "\n"))
