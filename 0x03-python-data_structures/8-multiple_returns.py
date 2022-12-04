#!/usr/bin/python3

def multiple_returns(sentence):
    """ The lentgh of string and the first
        Args:
            sentence: a string
        Returns:
            a tuple with the length of a string and its first character
    """
    if len(sentence) == 0:
        return None
    return (len(sentence), sentence[0])
