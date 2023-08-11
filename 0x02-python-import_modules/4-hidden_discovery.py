#!/usr/bin/python3
if __name__ == "__main__":
    module_path = "hidden_4.pyc"
    for item in dir(module_path):
        if (item[0] != '_'):
            print(item)
