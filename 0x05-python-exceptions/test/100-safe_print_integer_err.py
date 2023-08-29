#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as err1:
        print(f"Exception: {err1}"s, file=sys.stderr)
        return False
    except TypeError as err2:
        print(err2, file=sys.stderr)
    else:
        return True
