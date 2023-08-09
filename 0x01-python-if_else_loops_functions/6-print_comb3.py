#!/usr/bin/python3
for i in range(0, 89):
    second_digit = i % 10
    first_digit = (i - second_digit) // 10
    if ((second_digit - first_digit) < 0):
        pass
    else:
        if (first_digit == second_digit):
            pass
        else:
            print("{:02}, ".format(i), end='')
print("89")
