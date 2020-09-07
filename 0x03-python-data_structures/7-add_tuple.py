#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = 0, 0
    elif len(tuple_a) == 1:
        a,  = tuple_a
        tuple_a = a, 0
    if len(tuple_b) == 0:
        tuple_b = 0, 0
    elif len(tuple_b) == 1:
        b,  = tuple_b
        tuple_b = b, 0
    a1, a2 = tuple_a
    b1, b2 = tuple_b

    sum1 = a1 + b1
    sum2 = a2 + b2

    new_tuple = sum1, sum2

    return new_tuple
