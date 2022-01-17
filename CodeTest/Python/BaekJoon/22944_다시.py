import sys
from collections import deque
sys.stdin = open('input.txt')

def solution(y, x):
    h = H
    u = 0
    q = deque([(y, x)])

    while q:
        node = q.popleft()
        for k in range(4):
            r = y + dr[k]
            c = x + dc[k]

            if 0 <= r < N and 0 <= c < N and not visited[r][c]:
                tmp_u = u
                tmp_h = h
                if board[r][c] == 'U':
                    tmp_u = D
                elif board[r][c] == '.':
                    if u > 0:
                        tmp_u -= 1
                    elif h > 1:
                        tmp_h -= 1
                tmp = tmp_u + tmp_h

                if dp[r][c] <= tmp:
                    visited[r][c] = visited[y][x] + 1
                    q.append((r, c))




dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, H, D = map(int, sys.stdin.readline().split())                    # 격자 길이, 현재 체력, 우산 내구도
board = [list(sys.stdin.readline().strip()) for _ in range(N)]      # U - 우산, S - 현재위치, E - 안전지대, . - 빈칸

visited = [[0] * N for _ in range(N)]
dp = [[0] * N for _ in range(N)]
umbrella = 0
answer = 1e10
end_flag = False

for i in range(N):
    for j in range(N):
        if board[i][j] == 'S':
            visited[i][j] = 1
            dp[i][j] = H
            solution(i, j)
            end_flag = True
            break
    if end_flag:
        break

if answer >= 1e10:
    print('-1')
else:
    print(answer)