#!/usr/bin/python3
""" A class square that defines a square
"""


class Square:
    """ Empty class with size private att
    """
    def __init__(self, size=0):
        """ 
            Instantation with size
        Args: 
            size: size of square
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
