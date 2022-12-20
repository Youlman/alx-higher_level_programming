#!/usr/bin/python3

""" Define a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize the size"""
        self.__size = size

    @property
    def size(self):
        """Size getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the area of a sqaure

            returns:
                the current square area
        """
        return (self.__size*self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

