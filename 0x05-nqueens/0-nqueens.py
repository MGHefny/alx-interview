#!/usr/bin/python3
""" N Queens function """
import sys


class NQueen:
    """" the nqueen function backtracking """

    def __init__(self, a):
        """ the init function """
        self.a = a
        self.q = [0 for b in range(a + 1)]
        self.result = []

    def possition(self, c, b):
        """ the index """
        for z in range(1, c):
            if self.q[z] == b or \
               abs(self.q[z] - b) == abs(z - c):
                return 0
        return 1

    def n_queen(self, c):
        """ the nqueen function backtracking """
        for b in range(1, self.a + 1):
            if self.possition(c, b):
                self.q[c] = b
                if c == self.a:
                    sol = []
                    for b in range(1, self.a + 1):
                        sol.append([b - 1, self.q[b] - 1])
                    self.result.append(sol)
                else:
                    self.n_queen(c + 1)
        return self.result



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

queen = NQueen(N)
result = queen.n_queen(1)

for b in result:
    print(b)







'''
#!/usr/bin/python3
""" N Queens function """

import sys


def possition(q, c, b):
    """ the index """
    for z in range(1, c):
        if q[z] == b or abs(q[z] - b) == abs(z - c):
            return False
    return True


def n_queen(a, q, c, result):
    """" the nqueen function backtracking """
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
'''
