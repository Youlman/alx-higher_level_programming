#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """ all elements in only one sets
        Args:
            set_1: The first set
            set_2: the second set
        Returns:
            set of all elements present in one set
    """

    return (set_1.symmetric_difference(set_2))
