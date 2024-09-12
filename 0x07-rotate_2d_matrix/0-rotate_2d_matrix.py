#!/usr/bin/python3
""" rotate 2d matrix n*n
"""


def rotate_2d_matrix(matrix):
    """ rotate 2d matrix n*n
    """
    n = len(matrix[0])
    b = matrix[y][x], matrix[x][y]

    for x in range(n):
        for y in range(x, n):
            matrix[x][y], matrix[y][x] = b

    for x in range(n):
        matrix[x].reverse()
