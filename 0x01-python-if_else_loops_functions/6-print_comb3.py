#!/usr/bin/python3
for n in range(0, 9):
    for x in range(n + 1, 10):
        print('{}'.format(str(n) + str(x)), end=(',\
 ' if int(str(n) + str(x)) < 89 else '\n'))
