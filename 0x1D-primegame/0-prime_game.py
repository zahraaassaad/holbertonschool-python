#!/usr/bin/python3

"""
Module for isWinner.
"""


def isWinner(x, nums):
    """ Prime numbers game. """
    no = 0
    for number_of_rounds in range(x):
        isPrime = True
        for num in range(2, int(nums[number_of_rounds] ** 0.5) + 1):
            if nums[number_of_rounds] % num == 0:
                isPrime = False
                break

        if isPrime:
            no += 1

    if no % 2 == 0:
        return "Ben"

    elif no % 2 != 0:
        return "Maria"

    else:
        return None
