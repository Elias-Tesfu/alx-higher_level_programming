#!/usr/bin/python3
""" A class square that defines a square
"""


class Square:
    """ Empty class square with size private attribute
    """
    def __init__(self, size):
        """
            Instantation with size
        Args:
            size: size of the square
        """
        self.__size = size
