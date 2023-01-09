#!/usr/bin/python3

""" Class MyList"""


class MyList(list):
    """ MyList """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ Print ascending sort """
        print(sorted(self))
