#!/usr/bin/python3

""" Define a class Square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the new square
            Args:
                size (int): The size of the new square
                position (int, int): the position of the new square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Position getter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """position setter"""
        if (not isintance(value, tuple) or len(value) != 2 or
                not all(isinstance(item, int) for item in value) or
                not all(item >= 0 for item in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculate the area of a sqaure

            returns:
                the current square area
        """
        return (self.__size*self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
