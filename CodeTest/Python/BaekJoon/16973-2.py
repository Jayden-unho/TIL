import sys
from collections import deque
sys.stdin = open('input.txt')


def change_disable(y, x):
    for r in range(y-H+1, y+1):
        for c in range(x-W+1, x+1):
            if 0 <= r < N and 0 <= c < M:
                visited[r][c] = -1


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
H, W, SR, SC, TR, TC = map(int, sys.stdin.readline().split())
visited = [[0] * M for _ in range(N)]

for i in range(N+1):
    for j in range(M+1):
        if i == N or j == M or board[i][j]:
            change_disable(i, j)

q = deque([(SR-1, SC-1)])
visited[SR-1][SC-1] = 1

while q and not visited[TR-1][TC-1]:
    y, x = q.popleft()
    for k in range(4):
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < M and not visited[r][c]:
            visited[r][c] = visited[y][x] + 1
            q.append((r, c))

if visited[TR-1][TC-1] > 0:
    print(visited[TR-1][TC-1] - 1)
else:
    print(-1)
