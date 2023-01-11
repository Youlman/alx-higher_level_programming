#!/usr/bin/python3

""" Class MyList"""


class MyList(list):
    """ MyList """

    def print_sorted(self):
        """ Print ascending sort """
        print(sorted(self))
