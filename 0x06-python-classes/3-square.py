#!/usr/bin/python3


class Square():
    """A square class."""

    def __init__(self, size=0):
        """Initialize class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
'''
#!/usr/bin/python3
"""
    3-square.py
    Module defining square
    return size
"""


class Square:
    """Square class. It defines a square.
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
        """function that calculates and returns square area.
           return area
        """
        return self.__size ** 2
'''
