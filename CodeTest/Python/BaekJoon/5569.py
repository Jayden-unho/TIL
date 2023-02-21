import sys
sys.stdin = open('input.txt')


W, H = map(int, sys.stdin.readline().split())
dp = [[[[0, 0] for _ in range(2)] for _ in range(W)] for _ in range(H)]
# dp (y좌표, x좌표, 진행방향, 방향전환 가능여부)

# 초기 가장 자리는 한가지 경우만 존재
for i in range(1, H):
    dp[i][0][1][1] = 1

for j in range(1, W):
    dp[0][j][0][1] = 1


for i in range(1, H):
    for j in range(1, W):
        # 수평, 불가능
        dp[i][j][0][0] = dp[i][j-1][1][1] % 100000
        # 수평, 가능
        dp[i][j][0][1] = (dp[i][j-1][0][0] + dp[i][j-1][0][1]) % 100000
        # 수직, 불가능
        dp[i][j][1][0] = dp[i-1][j][0][1] % 100000
        # 수직, 가능
        dp[i][j][1][1] = (dp[i-1][j][1][0] + dp[i-1][j][1][1]) % 100000

answer = sum(dp[-1][-1][0]) + sum(dp[-1][-1][1])
print(answer % 100000)
