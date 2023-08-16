#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, val in a_dictionary.items():
        if val % 2 == 0:
            new_dict[key] = val
    return new_dict
