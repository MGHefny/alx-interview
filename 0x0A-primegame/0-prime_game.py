#!/usr/bin/python3
"""Prime Game"""


def prnumber(n):
    """prime number"""
    pr = []
    s = [True] * (n + 1)
    for a in range(2, n + 1):
        if (s[a]):
            pr.append(a)
            for b in range(a, n + 1, a):
                s[b] = False
    return pr


def isWinner(x, nums):
    """is winner fun"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for b in range(x):
        pr = prnumber(nums[b])
        if len(pr) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
