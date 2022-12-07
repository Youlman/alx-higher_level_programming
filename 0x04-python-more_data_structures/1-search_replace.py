#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Replaces all occurences of an element by another in a new list"
        Args:
            my_list: The initial
            search: the element too replace in the list
            replace: the new element
        Returns:
            the list
    """
    new_list = []
    for value in my_list:
        if value == search:
            new_list.append(replace)
        else:
            new_list.append(value)

    return (new_list)
