#!/usr/bin/python3
""" make change methoud
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    y = total + 1
    """ arr to save mini number value
    """
    co_mine = [float('inf')] * (y)
    co_mine[0] = 0

    for c in coins:
        for x in range(c, y):
            co_mine[x] = min(co_mine[x], co_mine[x - c] + 1)

    """ re value of mini numb
    """
    if co_mine[total] != float('inf'):
        return co_mine[total]
    else:
        return -1
