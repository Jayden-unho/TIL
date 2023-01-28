import sys
from itertools import combinations
sys.stdin = open('input.txt')


def chk(coors):
    y, x = coors.pop()

    visited = {}
    visited[(y, x)] = 1

    stack = [(y, x)]
    limit = 2 if board[y][x] == 'Y' else 3
    coors = set(coors)
    while stack:
        y, x = stack.pop()

        for k in range(4):
            r = y + dr[k]
            c = x + dc[k]

            if (r, c) in coors and not visited.get((r, c), False):
                visited[(r, c)] = 1
                stack.append((r, c))
                if board[r][c] == 'Y':
                    limit -= 1

    if len(visited.keys()) == 7 and limit >= 0:
        return True
    return False


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

board = [list(sys.stdin.readline().strip()) for _ in range(5)]
coordinates = [(i, j) for j in range(5) for i in range(5)]
answer = 0

for comb in combinations(coordinates, 7):
    if chk(list(comb)):
        answer += 1

print(answer)
