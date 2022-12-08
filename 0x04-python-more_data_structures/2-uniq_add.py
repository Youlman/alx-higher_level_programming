#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ Adds all unique in a list
        Args:
            my_list: The initial list
        Returns:
            the list
    """

    result = 0
    for x in set(my_list):
        result += x
    return (result)
