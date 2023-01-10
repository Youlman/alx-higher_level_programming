#!/usr/bin/python3
""" JSON Representation """


import json
def to_json_string(my_obj):
    """ JSON representation of an object """
    if isinstance(my_obj, set):
        raise TypeError(f"{my_obj} is not JSON serializable")
    return (json.dumps(my_obj))
