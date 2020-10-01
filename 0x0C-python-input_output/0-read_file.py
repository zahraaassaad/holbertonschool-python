#!/usr/bin/python3

"""
Module for read_file.
"""


def read_file(filename=""):
    "reads a text file (UTF8) and prints it to stdout."
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')
