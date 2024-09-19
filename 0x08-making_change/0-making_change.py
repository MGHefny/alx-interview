#!/usr/bin/python3
""" make change methoud
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    """ arr to save mini number value
    """
    co_mine = [float('inf')] * (total + 1)
    co_mine[0] = 0

    for x in range(total + 1):
        for c in coins:
            if x >= c:
                co_mine[x] = min(co_mine[x], co_mine[x - c] + 1)


    """ re value of mini numb
    """
    if co_mine[total] != float('inf'):
        return co_mine[total]
    else:
        return -1
