#!/usr/bin/python3

""" Define a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize the size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculate the area of a sqaure

            returns:
                the current square area
        """
        return (self.__size*self.__size)
