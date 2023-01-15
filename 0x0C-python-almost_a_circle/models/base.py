#!/usr/bin/python3
""" Define Base class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list dictionaries 
            Args:
                list_dictionaries(list): A list of dictionaries.                
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)
