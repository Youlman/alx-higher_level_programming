#!/usr/bin/python3

def print_last_digit(number):
    """Return the last digit of number."""
    digit = abs(number) % 10
    if number < 0:
        digit = -digit
    return digit
