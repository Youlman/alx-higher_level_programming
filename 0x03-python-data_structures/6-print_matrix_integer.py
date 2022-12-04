#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """ Prints a matrix of integers.
        Args:
            matrix: the matrix
    """

    for row in matrix:
        for val in row:
            print("{:d} ".format(val), end="")
        print()
