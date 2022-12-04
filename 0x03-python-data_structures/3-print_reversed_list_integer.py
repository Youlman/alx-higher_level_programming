#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print all the elments of a list in reverse.
        Args:
            my_list: a list
    """
    for i in range(len(my_list), 0, -1):
        print("{:d}".format(my_list[i - 1]))
