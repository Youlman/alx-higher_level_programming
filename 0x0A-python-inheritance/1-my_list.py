#!/usr/bin/python3

""" Class MyList"""


class MyList(list):
    """ MyList """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ Print ascending sort """
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
