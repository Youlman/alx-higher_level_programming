#!/usr/bin/python3
""" Write a text file """


def write_file(filename="", text=""):
    """ write string to a file and return number f characters """
    with open(filename, 'w', encoding="utf-8") as f:
        number_characters = f.write(text)

    return (number_characters)
