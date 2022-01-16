import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')

def solution(y, x, h, u, ans):
    global answer 
    if board[y][x] == 'E':
        answer = ans
        return
    elif answer <= ans:
        return
    elif dp[y][x] > h + u:
        return
    elif dp[y][x] <= h + u:
        dp[y][x] = h + u
    
    for k in range(4):
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < N and 0 <= c < N and not visited[r][c]:
            # print(f'r: {r} / c: {c} / h: {h} / u: {u}')
            if board[r][c] == 'U':
                u = D
            elif board[r][c] == '.':
                if u > 0:
                    u -= 1
                elif h > 0:
                    h -= 1
                    if h <= 0:
                        return
                else:
                    return
                    
            visited[r][c] = 1
            solution(r, c, h, u, ans + 1)
            visited[r][c] = 0


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, H, D = map(int, sys.stdin.readline().split())                    # 격자 길이, 현재 체력, 우산 내구도
board = [list(sys.stdin.readline().strip()) for _ in range(N)]      # U - 우산, S - 현재위치, E - 안전지대, . - 빈칸
dp = [[0] * N for _ in range(N)]

visited = [[0] * N for _ in range(N)]
umbrella = 0
answer = 1e10
end_flag = False

for i in range(N):
    for j in range(N):
        if board[i][j] == 'S':
            visited[i][j] = 1
            dp[i][j] = H
            solution(i, j, H, 0, 0)
            end_flag = True
            break
    if end_flag:
        break

if answer >= 1e10:
    print('-1')
else:
    print(answer)