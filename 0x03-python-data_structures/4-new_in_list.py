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
    new_list = []
    for i in range(len(my_list)):
        new_list.append(my_list[i])

    if idx < 0 or idx > (len(new_list) - 1):
        return (new_list)

    new_list[idx] = element
    return (new_list)
