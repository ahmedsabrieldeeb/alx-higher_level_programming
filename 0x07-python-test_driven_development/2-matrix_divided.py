#!/usr/bin/python3

"""
    A module that cotains only one function
    a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    A function to divide a matrix by some number element wise

    Args:
        matrix (list of lists): a matrix containing integers or floats only
        div (int or floa): the dividend.

    Returns:
        list of lists (int, floats): representing quotient

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Notes:
        the returned matrix will be the same size as the input one
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    first_length = len(matrix[0])
    for row in matrix:
        if first_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_row.append(round((element / div), 2))
        new_matrix.append(new_row)

    return new_matrix
