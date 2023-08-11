#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as arg_list

    len_arg_list = len(arg_list)
    if (len_arg_list == 1):
        print("0 arguments.")
    else:
        print("{} arguments:".format(len_arg_list))
        for i in range(1, len_arg_list):
            print("{}: {}".format(i, arg_list[i]))
