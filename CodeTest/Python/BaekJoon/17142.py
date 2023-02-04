import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')


def find_ans():
    case_ans = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] != 1 and timed[i][j] == 1e5:
                return 1e5
            if timed[i][j] != 1e5:
                case_ans = max(
                    case_ans, 0 if lab[i][j] == 2 else timed[i][j])
    return case_ans


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1e5

virus = set()
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.add((i, j))

for comb in combinations(virus, M):
    q = deque(comb)
    timed = [[1e5] * N for _ in range(N)]
    for y, x in comb:
        timed[y][x] = 0

    while q:
        y, x = q.popleft()
        next_time = timed[y][x] + 1
        for k in range(4):
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < N and 0 <= c < N and lab[r][c] != 1 and timed[r][c] > next_time:
                timed[r][c] = next_time
                q.append((r, c))

    answer = min(answer, find_ans())

print(answer if answer != 1e5 else -1)
