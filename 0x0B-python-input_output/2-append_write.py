#!/usr/bin/python3
""" Append a text file """


def append_write(filename="", text=""):
    """ Append string to a file and return number f characters """
    with open(filename, 'a', encoding="utf-8") as f:
        number_characters = f.write(text)

    return (number_characters)
