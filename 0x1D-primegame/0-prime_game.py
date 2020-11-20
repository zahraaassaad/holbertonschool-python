#!/usr/bin/python3

"""
Module for isWinner.
"""


def isWinner(x, nums):
    """ Prime numbers game. """
    biggest_prime = nums[-1]
    if biggest_prime < 1 or x < 0 or nums == []:
        return None
    if x > biggest_prime:
        for i in range(biggest_prime + 1, x + 1):
            for y in range(2, int(x ** .5) + 1):
                if x % y:
                    nums.append(i)
    return 'Ben' if sum(i <= x for i in nums) % 2 else 'Maria'
