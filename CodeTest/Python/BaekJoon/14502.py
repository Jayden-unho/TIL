import sys
from collections import deque
from itertools import combinations
sys.stdin = open('input.txt')

def solution():
    global ans

    q = deque(start_coordinates)

    while q:
        node = q.popleft()
        for k in range(4):
            r = node[0] + dr[k]
            c = node[1] + dc[k]

            if 0 <= r < N and 0 <= c < M and not board[r][c] and (r, c) not in e and not visited[r][c]:
                visited[r][c] = 1
                ans -= 1
                q.append((r, c))


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
empty_coordinates = []
start_coordinates = []
wall = set()
answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            start_coordinates.append((i, j))
        elif board[i][j] == 0:
            empty_coordinates.append((i, j))

safe = len(empty_coordinates) - 3
for e in combinations(empty_coordinates, 3):
    visited = [[0] * M for _ in range(N)]
    ans = safe

    solution()
    
    answer = max(answer, ans)

print(answer)