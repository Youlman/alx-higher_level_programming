#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """ Delete the item at a specific position
        Args:
            my_list: a list
            idx: the position
        Returns:
            The new list or the original
    """
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    
    for i in range(idx,len(my_list)):
        if i == len(my_list) - 1:
            del my_list[i]
            break
        my_list[i] = my_list[i + 1]

    return (my_list)
