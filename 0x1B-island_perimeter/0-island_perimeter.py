#!/usr/bin/python3

"""
Module for to_graph.
"""


def island_perimeter(grid):
        """ Returns the perimeter of the island described in grid."""
        num = 0
        neighbor = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num = num + 1
                    if i > 0 and grid[i-1][j] == 1:
                        neighbor += 1
                    if j>0 and grid[i][j-1] == 1:
                        neighbor += 1
        return num * 4 - neighbor *2
