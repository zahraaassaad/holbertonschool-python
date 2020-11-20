#!/usr/bin/python3

def isWinner(x, nums):
    """ Prime numbers game. """
    number_of_rounds = 0
    no = 0
    for number_of_rounds in range(x):
        isPrime = True
        for num in range(2, nums[number_of_rounds]):
            if nums[number_of_rounds] % num == 0:
                isPrime = False

        if isPrime:
            no += 1

    if no % 2 == 0:
        return "Ben"

    elif no % 2 != 0:
        return "Maria"

    else:
        return None
