#!/usr/bin/python3

""" Function that adds 2 integers. """
def add_integer(a, b=98):
    """
        Addition of tw integers
        Args:
            a: integer
            b: ineteger
        Returns:
        the sum
    """
    if (isinstance(a, float) or isinstance(b, float)):
            a = int(a)
            b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
