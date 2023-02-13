import sys
from collections import deque
sys.stdin = open('input.txt')


def can_move(y, x, d):
    if d == 0:
        for c in range(x, x+W):
            if board[y][c]:
                return False
    elif d == 1:
        nx = x+W-1
        if not (0 <= nx < M):
            return False
        for r in range(y, y+H):
            if board[r][nx]:
                return False
    elif d == 2:
        ny = y+H-1
        if not (0 <= ny < N):
            return False
        for c in range(x, x+W):
            if board[ny][c]:
                return False
    elif d == 3:
        for r in range(y, y+H):
            if board[r][x]:
                return False

    return True


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
H, W, SR, SC, TR, TC = map(int, sys.stdin.readline().split())
visited = [[-1] * M for _ in range(N)]

q = deque([(SR-1, SC-1)])
visited[SR-1][SC-1] = 0

while q and visited[TR-1][TC-1] == -1:
    y, x = q.popleft()
    for k in range(4):
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < M and visited[r][c] == -1 and can_move(r, c, k):
            visited[r][c] = visited[y][x] + 1
            q.append((r, c))

print(visited[TR-1][TC-1])
