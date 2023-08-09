#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for i in range(len(str)):
        decimal = ord(str[i])
        if (decimal >= 97 and decimal <= 122):
            upper_str = upper_str + chr(decimal - 32)
        else:
            upper_str = upper_str + str[i]
    print("{}".format(upper_str))
