import sys
from collections import deque
sys.stdin = open('input.txt')

def solution(y, x):
    q = deque([(y, x, 1)])
    visited[y][x] = (1, 1)

    while q:
        y, x, remain = q.popleft()
        for k in range(4):
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < N and 0 <= c < M:
                if board[r][c] == 1 and remain:
                    visited[r][c] = (visited[y][x][0] + 1, 0)
                    q.append((r, c, 0))
                elif board[r][c] == 0 and visited[r][c][0] > visited[y][x][0]:
                    visited[r][c] = (visited[y][x][0] + 1, remain)
                    q.append((r, c, remain))    


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited =[[(1e10, 0) for _ in range(M)] for _ in range(N)]

solution(0, 0)

if visited[N-1][M-1][0] >= 1e10:
    print(-1)
else:
    print(visited[N-1][M-1][0])