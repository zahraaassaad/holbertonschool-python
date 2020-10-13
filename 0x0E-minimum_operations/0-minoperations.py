#!/usr/bin/python3

"""
Module for minOperations.
"""


def minOperations(n):
    """calculates the fewest number of operations needed."""
    res = 0
    for i in range(2, n):
        while n%i == 0: #check if problem can be broken into smaller problem
            res += i #if yes then add no of smaller problems to result. If number = 25  i = 5 then 5*5 = 25 so add 5 to results
            n = n/i #create smaller problem
    return res
