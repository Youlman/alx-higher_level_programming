#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """ the square value of all integers of a matrix
        Args:
            matrix: a matrix
        Returns:
            a matrix
    """
    squared_matrix = []
    for row in matrix:
        col = []
        for val in row:
            col.append(val*val)
        squared_matrix.append(col)

    return (squared_matrix)
