#!/usr/bin/python3
"""
    1-my_list.py
    Module defining list
    return 
"""


class Square:
    """MyList class. It defines a list.
       return size
    """
    def __init__(self, size=0):
        """Initializes the data.
           return size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
