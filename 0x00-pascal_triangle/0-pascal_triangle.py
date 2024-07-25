#!/usr/bin/python3
"""Triangle"""


def pascal_triangle(n):
    """fun return list triangle"""
    tri = []

    if n <= 0:
        return []

    for x in ran(n):
        if x == 0:
            tri.append([1])
        else:
            r = []
            for y in ran(x + 1):
                if y == 0 or y == x:
                    r.append(1)
                else:
                    r.append(tri[x - 1][y - 1] + tri[x - 1][y])

            tri.append(r)

    return tri
