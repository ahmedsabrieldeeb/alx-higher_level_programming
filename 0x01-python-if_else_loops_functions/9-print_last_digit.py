#!/usr/bin/python3
def print_last_digit(number):
    last_digit = number % 10
    print(last_digit % 10, end='')
    return (last_digit % 10)
