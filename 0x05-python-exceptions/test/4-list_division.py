#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = [0] * list_length
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            new_list[i] = res
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            pass
    return (new_list)
