#!/usr/bin/python3
"""
    4-square.py
    Module defining square
    return {}
"""

class Square:
    """Class Square"""

    def __init__(self, size=0):
        """method to initiate"""
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method to initalize value"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """class method to return current square area"""
        return (self.__size**2)
'''
#!/usr/bin/python3
"""
    4-square.py
    Module defining square
    return {}
"""


class Square:
    """Square class. It defines a square.
       return size
    """
    def __init__(self, size=0):
        """Initializes the data.
        return size
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve __size of Square class."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set __size of Square class."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
'''
