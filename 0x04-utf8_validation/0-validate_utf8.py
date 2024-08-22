#!/usr/bin/python3
"""
Task 0 UTF-8 Validation
"""


def validUTF8(data):
    """
    return the int of list valid utf-8
    the count of the byte or true or fals
    """
    co_byte = 0

    for x in data:
        # Check the number of leading 1s
        if co_byte == 0:
            """char encod utf-8 1 byte"""
            if x >> 5 == 0b110:
                co_byte = 1
                """char encod utf-8 2 byte"""
            elif x >> 4 == 0b1110:
                co_byte = 2
                """char encod utf-8 3 byte"""
            elif x >> 3 == 0b11110:
                co_byte = 3
                """char encod utf-8 fals"""
            elif x >> 7 == 0b1:
                return False
        else:
            """cant count byte"""
            if x >> 6 != 0b10:
                return False
            co_byte -= 1

    return co_byte == 0
