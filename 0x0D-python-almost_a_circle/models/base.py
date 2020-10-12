#!/usr/bin/python3
"""
    base.py
    Module defining base
    return {}
"""


class Base():
    """A base class."""

    # A class variable, counting the number of bases
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
