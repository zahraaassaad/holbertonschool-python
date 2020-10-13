#!/usr/bin/python3

"""
Module for minOperations.
"""


def minOperations(n):
    """calculates the fewest number of operations needed."""
    res = 0
    for i in range(n+1):
        while n % i == 0:
            res += i
            n = n/i
    return res
