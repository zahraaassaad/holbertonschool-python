#!/usr/bin/python3

"""
Module for rotate_2d_m.
"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees."""
    N = len(matrix[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = matrix[i][j] 
            matrix[i][j] = matrix[N - 1 - j][i] 
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j] 
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i] 
            matrix[j][N - 1 - i] = temp
