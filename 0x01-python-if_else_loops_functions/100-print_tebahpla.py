#!/usr/bin/python3
for i in range(122, 96, -1):
    k = i
    if ((i % 2) == 0):
        pass
    else:
        k = k - 32
    print("{}".format(chr(k)), end='')
