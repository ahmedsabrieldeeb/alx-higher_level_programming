#!/usr/bin/python3

def no_c(my_string):
    if len(my_string) != 0:
        characters_to_remove = ['c', 'C']
        result_string = "".join(char for char in my_string if char not in characters_to_remove)
        return result_string
    return ""
