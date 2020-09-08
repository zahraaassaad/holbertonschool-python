#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if matrix:
        result = []
        for row in matrix:
            squared = []
            for i in row:
                squared.append(i ** 2)
            result.append(squared)
    return result
