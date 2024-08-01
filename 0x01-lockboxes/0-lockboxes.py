#!/usr/bin/python3
"""Box list"""


def canUnlockAll(boxes):
    """boxe can unlocked"""
    pos = 0
    unlocked = {}
    box_num = len(boxes)

    while pos < box_num:
        if len(boxes[pos]) == 0 or pos == 0:
            unlocked[pos] = "always_unlocked"

        x = 0
        while x < len(boxes[pos]):
            k = boxes[pos][x]
            if k < box_num and k != pos:
                unlocked[k] = k
            x += 1

        if len(unlocked) == box_num:
            return True

        pos += 1

    return False
