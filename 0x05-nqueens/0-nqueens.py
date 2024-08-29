#!/usr/bin/python3
"""N Queens algorithm with backtracking"""

import sys

def place(x, k, i):
    """Check if k-th queen can be placed in i-th column.

    Args:
        x: List representing the board configuration.
        k: Current row to check.
        i: Column to place the queen.

    Returns:
        bool: True if placement is valid, False otherwise.
    """
    for j in range(1, k):
        if (x[j] == i or
                abs(x[j] - i) == abs(j - k)):
            return False
    return True

def n_queen(n, x, k, res):
    """Solve the N Queens problem using backtracking.

    Args:
        n: Total number of queens.
        x: List representing the board configuration.
        k: Current row to check.
        res: List to collect solutions.
    """
    for i in range(1, n + 1):
        if place(x, k, i):
            x[k] = i
            if k == n:
                solution = [[i - 1, x[i] - 1] for i in range(1, n + 1)]
                res.append(solution)
            else:
                n_queen(n, x, k + 1, res)

# Command-line argument handling
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Initialize board and results list
x = [0] * (n + 1)
res = []

# Solve the N Queens problem and print results
n_queen(n, x, 1, res)

for solution in res:
    print(solution)
