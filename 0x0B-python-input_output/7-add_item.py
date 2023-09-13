#!/usr/bin/python3
"""
Adding all arguments to a Python list, and then save them to a file

Functions:
    load_from_json_file(filename): load JSON file into a python object
    save_to_json_file(my_obj, filename): save object to JSON file
"""

import sys
import json

# importing modules
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
file_name = "add_item.json"

# read the arguments if there
argv = sys.argv
if (len(argv) > 1):
    new_list = argv[1:]
else:
    new_list = []

# manilulating the file
json_content = []
try:
    json_content = list(load_from_json_file(file_name))
except FileNotFoundError:
    with open(file_name, mode="w", encoding="utf-8") as new_file:
        pass
finally:
    json_content += new_list
    save_to_json_file(json_content, file_name)
