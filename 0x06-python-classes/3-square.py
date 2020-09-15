#!/usr/bin/python3
"""
    3-square.py
    Module defining square by private instance attribute size
    raises exception if size < 0 or size non integer
    return size
"""


class Square:
    """Square class.
       It defines a square by private instance attribute size.
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
        """Calculates and returns square area.
           return area
        """
        return self.__size ** 2
