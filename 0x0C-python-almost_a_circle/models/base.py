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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write an object to a text file using JSON representation.
            Args:
                list_objs(list): list of Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [ob.to_dictionary() for ob in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
