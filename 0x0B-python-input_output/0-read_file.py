#!/usr/bin/python3
""" Read a text file """


def read_file(filename=""):
    """ Read a file and print """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
