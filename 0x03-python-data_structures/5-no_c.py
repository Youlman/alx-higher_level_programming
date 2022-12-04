#!/usr/bin/python3

def no_c(my_string):
    """ Removes all characters c and C from.
        Args:
            my_string: a string
        Returns:
            new string
    """

    new_string = ""
    for char in my_string:
        if char == 'c' or char == 'C':
            continue
        new_string += char

    return (new_string)
