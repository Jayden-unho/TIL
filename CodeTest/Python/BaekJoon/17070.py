import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())                                               # 가로, 세로 길이
home = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]     # 집의 상태 0-빈칸, 1-벽
dp = [[[0] * (N+1) for _ in range(N+1)] for _ in range(3)]                  # 가로, 대각선, 세로

dp[0][1][2] = 1                                                                     # 처음에 (1, 1)과 (1, 2)를 차지하고 있으므로 가로 방향 1,2 경우의 수 1개
for i in range(1, N+1):                                                             # 1행부터 시작, 3열부터 시작
    for j in range(3, N+1):                                                         
        if home[i-1][j-1] == 0:                                                     # 다음에 놓을 칸이 빈 칸일때만
            dp[0][i][j] = dp[0][i][j-1] + dp[1][i][j-1]                             # 가로로 놓는 경우의 수 = 왼쪽 열의 가로 경우의 수 + 왼쪽 열의 대각선 경우의 수
            dp[2][i][j] = dp[2][i-1][j] + dp[1][i-1][j]                             # 세로로 놓는 경우의 수 = 위쪽 행의 세로 경우의 수 + 위쪽 행의 대각선 경우의 수
            if home[i-2][j-1] == 0 and home[i-1][j-2] == 0:                         # 대각선으로 놓을때 주변 4칸이 빈칸이여야 함
                dp[1][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]   # 대각선 놓는 경우의 수 = 왼쪽 위의 가로, 세로, 대각선 경우의 수를 모두 합함

print(dp[0][N][N] + dp[1][N][N] + dp[2][N][N])          # N, N 의 가로, 세로, 대각선의 모든 경우의 수를 더함

# ROTATION = {
#     0: [1, 0],
#     1: [1, 0, 2],
#     2: [1, 2]
# }

# def solution():
#     global answer

#     q = deque([[(0, 1), 0]])
    
#     while q:
#         node = q.popleft()
#         direction = node.pop()
#         y, x = node.pop()

#         if y == N-1 and x == N-1:
#             answer += 1
#             continue

#         for k in ROTATION[direction]:
#             r = y + dr[k]
#             c = x + dc[k]

#             if 0 <= r < N and 0 <= c < N and home[r][c] != 1:
#                 if k == 1 and (home[r-1][c] == 1 or home[r][c-1] == 1):
#                     continue
#                 q.append([(r, c), k])
                
# dr = [0, 1, 1]     # 가로, 대각선, 세로
# dc = [1, 1, 0]

# N = int(sys.stdin.readline())
# home = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# answer = 0

# solution()

# print(answer)