#!/usr/bin/python3

"""
Module for number_of_lines.
"""


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        return(len(list(f)))
