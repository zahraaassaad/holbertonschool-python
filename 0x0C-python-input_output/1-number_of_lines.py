#!/usr/bin/python3

"""
Module for number_of_lines.
"""


def number_of_lines(filename=""):
    """Return the number of lines of a text file."""
    with open(filename, 'r') as f:
        return(len(list(f)))
