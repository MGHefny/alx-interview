#!/usr/bin/python3
"""model island per"""


def island_perimeter(grid):
    """the island function"""
    coun = 0

    """the row"""
    for l_r in range(len(grid)):
        """the coulmn"""
        for l_c in range(len(grid[l_r])):
            left = grid[l_r][l_c]
            if left == 1:
                if l_c == 0:
                    """head"""
                    coun += 1
                    if grid[l_r][l_c + 1] == 0:
                        coun += 1
                elif l_c == len(grid[0]) - 1:
                    if grid[l_r][l_c - 1] == 0:
                        coun += 1
                    coun += 1
                else:
                    """head"""
                    if grid[l_r][l_c - 1] == 0:
                        coun += 1
                    if grid[l_r][l_c + 1] == 0:
                        coun += 1
                if l_r == 0:
                    coun += 1
                    if grid[l_r + 1][l_c] == 0:
                        coun += 1
                elif l_r == len(grid) - 1:
                    """head"""
                    if grid[l_r - 1][l_c] == 0:
                        coun += 1
                    coun += 1
                else:
                    if grid[l_r - 1][l_c] == 0:
                        coun += 1
                    if grid[l_r + 1][l_c] == 0:
                        coun += 1

    return coun
