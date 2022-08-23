import sys
sys.stdin = open('input.txt')

# 입력값
N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

# dp 값
dp = [0] * (K+1)
dp[0] = 1

# 동전별 가치를 나타내기 위해 필요한 개수
for i in range(N):
    for j in range(coins[i], K+1):
        dp[j] += dp[j-coins[i]]

print(dp[-1])
