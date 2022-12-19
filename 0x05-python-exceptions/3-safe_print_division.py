#!/usr/bin/python3

def safe_print_division(a, b):
    """ Divides 2 integers
        Args:
            a (int): the first integer
            b (int): the second number
        Returns:
            the result
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
