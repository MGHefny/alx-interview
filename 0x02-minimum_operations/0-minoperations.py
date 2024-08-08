#!/usr/bin/python3
"""numb method that calculates res"""


def minOperations(n):
    """fewest number needed to result in exactly"""
    opre = 0
    x = 2
    for x in range(2, int(n) + 1):
        while n % x == 0:
            opre += x
            n /= x
        if n == 1:
            break

    return opre
