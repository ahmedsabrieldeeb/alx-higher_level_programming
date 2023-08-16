#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    res = []
    for ls in matrix:
        res.append(list(map(lambda x: x ** 2, ls)))
    return res
