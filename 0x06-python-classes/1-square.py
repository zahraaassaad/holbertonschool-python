#!/usr/bin/python3
"""
    1-square.py
    Module defining square by private instance attribute size
    return {}
"""


class Square:
    """Square class.
       It defines a square by private instance attribute size
    """
    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
