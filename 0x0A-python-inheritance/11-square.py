#!/usr/bin/python3
"""Defines Square inherits Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent Square from Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.
        Args:
            size (int): The size of the new Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
