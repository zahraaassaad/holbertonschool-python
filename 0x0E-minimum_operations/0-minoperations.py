#!/usr/bin/python3

"""
Module for minOperations.
"""


def minOperations(n):
    """calculates the fewest number of operations needed."""
    res = 0
    for i in range(2, n):
        while n%i == 0:
            res += i
            n = n/i
    if n != 1:
        return 0
    return res
