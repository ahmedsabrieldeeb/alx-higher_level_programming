#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "XX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
