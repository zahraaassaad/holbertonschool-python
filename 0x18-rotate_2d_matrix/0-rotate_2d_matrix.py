#!/usr/bin/python3
import numpy as np

"""
Module for rotate_2d_m.
"""


def rotate_2d_m(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees."""
    matrix_cp = np.copy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = matrix_cp[len(matrix)-1-j][i]
