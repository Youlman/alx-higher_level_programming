#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ Finds all multiples of 2 a list
        Args:
            my_list: a list
        Returns:
            The new list with True or False
    """
    new_list = []
    for val in my_list:
        if val % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
