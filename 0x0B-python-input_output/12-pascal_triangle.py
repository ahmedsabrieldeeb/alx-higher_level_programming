#!/usr/bin/python3
"""
Interview Question
"""


def pascal_triangle(n):
    """
    Returning a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n (int): triangle depth

    Returns:
        list: nested list representing the pascal triangle
    """

    pascal = []
    for row in range(n):
        row_list = []
        for element in range(row+1):
            try:
                if element-1 < 0:
                    raise IndexError
                left_side = pascal[row-1][element-1]
            except IndexError:
                left_side = 0

            try:
                right_side = pascal[row-1][element]
            except IndexError:
                right_side = 0

            if (left_side == right_side == 0):
                sum = 1
            else:
                sum = left_side + right_side

            row_list.append(sum)
        pascal.append(row_list)

    return (pascal)
