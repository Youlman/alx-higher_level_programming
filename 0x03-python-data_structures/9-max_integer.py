#!/usr/bin/python3

def max_integer(my_list=[]):
    """ Finds the biggest integer of a list
        Args:
            my_list: a list
        Returns:
            The max of a list
    """
    if len(my_list) == 0:
        return None

    maxi = my_list[0]
    for val in my_list:
        if val > maxi:
            maxi = val
    return (maxi)
