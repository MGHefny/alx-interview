#!/usr/bin/python3
""" N Queens function """

import sys


def possition(q, c, b):
    """Check if c-th queen can be placed in b-th column.

    Args:
        a: List representing the board configuration.
        c: Current row to check.
        b: Column to place the queen.

    Returns:
        bool: True if placement is valid, False otherwise.
    """
    for z in range(1, c):
        if q[z] == b or abs(q[z] - b) == abs(z - c):
            return False
    return True


def n_queen(a, q, c, result):
    """Solve the N Queens problem using backtracking.

    Args:
        a: Total number of queens.
        a: List representing the board configuration.
        c: Current row to check.
        result: List to collect solutions.
    """
    for b in range(1, a + 1):
        if possition(q, c, b):
            q[c] = b
            if c == a:
                sol = [[b - 1, q[b] - 1] for b in range(1, a + 1)]
                result.append(sol)
            else:
                n_queen(a, q, c + 1, result)


""" this the main function to main progress """
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
N = sys.argv[1]
try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
q = [0] * (N + 1)
result = []
n_queen(N, q, 1, result)
for sol in result:
    print(sol)
