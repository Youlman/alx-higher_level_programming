#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ Replace an element of a list without the original list.
        Args:
            my_list: a list
            idx: the specific position
            element: the element to insert
        Returns:
            copy original list or new list
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    new_list = []
    for val in my_list:
        new_list.append(val)

    new_list[idx] = element
    return (new_list)
