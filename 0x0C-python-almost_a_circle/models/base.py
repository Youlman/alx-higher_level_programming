#!/usr/bin/python3
""" Define Base class """


class Base:
    """ Represent Base class

    Attributes:
        __nb_objects (int): number of intantiated Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize a Base 

        Args:
            id (int): the identity of the new base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
