#!/usr/bin/python3
""" Defines the class Square that inherits from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a new Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initiaize a new Square
            Args:
                size (int): The size of the new Square.
                x (int): x coordinate
                y (int): y coordinate
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """ Return the print() and  str() representation of the Square """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)
