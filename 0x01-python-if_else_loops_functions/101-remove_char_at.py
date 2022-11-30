#!/usr/bin/python3

def remove_char_at(str, n):
    """Copy a string and remove at position"""
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1:])
