#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as arg_list

    if (len(arg_list) == 1):
        print("0")
    else:
        sum = 0
        for i in range(1, len(arg_list)):
            sum = sum + int(arg_list[i])

    print("{}".format(sum))
