import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
disable = set(map(int, sys.stdin.readline().split())) if M else set()
dp = [[1e10] * 110 for _ in range(N+6)]

dp[0][0] = 0

for i in range(N+1):
    for j in range(40):
        if dp[i][j] == 1e10:
            continue

        if i+1 in disable:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j])

        if j >= 3:
            dp[i+1][j-3] = min(dp[i][j], dp[i+1][j-3])

        # 1
        dp[i+1][j] = min(dp[i][j] + 10000, dp[i+1][j])

        # 3
        for k in range(1, 4):
            dp[i+k][j+1] = min(dp[i][j] + 25000, dp[i+k][j+1])

        # 5
        for k in range(1, 6):
            dp[i+k][j+2] = min(dp[i][j] + 37000, dp[i+k][j+2])

print(min(dp[N]))
