#!/usr/bin/python3

"""
Module for read_lines.
"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r') as f:
        if nb_lines <= 0 or nb_lines >= len(open(filename).readlines()):
            nb_lines = len(open(filename).readlines())
        for i in range(nb_lines, 0, -1):
            print(f.readline(), end="")
